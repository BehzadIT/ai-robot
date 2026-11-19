from __future__ import annotations

import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
REPOSITORIES = {
    "parent": ROOT,
    "android": ROOT / "robot-android-app",
    "esp32": ROOT / "robot-esp32-platform",
    "pico": ROOT / "robot-pico-platform",
}
ADAPTERS = {
    name: path / "tools" / "robot_adapter.py"
    for name, path in REPOSITORIES.items()
    if name != "parent"
}
LEVELS = ["static", "compile", "host", "simulation", "device", "hil", "physical"]
OUTCOME_PRIORITY = {"pass": 0, "skipped": 1, "inconclusive": 2, "blocked": 3, "fail": 4}
SECRET_PATTERN = re.compile(r"(?i)(password|passwd|secret|token|api[_-]?key)\s*[:=]\s*\S+")


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def redact(value: str) -> str:
    value = SECRET_PATTERN.sub(lambda match: match.group(1) + "=<redacted>", value)
    home = str(Path.home())
    return value.replace(home, "<home>") if home else value


def check(
    check_id: str,
    outcome: str,
    expected: str,
    observed: str,
    duration_ms: int = 0,
    category: str | None = None,
    exit_code: int | None = None,
) -> dict[str, Any]:
    return {
        "id": check_id,
        "outcome": outcome,
        "expected_signal": expected,
        "observed": redact(observed),
        "duration_ms": max(0, duration_ms),
        "failure_category": category,
        "exit_code": exit_code,
        "command": None,
    }


def result(command: str, level: str = "static") -> dict[str, Any]:
    timestamp = now()
    return {
        "schema_version": 1,
        "command": command,
        "scenario": None,
        "scenario_version": None,
        "started_at": timestamp,
        "finished_at": timestamp,
        "outcome": "pass",
        "verification_level": level,
        "physical_stage": None,
        "environment": {},
        "repositories": [],
        "devices": [],
        "checks": [],
        "artifacts": [],
        "approvals": [],
        "evidence_id": None,
        "safe_next_action": None,
    }


def aggregate_outcome(checks: list[dict[str, Any]]) -> str:
    if not checks:
        return "inconclusive"
    return max((item["outcome"] for item in checks), key=OUTCOME_PRIORITY.get)


def finish(payload: dict[str, Any]) -> dict[str, Any]:
    payload["finished_at"] = now()
    payload["outcome"] = aggregate_outcome(payload["checks"])
    return payload


def exit_code(payload: dict[str, Any]) -> int:
    outcome = payload["outcome"]
    if outcome == "pass":
        return 0
    categories = {item.get("failure_category") for item in payload.get("checks", [])}
    if outcome == "fail":
        if "build_failed" in categories:
            return 11
        if "flash_failed" in categories:
            return 12
        if "boot_timeout" in categories:
            return 13
        if "protocol_failed" in categories:
            return 14
        return 15
    if outcome == "blocked":
        if categories & {"device_absent", "device_ambiguous", "permission_denied", "resource_busy"}:
            return 21
        if "unsafe_precondition" in categories:
            return 22
        if "human_action_required" in categories:
            return 23
        return 20
    return 30 if outcome == "skipped" else 31


def repository_identity(name: str, path: Path) -> dict[str, Any]:
    def git(*args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(["git", "-C", str(path), *args], text=True, capture_output=True, check=False)

    sha = git("rev-parse", "HEAD")
    status = git("status", "--porcelain")
    branch = git("branch", "--show-current")
    return {
        "name": name,
        "path": str(path.relative_to(ROOT)) if path != ROOT else ".",
        "sha": sha.stdout.strip() if sha.returncode == 0 else None,
        "branch": branch.stdout.strip() if branch.returncode == 0 else None,
        "dirty": bool(status.stdout.strip()) if status.returncode == 0 else None,
    }


def load_local_config(path: Path | None = None) -> dict[str, Any]:
    path = path or ROOT / ".robot" / "local.yaml"
    if not path.exists():
        return {"schema_version": 1, "sdk_paths": {}, "device_aliases": {}}
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("local configuration root must be a mapping")
    allowed = {"schema_version", "sdk_paths", "device_aliases"}
    unknown = set(value) - allowed
    if unknown:
        raise ValueError(f"unknown local configuration keys: {sorted(unknown)}")
    if value.get("schema_version") != 1:
        raise ValueError("local configuration schema_version must be 1")
    for section in ("sdk_paths", "device_aliases"):
        if not isinstance(value.get(section, {}), dict):
            raise ValueError(f"{section} must be a mapping")
    sdk_paths = value.get("sdk_paths", {})
    unknown_sdks = set(sdk_paths) - {"android", "esp_idf", "pico"}
    if unknown_sdks:
        raise ValueError(f"unknown SDK path keys: {sorted(unknown_sdks)}")
    for name, sdk_path in sdk_paths.items():
        if sdk_path is not None and not isinstance(sdk_path, str):
            raise ValueError(f"SDK path {name} must be a string or null")
    identities: set[tuple[str, str]] = set()
    for alias, record in value.get("device_aliases", {}).items():
        if not isinstance(alias, str) or not isinstance(record, dict):
            raise ValueError("device aliases must map names to records")
        unknown_alias_keys = set(record) - {"kind", "usb_serial", "serial"}
        if unknown_alias_keys:
            raise ValueError(f"unknown keys for device alias {alias}: {sorted(unknown_alias_keys)}")
        kind = record.get("kind")
        if kind not in {"pico", "esp32", "adb", "android"}:
            raise ValueError(f"device alias {alias} has unsupported kind {kind!r}")
        stable_id = record.get("usb_serial") or record.get("serial")
        if not isinstance(stable_id, str) or not stable_id or stable_id == "replace-me":
            raise ValueError(f"device alias {alias} needs a real stable serial identity")
        identity = (kind, stable_id)
        if identity in identities:
            raise ValueError(f"duplicate device identity for alias {alias}")
        identities.add(identity)
    return value


def run_process(command: list[str], cwd: Path, timeout: int = 900, env: dict[str, str] | None = None) -> tuple[subprocess.CompletedProcess[str], int]:
    started = time.monotonic()
    try:
        completed = subprocess.run(command, cwd=cwd, env=env, text=True, capture_output=True, timeout=timeout, check=False)
    except subprocess.TimeoutExpired as exc:
        completed = subprocess.CompletedProcess(command, 124, exc.stdout or "", exc.stderr or "timeout")
    return completed, int((time.monotonic() - started) * 1000)


def passive_devices() -> list[dict[str, Any]]:
    devices: list[dict[str, Any]] = []
    seen_ports: set[str] = set()
    by_id = Path("/dev/serial/by-id")
    if by_id.is_dir():
        for link in sorted(by_id.iterdir()):
            try:
                target = str(link.resolve())
            except OSError:
                target = "unresolved"
            seen_ports.add(target)
            devices.append({"kind": "serial", "stable_id": link.name, "port": target, "source": "serial-by-id", "holders": port_holders(target)})
    for pattern in ("ttyACM*", "ttyUSB*"):
        for port in sorted(Path("/dev").glob(pattern)):
            if str(port) not in seen_ports:
                devices.append({"kind": "serial", "stable_id": port.name, "port": str(port), "source": "transient-device-node", "holders": port_holders(str(port))})
    adb = shutil.which("adb")
    if adb:
        completed, _ = run_process([adb, "devices", "-l"], ROOT, 10)
        for line in completed.stdout.splitlines()[1:]:
            fields = line.split()
            if len(fields) >= 2:
                devices.append({"kind": "adb", "stable_id": fields[0], "state": fields[1], "metadata": fields[2:], "source": "adb"})
    for base in (Path("/run/media"), Path("/media"), Path("/mnt")):
        if not base.exists():
            continue
        for candidate in base.rglob("*"):
            if candidate.is_dir() and candidate.name in {"RP2350", "RPI-RP2"}:
                devices.append({"kind": "uf2", "stable_id": candidate.name, "mount": str(candidate), "source": "mount"})
    return devices


def port_holders(port: str) -> list[int]:
    fuser = shutil.which("fuser")
    if not fuser or not port.startswith("/dev/"):
        return []
    completed = subprocess.run([fuser, port], text=True, capture_output=True, check=False)
    holders: list[int] = []
    for token in completed.stdout.split():
        try:
            holders.append(int(token))
        except ValueError:
            continue
    return holders


def adapter_call(platform_name: str, arguments: list[str], timeout: int = 1800) -> dict[str, Any]:
    adapter = ADAPTERS[platform_name]
    if not adapter.is_file():
        payload = result(f"adapter {platform_name}")
        payload["checks"].append(check(f"{platform_name}.adapter", "blocked", "platform adapter exists", f"missing {adapter}", category="environment_missing"))
        payload["safe_next_action"] = f"Implement {platform_name} tools/robot_adapter.py."
        return finish(payload)
    env = dict(os.environ)
    try:
        sdk_paths = load_local_config().get("sdk_paths", {})
    except ValueError:
        sdk_paths = {}
    sdk_path = sdk_paths.get(platform_name)
    if platform_name == "android" and sdk_path:
        env["ANDROID_HOME"] = sdk_path
    elif platform_name == "esp32" and sdk_paths.get("esp_idf"):
        env["IDF_PATH"] = sdk_paths["esp_idf"]
    elif platform_name == "pico" and sdk_path:
        env["PICO_SDK_PATH"] = sdk_path
    completed, duration = run_process([sys.executable, str(adapter), *arguments, "--json"], adapter.parent.parent, timeout, env)
    if completed.returncode not in range(0, 32) or not completed.stdout.strip():
        payload = result(f"adapter {platform_name}")
        payload["checks"].append(check(f"{platform_name}.adapter", "fail", "schema-valid adapter result", completed.stderr or completed.stdout, duration, "adapter_failed", completed.returncode))
        return finish(payload)
    try:
        value = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        payload = result(f"adapter {platform_name}")
        payload["checks"].append(check(f"{platform_name}.adapter", "fail", "JSON adapter result", str(exc), duration, "adapter_failed", completed.returncode))
        return finish(payload)
    return value


def merge(parent: dict[str, Any], child: dict[str, Any]) -> None:
    parent["checks"].extend(child.get("checks", []))
    known_devices = {(entry.get("kind"), entry.get("stable_id")) for entry in parent["devices"]}
    for device in child.get("devices", []):
        identity = (device.get("kind"), device.get("stable_id"))
        if identity not in known_devices:
            parent["devices"].append(device)
            known_devices.add(identity)
    parent["artifacts"].extend(child.get("artifacts", []))
    child_environment = child.get("environment", {})
    platform_name = child_environment.get("platform")
    if platform_name:
        parent["environment"].setdefault("platforms", {})[platform_name] = child_environment
    known_repositories = {(entry.get("name"), entry.get("sha")) for entry in parent["repositories"]}
    for repository in child.get("repositories", []):
        identity = (repository.get("name"), repository.get("sha"))
        if identity not in known_repositories:
            parent["repositories"].append(repository)
            known_repositories.add(identity)
    if LEVELS.index(child.get("verification_level", "static")) > LEVELS.index(parent["verification_level"]):
        parent["verification_level"] = child["verification_level"]
    if child.get("safe_next_action") and not parent.get("safe_next_action"):
        parent["safe_next_action"] = child["safe_next_action"]


def describe(platform_name: str) -> dict[str, Any]:
    return adapter_call(platform_name, ["describe"], 30)


def resolve_gate(platform_name: str, scenario: str) -> tuple[int, str]:
    description = describe(platform_name)
    for entry in description.get("environment", {}).get("scenarios", []):
        if entry.get("id") == scenario:
            return int(entry.get("gate", 0)), entry.get("description", scenario)
    return 0, scenario


def request_approval(gate: int, platform_name: str, scenario: str, device_alias: str | None, description: str) -> list[str]:
    if gate == 0:
        return []
    if not sys.stdin.isatty():
        raise PermissionError("device or physical scenario requires an interactive terminal")
    target = device_alias or "unresolved device"
    answer = input(f"Gate {gate}: run {scenario} on {platform_name} target {target}: {description}? [y/N] ").strip().lower()
    if answer not in {"y", "yes"}:
        raise PermissionError("owner did not approve the device operation")
    approvals = [f"owner confirmed gate {gate} for {scenario} on {target} at {now()}"]
    if gate >= 2:
        checklist = ["wiring/current protection checked", "emergency disconnect ready"]
        if gate >= 3:
            checklist.extend(["tracks lifted or restrained", "bounded stop path verified"])
        if gate >= 4:
            checklist.extend(["test area clear", "manual observer ready"])
        for item in checklist:
            response = input(f"Confirm {item}? [y/N] ").strip().lower()
            if response not in {"y", "yes"}:
                raise PermissionError(f"unsafe precondition not confirmed: {item}")
            approvals.append(f"owner confirmed: {item}")
    return approvals


def validate_result(payload: dict[str, Any]) -> None:
    import jsonschema

    schema_path = ROOT / "docs" / "reference" / "schemas" / "verification-result.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(payload)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
