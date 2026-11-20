#!/usr/bin/env python3
"""Validate US-002 registries, provenance, evidence, and generated indexes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT / "docs" / "reference"
SCHEMAS = REFERENCE / "schemas"
EVIDENCE = ROOT / "docs" / "verification" / "evidence"
COMPONENT_PACKS = ROOT / "docs" / "assets" / "components"
PROCEDURES = ROOT / "docs" / "verification" / "procedures"

REQUIRED_PROCEDURE_HEADINGS = (
    "Goal",
    "Why this is needed",
    "Tools and protective equipment",
    "Safe setup",
    "Procedure",
    "Expected result and tolerance",
    "Failure indications",
    "Stop conditions",
    "How the result changes the decision",
    "Evidence to retain",
)

REGISTRIES = {
    "components": (
        REFERENCE / "component-registry.yaml",
        SCHEMAS / "component-registry.schema.json",
    ),
    "tools": (
        REFERENCE / "tool-registry.yaml",
        SCHEMAS / "tool-registry.schema.json",
    ),
    "sources": (
        REFERENCE / "source-registry.yaml",
        SCHEMAS / "source-registry.schema.json",
    ),
    "questions_us002": (
        ROOT / "docs" / "verification" / "questions" / "US-002.yaml",
        SCHEMAS / "question-registry.schema.json",
    ),
    "questions_us003": (
        ROOT / "docs" / "verification" / "questions" / "US-003.yaml",
        SCHEMAS / "us003-question-registry.schema.json",
    ),
}

ADDITIONAL_RECORDS = {
    "toolchain_requirements": (
        REFERENCE / "toolchain-requirements.yaml",
        SCHEMAS / "toolchain-requirements.schema.json",
    ),
    "scenario_registry": (
        REFERENCE / "scenario-registry.yaml",
        SCHEMAS / "scenario-registry.schema.json",
    ),
}


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as stream:
        value = yaml.safe_load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: root must be a mapping")
    return value


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def provenance_refs(record: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for claim in record.get("claims", []):
        yield from claim.get("provenance", [])
    yield from record.get("provenance", [])


def validate_schema(name: str, data: dict[str, Any], schema_path: Path, errors: list[str]) -> None:
    validator = jsonschema.Draft202012Validator(load_json(schema_path), format_checker=jsonschema.FormatChecker())
    for error in sorted(validator.iter_errors(data), key=lambda item: list(item.absolute_path)):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"{name}:{location}: {error.message}")


def collect_ids(records: Iterable[dict[str, Any]], label: str, errors: list[str]) -> set[str]:
    found: set[str] = set()
    for record in records:
        record_id = record.get("id")
        if record_id in found:
            errors.append(f"{label}: duplicate id {record_id}")
        found.add(record_id)
    return found


def load_markdown_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML front matter")
    closing = text.find("\n---\n", 4)
    if closing == -1:
        raise ValueError("unterminated YAML front matter")
    value = yaml.safe_load(text[4:closing])
    if not isinstance(value, dict):
        raise ValueError("front matter must be a mapping")
    return value


def validate_component_documentation(
    components: list[dict[str, Any]],
    sources: list[dict[str, Any]],
    errors: list[str],
) -> dict[str, dict[str, Any]]:
    schema = load_json(SCHEMAS / "component-documentation.schema.json")
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    source_by_id = {source["id"]: source for source in sources}
    vendor_sources_by_component: dict[str, set[str]] = {}
    for source in sources:
        if source["kind"] not in {"vendor-manual", "vendor-web-page"}:
            continue
        for component_id in source.get("component_ids", []):
            vendor_sources_by_component.setdefault(component_id, set()).add(source["id"])

    metadata_by_component: dict[str, dict[str, Any]] = {}
    citation_pattern = re.compile(
        r"\[([^\]]*(source-[a-z0-9-]+)[^\]]*)\]\(([^)]+)\)"
    )
    for component in components:
        component_id = component["id"]
        documentation_value = component.get("documentation")
        requirement = component["documentation_requirement"]
        if requirement == "required" and not documentation_value:
            errors.append(f"{component_id}: required component lacks documentation")
            continue
        if not documentation_value:
            continue

        documentation = ROOT / documentation_value
        if not documentation.is_file():
            errors.append(f"{component_id}: documentation does not exist: {documentation_value}")
            continue
        try:
            metadata = load_markdown_frontmatter(documentation)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{documentation.relative_to(ROOT)}: {exc}")
            continue

        for error in validator.iter_errors(metadata):
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            errors.append(f"{documentation.relative_to(ROOT)}:{location}: {error.message}")
        if metadata.get("component_id") != component_id:
            errors.append(f"{documentation.relative_to(ROOT)}: component_id must be {component_id}")

        status = metadata.get("documentation_status")
        reviewed_sources = metadata.get("reviewed_sources", [])
        coverage = metadata.get("coverage", {})
        if status == "stub" and reviewed_sources:
            errors.append(f"{component_id}: stub documentation cannot claim reviewed sources")
        if status == "curated":
            if not metadata.get("reviewed_on"):
                errors.append(f"{component_id}: curated documentation needs reviewed_on")
            incomplete = [
                key for key, value in coverage.items()
                if value in {"partial", "pending"}
            ]
            if incomplete:
                errors.append(
                    f"{component_id}: curated documentation has incomplete coverage {sorted(incomplete)}"
                )

        reviewed_ids: set[str] = set()
        for reviewed in reviewed_sources:
            source_id = reviewed.get("id")
            if source_id in reviewed_ids:
                errors.append(f"{component_id}: duplicate reviewed source {source_id}")
                continue
            reviewed_ids.add(source_id)
            source = source_by_id.get(source_id)
            if not source:
                errors.append(f"{component_id}: unknown reviewed source {source_id}")
                continue
            if component_id not in source.get("component_ids", []):
                errors.append(f"{component_id}: reviewed source {source_id} is not mapped to component")
            if reviewed.get("sha256") != source["sha256"]:
                errors.append(f"{component_id}: reviewed source {source_id} hash is stale")

        if status == "curated":
            expected = vendor_sources_by_component.get(component_id, set())
            if reviewed_ids != expected:
                errors.append(
                    f"{component_id}: curated reviewed sources must equal mapped vendor sources; "
                    f"expected {sorted(expected)}, observed {sorted(reviewed_ids)}"
                )

        cited_ids: set[str] = set()
        text = documentation.read_text(encoding="utf-8")
        for label, source_id, raw_target in citation_pattern.findall(text):
            cited_ids.add(source_id)
            source = source_by_id.get(source_id)
            if not source:
                errors.append(f"{documentation.relative_to(ROOT)}: citation uses unknown {source_id}")
                continue
            path_part, separator, fragment = raw_target.partition("#")
            resolved = (documentation.parent / path_part).resolve()
            registered = (ROOT / source["path"]).resolve()
            if resolved != registered:
                errors.append(
                    f"{documentation.relative_to(ROOT)}: {source_id} citation path does not match registry"
                )
            if registered.suffix.lower() == ".pdf":
                page_label = re.search(r"PDF p\. ([0-9]+)", label)
                page_fragment = re.fullmatch(r"page=([0-9]+)", fragment)
                if not page_label or not page_fragment:
                    errors.append(
                        f"{documentation.relative_to(ROOT)}: {source_id} PDF citation needs "
                        "'PDF p. N' and '#page=N'"
                    )
                elif page_label.group(1) != page_fragment.group(1):
                    errors.append(
                        f"{documentation.relative_to(ROOT)}: {source_id} citation page label and fragment differ"
                    )
            elif source["kind"] == "vendor-web-page" and ("§" not in label or not separator or not fragment):
                errors.append(
                    f"{documentation.relative_to(ROOT)}: {source_id} HTML citation needs a section and anchor"
                )

        if status == "curated" and not reviewed_ids.issubset(cited_ids):
            errors.append(
                f"{component_id}: curated component documentation lacks citations for "
                f"{sorted(reviewed_ids - cited_ids)}"
            )
        metadata_by_component[component_id] = metadata

    return metadata_by_component


def validate_references(data: dict[str, dict[str, Any]], errors: list[str]) -> None:
    components = data["components"]["components"]
    tools = data["tools"]["tools"]
    sources = data["sources"]["sources"]
    questions_us002 = data["questions_us002"]["questions"]
    questions_us003 = data["questions_us003"]["questions"]
    questions = [*questions_us002, *questions_us003]

    component_ids = collect_ids(components, "components", errors)
    tool_ids = collect_ids(tools, "tools", errors)
    source_ids = collect_ids(sources, "sources", errors)
    question_ids = collect_ids(questions, "questions", errors)
    us002_question_ids = {question["id"] for question in questions_us002}

    all_ids: set[str] = set()
    for namespace, ids in (
        ("component", component_ids),
        ("tool", tool_ids),
        ("source", source_ids),
        ("question", question_ids),
    ):
        overlap = all_ids.intersection(ids)
        if overlap:
            errors.append(f"{namespace}: IDs reused across namespaces: {sorted(overlap)}")
        all_ids.update(ids)

    assembly_graph: dict[str, list[str]] = {}
    for component in components:
        component_id = component["id"]
        members = component.get("member_component_ids", [])
        assembly_graph[component_id] = members
        for member_id in members:
            if member_id not in component_ids:
                errors.append(f"{component_id}: unknown member component {member_id}")
            if member_id == component_id:
                errors.append(f"{component_id}: component cannot contain itself")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit_assembly(component_id: str, path: list[str]) -> None:
        if component_id in visiting:
            cycle_start = path.index(component_id)
            errors.append(f"components: assembly cycle {' -> '.join(path[cycle_start:])}")
            return
        if component_id in visited or component_id not in assembly_graph:
            return
        visiting.add(component_id)
        for member_id in assembly_graph[component_id]:
            visit_assembly(member_id, [*path, member_id])
        visiting.remove(component_id)
        visited.add(component_id)

    for component_id in assembly_graph:
        visit_assembly(component_id, [component_id])

    for record in [*components, *tools]:
        record_id = record["id"]
        for question_id in record.get("question_ids", []):
            if question_id not in us002_question_ids:
                errors.append(f"{record_id}: unknown question reference {question_id}")
        for provenance in provenance_refs(record):
            source_id = provenance.get("source_id")
            if source_id and source_id not in source_ids:
                errors.append(f"{record_id}: unknown source reference {source_id}")
        claim_keys: set[str] = set()
        for claim in record.get("claims", []):
            if claim["key"] in claim_keys:
                errors.append(f"{record_id}: duplicate claim key {claim['key']}")
            claim_keys.add(claim["key"])

        states = record.get("states", {})
        if (
            states.get("installation") == "owner-reported"
            and states.get("identity") in {"unknown", "conflicting", "suspected-missing"}
            and not record.get("question_ids")
        ):
            errors.append(f"{record_id}: installed item with unresolved identity needs a question")

    for question in questions_us002:
        for source_id in question.get("source_ids", []):
            if source_id not in source_ids:
                errors.append(f"{question['id']}: unknown source reference {source_id}")

    source_hash_owners: dict[str, list[str]] = {}
    for source in sources:
        for component_id in source.get("component_ids", []):
            if component_id not in component_ids:
                errors.append(f"{source['id']}: unknown component reference {component_id}")
        if source["kind"] in {"vendor-manual", "vendor-web-page"}:
            if not source.get("component_ids"):
                errors.append(f"{source['id']}: vendor source needs component_ids")
            if not source["path"].startswith("docs/assets/components/") or "/vendor/" not in source["path"]:
                errors.append(f"{source['id']}: vendor source must live in a component vendor directory")
        path = ROOT / source["path"]
        if not path.is_file():
            errors.append(f"{source['id']}: source path does not exist: {source['path']}")
            continue
        observed = sha256(path)
        if observed != source["sha256"]:
            errors.append(
                f"{source['id']}: sha256 mismatch for {source['path']}; "
                f"expected {source['sha256']}, observed {observed}"
            )
        source_hash_owners.setdefault(observed, []).append(source["id"])
        if path.suffix.lower() == ".pdf":
            with path.open("rb") as stream:
                signature = stream.read(5)
            if signature != b"%PDF-":
                errors.append(f"{source['id']}: PDF source lacks a PDF signature: {source['path']}")

    for digest, owners in source_hash_owners.items():
        if len(owners) > 1:
            errors.append(f"sources: duplicate sha256 {digest} used by {sorted(owners)}")

    validate_component_documentation(components, sources, errors)
    validate_evidence(component_ids, tool_ids, question_ids, errors)


def validate_evidence(
    component_ids: set[str], tool_ids: set[str], question_ids: set[str], errors: list[str]
) -> None:
    schema = load_json(SCHEMAS / "evidence-metadata.schema.json")
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    evidence_ids: set[str] = set()

    for directory in sorted(EVIDENCE.glob("EV-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9]")):
        metadata_path = directory / "metadata.yaml"
        if not metadata_path.is_file():
            errors.append(f"{directory.relative_to(ROOT)}: missing metadata.yaml")
            continue
        metadata = load_yaml(metadata_path)
        for error in validator.iter_errors(metadata):
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            errors.append(f"{metadata_path.relative_to(ROOT)}:{location}: {error.message}")

        evidence_id = metadata.get("id")
        if evidence_id != directory.name:
            errors.append(f"{directory.relative_to(ROOT)}: metadata id must match directory name")
        if evidence_id in evidence_ids:
            errors.append(f"evidence: duplicate id {evidence_id}")
        evidence_ids.add(evidence_id)

        if not (directory / "procedure.md").is_file() or not (directory / "result.md").is_file():
            errors.append(f"{directory.relative_to(ROOT)}: procedure.md and result.md are required")

        links = metadata.get("links", {})
        for component_id in links.get("component_ids", []):
            if component_id not in component_ids:
                errors.append(f"{evidence_id}: unknown component reference {component_id}")
        for question_id in links.get("question_ids", []):
            if question_id not in question_ids:
                errors.append(f"{evidence_id}: unknown question reference {question_id}")
        for tool_id in metadata.get("tools", []):
            if tool_id not in tool_ids:
                errors.append(f"{evidence_id}: unknown tool reference {tool_id}")
        for artifact in metadata.get("artifacts", []):
            artifact_path = directory / artifact["path"]
            if not artifact_path.is_file():
                errors.append(f"{evidence_id}: missing artifact {artifact['path']}")
            elif sha256(artifact_path) != artifact["sha256"]:
                errors.append(f"{evidence_id}: artifact hash mismatch {artifact['path']}")


def render_bom(data: dict[str, dict[str, Any]]) -> str:
    components = data["components"]["components"]
    tools = data["tools"]["tools"]
    rows = []
    for component in components:
        states = component["states"]
        rows.append(
            f"| `{component['id']}` | {component['name']} | {component['category']} | "
            f"{states['identity']} | {states['installation']} | {states['functional']} |"
        )
    tool_rows = [
        f"| `{tool['id']}` | {tool['name']} | {tool['category']} | {tool['availability']} | {tool['condition']} |"
        for tool in tools
    ]
    return "\n".join(
        [
            "# BOM And Parts Status",
            "",
            "This file is generated from `component-registry.yaml` and `tool-registry.yaml`.",
            "Do not edit it directly; update the registries and run",
            "`python3 tools/docs/validate_us002_records.py --write-indexes`.",
            "",
            "States describe evidence strength, not desired target architecture. Follow each",
            "record's questions and claim provenance before relying on a hardware fact.",
            "",
            "## Components",
            "",
            "| ID | Name | Category | Identity | Installation | Functional |",
            "| --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Workshop Tools",
            "",
            "| ID | Name | Category | Availability | Condition |",
            "| --- | --- | --- | --- | --- |",
            *tool_rows,
            "",
        ]
    )


def render_source_index(data: dict[str, dict[str, Any]]) -> str:
    rows = []
    for source in data["sources"]["sources"]:
        retrieval = source.get("retrieval")
        origin = (
            f"[{retrieval['host_type']}]({retrieval['url']}) ({retrieval['retrieved_on']})"
            if retrieval
            else "—"
        )
        rows.append(
            f"| `{source['id']}` | [{source['title']}](../../{source['path']}) | "
            f"{source['kind']} | {source['authority']} | {source['extraction_status']} | {origin} |"
        )
    return "\n".join(
        [
            "# Source Index",
            "",
            "This file is generated from `source-registry.yaml`. Do not edit it directly;",
            "update the registry and run",
            "`python3 tools/docs/validate_us002_records.py --write-indexes`.",
            "",
            "## Repositories",
            "",
            "- [robot-pico-platform](../../robot-pico-platform)",
            "- [robot-esp32-platform](../../robot-esp32-platform)",
            "- [robot-android-app](../../robot-android-app)",
            "",
            "## Registered Sources",
            "",
            "| ID | Source | Kind | Authority | Extraction | Retrieval |",
            "| --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "A registered source is not automatically proof that its claims apply to the",
            "installed robot. Applicability and limitations live in the source registry;",
            "physical qualification lives in evidence bundles.",
            "",
        ]
    )


def render_component_catalog(data: dict[str, dict[str, Any]]) -> str:
    components = data["components"]["components"]
    sources = data["sources"]["sources"]
    source_counts: dict[str, int] = {}
    for source in sources:
        for component_id in source.get("component_ids", []):
            source_counts[component_id] = source_counts.get(component_id, 0) + 1

    requirement_counts = {"required": 0, "conditional": 0, "not-required": 0}
    status_counts = {
        "curated": 0,
        "partial": 0,
        "stub": 0,
        "conditional": 0,
        "missing": 0,
    }
    rows: list[str] = []
    for component in components:
        requirement = component["documentation_requirement"]
        requirement_counts[requirement] += 1
        documentation_value = component.get("documentation")
        metadata: dict[str, Any] = {}
        if documentation_value and (ROOT / documentation_value).is_file():
            try:
                metadata = load_markdown_frontmatter(ROOT / documentation_value)
            except (OSError, ValueError, yaml.YAMLError):
                metadata = {}
        default_status = "conditional" if requirement == "conditional" and not documentation_value else "missing"
        status = metadata.get("documentation_status", default_status)
        if status not in status_counts:
            status = "missing"
        status_counts[status] += 1

        if documentation_value:
            relative = Path(documentation_value).relative_to("docs/assets/components")
            name = f"[{component['name']}]({relative.as_posix()})"
        else:
            name = component["name"]
        coverage = metadata.get("coverage", {})
        applicable = [value for value in coverage.values() if value != "not-applicable"]
        covered = sum(value == "covered" for value in applicable)
        coverage_text = f"{covered}/{len(applicable)}" if applicable else "—"
        questions = ", ".join(f"`{value}`" for value in component.get("question_ids", [])) or "—"
        rows.append(
            f"| `{component['id']}` | {name} | {component['category']} | "
            f"{component['states']['identity']} | {requirement} | {status} | "
            f"{coverage_text} | {source_counts.get(component['id'], 0)} | {questions} |"
        )

    return "\n".join(
        [
            "# Component Documentation Catalog",
            "",
            "This file is generated from the component and source registries plus documentation",
            "front matter. Do not edit it directly; update those records and run",
            "`python3 tools/docs/validate_us002_records.py --write-indexes`.",
            "",
            "Read the component documentation first, then its registry state and unresolved",
            "questions. Open cited source pages next and the complete vendor source only",
            "when the documentation is insufficient.",
            "",
            "## Coverage Summary",
            "",
            f"- Registered components: {len(components)}",
            f"- Documentation requirement: {requirement_counts['required']} required, "
            f"{requirement_counts['conditional']} conditional, {requirement_counts['not-required']} not required",
            f"- Documentation: {status_counts['curated']} curated, {status_counts['partial']} partial, "
            f"{status_counts['stub']} stub, {status_counts['missing']} missing required",
            f"- Conditional registry records without documentation: {status_counts['conditional']}",
            "",
            "Coverage reports documented decision areas, not physical qualification.",
            "",
            "## Components",
            "",
            "| ID | Component | Category | Identity | Requirement | Documentation | Coverage | Sources | Open questions |",
            "| --- | --- | --- | --- | --- | --- | --- | ---: | --- |",
            *rows,
            "",
        ]
    )


def check_or_write_indexes(data: dict[str, dict[str, Any]], write: bool, errors: list[str]) -> None:
    expected = {
        REFERENCE / "bom-and-parts-status.md": render_bom(data),
        REFERENCE / "source-index.md": render_source_index(data),
        COMPONENT_PACKS / "README.md": render_component_catalog(data),
    }
    for path, content in expected.items():
        if write:
            path.write_text(content, encoding="utf-8")
        elif not path.is_file() or path.read_text(encoding="utf-8") != content:
            errors.append(f"{path.relative_to(ROOT)}: generated index is stale; run with --write-indexes")


def check_append_only(base_ref: str, errors: list[str]) -> None:
    command = ["git", "diff", "--name-status", base_ref, "--", "docs/verification/evidence"]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        errors.append(f"append-only check failed: {result.stderr.strip()}")
        return
    for line in result.stdout.splitlines():
        status, *paths = line.split("\t")
        if status.startswith(("M", "D", "R")) and any("/EV-" in path for path in paths):
            errors.append(f"append-only violation: {line}")


def validate_markdown_links(errors: list[str]) -> None:
    """Check local links in the canonical parent documentation tree."""
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for markdown in sorted((ROOT / "docs").rglob("*.md")):
        text = markdown.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for raw_target in pattern.findall(text):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (markdown.parent / target).resolve()
            if not resolved.exists():
                errors.append(
                    f"{markdown.relative_to(ROOT)}: broken local link {raw_target}"
                )


def validate_physical_procedures(
    errors: list[str], procedures: Path | None = None
) -> None:
    """Require the physical-procedure contract and its safety-critical order."""
    procedures = procedures or PROCEDURES
    for path in sorted(procedures.glob("US*-PROC-*.md")):
        text = path.read_text(encoding="utf-8")
        positions: list[int] = []
        for heading in REQUIRED_PROCEDURE_HEADINGS:
            match = re.search(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE)
            if match is None:
                errors.append(f"{path.relative_to(ROOT)}: missing procedure heading {heading}")
                continue
            positions.append(match.start())
        if len(positions) == len(REQUIRED_PROCEDURE_HEADINGS) and positions != sorted(positions):
            errors.append(f"{path.relative_to(ROOT)}: procedure headings are out of contract order")

        if path.name == "US002-PROC-001-unpowered-identity.md":
            safe_setup = re.search(
                r"^## Safe setup\s*$\n(.*?)(?=^## )", text, re.MULTILINE | re.DOTALL
            )
            safe_text = safe_setup.group(1).lower() if safe_setup else ""
            if "unknown" not in safe_text or "isolation" not in safe_text or "inaccessible" not in safe_text:
                errors.append(
                    f"{path.relative_to(ROOT)}: safe setup must make unknown isolation inaccessible"
                )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-indexes", action="store_true", help="regenerate human-readable registry indexes")
    parser.add_argument("--base-ref", help="reject modified/deleted evidence bundles relative to this Git ref")
    args = parser.parse_args()

    errors: list[str] = []
    data: dict[str, dict[str, Any]] = {}
    for name, (registry_path, schema_path) in REGISTRIES.items():
        try:
            data[name] = load_yaml(registry_path)
            validate_schema(name, data[name], schema_path, errors)
        except (OSError, ValueError, yaml.YAMLError, json.JSONDecodeError) as exc:
            errors.append(f"{name}: {exc}")

    for name, (record_path, schema_path) in ADDITIONAL_RECORDS.items():
        try:
            validate_schema(name, load_yaml(record_path), schema_path, errors)
        except (OSError, ValueError, yaml.YAMLError, json.JSONDecodeError) as exc:
            errors.append(f"{name}: {exc}")

    if len(data) == len(REGISTRIES):
        validate_references(data, errors)
        check_or_write_indexes(data, args.write_indexes, errors)
        validate_markdown_links(errors)
        validate_physical_procedures(errors)
    if args.base_ref:
        check_append_only(args.base_ref, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"US-002 validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(
        "US-002 records valid: "
        f"{len(data['components']['components'])} components, "
        f"{len(data['tools']['tools'])} tools, "
        f"{len(data['sources']['sources'])} sources, "
        f"{len(data['questions_us002']['questions']) + len(data['questions_us003']['questions'])} questions."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
