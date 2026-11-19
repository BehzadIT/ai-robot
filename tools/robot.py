#!/usr/bin/env python3
"""Discover, verify, and retain evidence for the integrated robot workspace."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from robotlib.core import (
    REPOSITORIES,
    ROOT,
    adapter_call,
    check,
    exit_code,
    finish,
    load_local_config,
    merge,
    now,
    passive_devices,
    repository_identity,
    request_approval,
    resolve_gate,
    result,
    sha256,
    validate_result,
)


DEFAULT_SCENARIOS = {
    "android": "android-default",
    "esp32": "esp32-default",
    "pico-host": "pico-host-default",
    "pico-firmware": "pico-firmware-compile",
}
SCENARIO_REGISTRY = yaml.safe_load(
    (ROOT / "docs" / "reference" / "scenario-registry.yaml").read_text(encoding="utf-8")
)
SCENARIO_PLATFORM = {
    entry["id"]: entry["target"] for entry in SCENARIO_REGISTRY["scenarios"]
}


def doctor(platform_name: str) -> dict[str, Any]:
    payload = result("doctor")
    payload["environment"] = {
        "python": sys.version.split()[0],
        "host": sys.platform,
        "read_only": True,
    }
    payload["repositories"] = [repository_identity(name, path) for name, path in REPOSITORIES.items()]
    payload["checks"].append(check("parent.workspace", "pass", "four readable Git repositories", "parent and three platform repositories found"))
    targets = ["android", "esp32", "pico"] if platform_name == "all" else [platform_name]
    for target in targets:
        merge(payload, adapter_call(target, ["doctor"]))
    return finish(payload)


def inventory() -> dict[str, Any]:
    payload = result("inventory")
    payload["repositories"] = [repository_identity(name, path) for name, path in REPOSITORIES.items()]
    payload["devices"] = passive_devices()
    payload["checks"].append(check("inventory.passive", "pass", "passive device enumeration", f"observed {len(payload['devices'])} dynamic device(s)"))
    try:
        local = load_local_config()
        payload["environment"] = {"configured_aliases": sorted(local["device_aliases"]), "canonical_registries": ["components", "tools"]}
        payload["checks"].append(check("inventory.config", "pass", "valid optional local configuration", f"{len(local['device_aliases'])} alias(es) configured"))
    except ValueError as exc:
        payload["checks"].append(check("inventory.config", "blocked", "valid local configuration", str(exc), category="environment_missing"))
    return finish(payload)


def verify(target: str, scenario: str | None, device: str | None) -> dict[str, Any]:
    platform_name = "pico" if target.startswith("pico-") else target
    selected = scenario or DEFAULT_SCENARIOS[target]
    gate, description = resolve_gate(platform_name, selected)
    payload = result(f"verify {target}")
    payload["scenario"] = selected
    payload["scenario_version"] = 1
    resolved_device: dict[str, Any] | None = None
    try:
        config = load_local_config()
        if gate > 0:
            if not device:
                raise ValueError("--device alias is required for device-changing or physical scenarios")
            if device not in config["device_aliases"]:
                raise ValueError(f"unknown device alias: {device}")
            declared = config["device_aliases"][device]
            observed = passive_devices()
            expected_kind = declared.get("kind")
            identity = declared.get("serial") or declared.get("usb_serial")
            matches = [
                candidate for candidate in observed
                if (expected_kind in {"android", "adb"} and candidate.get("kind") == "adb" or
                    expected_kind in {"pico", "esp32"} and candidate.get("kind") == "serial")
                and identity and identity in str(candidate.get("stable_id", ""))
            ]
            if len(matches) != 1:
                raise ValueError(f"device alias {device} resolved to {len(matches)} connected devices; expected exactly one")
            resolved_device = {"alias": device, "declared": declared, "observed": matches[0]}
        payload["approvals"] = request_approval(gate, platform_name, selected, device, description)
    except (ValueError, PermissionError) as exc:
        payload["checks"].append(check("approval", "blocked", "resolved device and owner confirmation", str(exc), category="unsafe_precondition" if gate >= 2 else "human_action_required"))
        payload["safe_next_action"] = "Configure the device alias and rerun interactively after establishing the stated preconditions."
        return finish(payload)
    arguments = ["verify", selected]
    device_path: Path | None = None
    if resolved_device:
        device_dir = ROOT / "temp" / "us003"
        device_dir.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", prefix="device-", dir=device_dir, delete=False) as stream:
            json.dump(resolved_device, stream)
            device_path = Path(stream.name)
        arguments.extend(["--device-json", str(device_path)])
    try:
        child = adapter_call(platform_name, arguments)
    finally:
        if device_path:
            device_path.unlink(missing_ok=True)
    merge(payload, child)
    payload["approvals"].extend(child.get("approvals", []))
    return finish(payload)


def stage_evidence(scenario: str, payload: dict[str, Any]) -> tuple[str, Path]:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_id = f"RUN-{stamp}-{scenario.lower()}"
    run_dir = ROOT / "temp" / "us003" / "runs" / run_id
    suffix = 1
    while run_dir.exists():
        suffix += 1
        run_id = f"RUN-{stamp}-{scenario.lower()}-{suffix}"
        run_dir = ROOT / "temp" / "us003" / "runs" / run_id
    (run_dir / "raw").mkdir(parents=True)
    (run_dir / "artifacts").mkdir()
    result_path = run_dir / "result.json"
    result_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    repositories: list[dict[str, Any]] = []
    seen_repositories: set[tuple[str, str]] = set()
    for repository in payload.get("repositories", []):
        identity = (repository.get("name"), repository.get("sha"))
        if identity in seen_repositories or not identity[0] or not identity[1]:
            continue
        seen_repositories.add(identity)
        repositories.append({"name": identity[0], "sha": identity[1], "dirty": bool(repository.get("dirty"))})
    software_tools: list[dict[str, Any]] = []
    for platform_environment in payload.get("environment", {}).get("platforms", {}).values():
        software_tools.extend(platform_environment.get("software_tools", []))
    metadata = {
        "schema_version": 2,
        "id": None,
        "run_id": run_id,
        "started_at": payload["started_at"],
        "finished_at": payload["finished_at"],
        "operator": "owner",
        "observation_origin": ["agent", "software"] + (["human"] if payload.get("approvals") else []),
        "scenario": {"id": scenario, "version": payload.get("scenario_version") or 1},
        "verification_level": payload["verification_level"],
        "physical_stage": payload.get("physical_stage"),
        "outcome": payload["outcome"],
        "system_identity": {"hardware_revision": None, "harness_revision": None, "electrical_revision": None, "mechanical_revision": None, "configuration": None, "calibration": None, "repositories": repositories},
        "tools": [],
        "software_tools": software_tools,
        "commands": [entry["command"] for entry in payload.get("checks", []) if entry.get("command")],
        "preconditions": [],
        "approvals": payload.get("approvals", []),
        "measurements": [],
        "checks": payload.get("checks", []),
        "links": {"backlog_ids": ["US-003"], "component_ids": [], "question_ids": [], "decision_ids": []},
        "artifacts": [{"path": "result.json", "sha256": sha256(result_path), "kind": "structured-result"}],
        "safe_next_action": payload.get("safe_next_action"),
    }
    (run_dir / "metadata.yaml").write_text(yaml.safe_dump(metadata, sort_keys=False), encoding="utf-8")
    (run_dir / "procedure.md").write_text(f"# Procedure\n\nScenario `{scenario}` version 1 executed through `tools/robot.py`.\n", encoding="utf-8")
    (run_dir / "result.md").write_text(f"# Result\n\nOutcome: `{payload['outcome']}`  \nVerification level: `{payload['verification_level']}`\n", encoding="utf-8")
    return run_id, run_dir


def promote(run_id: str) -> dict[str, Any]:
    payload = result(f"evidence promote {run_id}")
    run_dir = (ROOT / "temp" / "us003" / "runs" / run_id).resolve()
    allowed = (ROOT / "temp" / "us003" / "runs").resolve()
    if allowed not in run_dir.parents or not run_dir.is_dir():
        payload["checks"].append(check("evidence.run", "blocked", "existing staged run", f"not found: {run_id}", category="environment_missing"))
        return finish(payload)
    metadata_path = run_dir / "metadata.yaml"
    metadata = yaml.safe_load(metadata_path.read_text(encoding="utf-8"))
    year = datetime.now(timezone.utc).year
    evidence_root = ROOT / "docs" / "verification" / "evidence"
    existing = sorted(evidence_root.glob(f"EV-{year}-[0-9][0-9][0-9]"))
    number = max([int(path.name.rsplit("-", 1)[1]) for path in existing] or [0]) + 1
    evidence_id = f"EV-{year}-{number:03d}"
    destination = evidence_root / evidence_id
    metadata["id"] = evidence_id
    import jsonschema

    schema = json.loads((ROOT / "docs" / "reference" / "schemas" / "evidence-metadata.schema.json").read_text(encoding="utf-8"))
    try:
        jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(metadata)
    except jsonschema.ValidationError as exc:
        payload["checks"].append(check("evidence.schema", "blocked", "schema-valid staged evidence", exc.message, category="environment_missing"))
        return finish(payload)
    for required_name in ("procedure.md", "result.md"):
        if not (run_dir / required_name).is_file():
            payload["checks"].append(check("evidence.files", "blocked", "procedure.md and result.md exist", f"missing {required_name}", category="environment_missing"))
            return finish(payload)
    for artifact in metadata.get("artifacts", []):
        artifact_path = (run_dir / artifact["path"]).resolve()
        if run_dir not in artifact_path.parents or not artifact_path.is_file():
            payload["checks"].append(check("evidence.artifact", "blocked", "artifact stays inside staged run and exists", artifact["path"], category="environment_missing"))
            return finish(payload)
        if sha256(artifact_path) != artifact["sha256"]:
            payload["checks"].append(check("evidence.artifact", "blocked", "artifact hash matches metadata", artifact["path"], category="assertion_failed"))
            return finish(payload)
    for path in run_dir.rglob("*"):
        if path.is_file() and path.stat().st_size <= 2_000_000:
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if any(marker in content.lower() for marker in ("password=", "password:", "api_key=", "token=")):
                payload["checks"].append(check("evidence.secrets", "blocked", "no secret-like content", f"secret-like marker in {path.relative_to(run_dir)}", category="unsafe_precondition"))
                return finish(payload)
    try:
        shutil.copytree(run_dir, destination)
    except FileExistsError:
        payload["checks"].append(check("evidence.allocate", "blocked", "unused evidence ID", f"concurrent allocation used {evidence_id}", category="resource_busy"))
        payload["safe_next_action"] = "Rerun promotion so a new evidence ID can be allocated."
        return finish(payload)
    (destination / "metadata.yaml").write_text(yaml.safe_dump(metadata, sort_keys=False), encoding="utf-8")
    payload["evidence_id"] = evidence_id
    payload["checks"].append(check("evidence.promote", "pass", "new immutable evidence bundle", str(destination.relative_to(ROOT))))
    validation = subprocess.run(
        [sys.executable, "tools/docs/validate_us002_records.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    payload["checks"].append(
        check(
            "evidence.canonical_validation",
            "pass" if validation.returncode == 0 else "fail",
            "canonical registry and evidence validation succeeds",
            (validation.stdout + "\n" + validation.stderr).strip(),
            category=None if validation.returncode == 0 else "assertion_failed",
            exit_code=validation.returncode,
        )
    )
    if validation.returncode != 0:
        payload["safe_next_action"] = (
            "Do not modify the promoted bundle; correct the validator or linked canonical records "
            "with a follow-up change and retain this failed promotion result."
        )
    return finish(payload)


def emit(payload: dict[str, Any], as_json: bool) -> None:
    validate_result(payload)
    if as_json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return
    print(f"{payload['command']}: {payload['outcome']} ({payload['verification_level']})")
    for item in payload["checks"]:
        print(f"[{item['outcome']}] {item['id']}: {item['observed']}")
    if payload.get("safe_next_action"):
        print(f"Next: {payload['safe_next_action']}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    doctor_parser = sub.add_parser("doctor")
    doctor_parser.add_argument("--platform", choices=["all", "android", "esp32", "pico"], default="all")
    doctor_parser.add_argument("--json", action="store_true")
    inventory_parser = sub.add_parser("inventory")
    inventory_parser.add_argument("--json", action="store_true")
    verify_parser = sub.add_parser("verify")
    verify_parser.add_argument("target", choices=["android", "esp32", "pico-host", "pico-firmware", "integration"])
    verify_parser.add_argument("--scenario")
    verify_parser.add_argument("--device")
    verify_parser.add_argument("--json", action="store_true")
    evidence_parser = sub.add_parser("evidence")
    evidence_sub = evidence_parser.add_subparsers(dest="evidence_command", required=True)
    run_parser = evidence_sub.add_parser("run")
    run_parser.add_argument("scenario")
    run_parser.add_argument("--device")
    run_parser.add_argument("--json", action="store_true")
    promote_parser = evidence_sub.add_parser("promote")
    promote_parser.add_argument("run_id")
    promote_parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "doctor":
        payload = doctor(args.platform)
    elif args.command == "inventory":
        payload = inventory()
    elif args.command == "verify":
        if args.target == "integration" and not args.scenario:
            raise SystemExit("verify integration requires --scenario")
        mapped = SCENARIO_PLATFORM.get(args.scenario, args.target) if args.target == "integration" else args.target
        payload = verify(mapped, args.scenario, args.device)
    elif args.evidence_command == "run":
        if args.scenario not in SCENARIO_PLATFORM:
            raise SystemExit(f"unknown evidence scenario: {args.scenario}")
        payload = verify(SCENARIO_PLATFORM[args.scenario], args.scenario, args.device)
        run_id, run_dir = stage_evidence(args.scenario, payload)
        payload["environment"]["staged_run_id"] = run_id
        payload["artifacts"].append({"path": str(run_dir.relative_to(ROOT)), "kind": "staged-evidence"})
    else:
        payload = promote(args.run_id)
    emit(payload, args.json)
    return exit_code(payload)


if __name__ == "__main__":
    raise SystemExit(main())
