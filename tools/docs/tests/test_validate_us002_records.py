from __future__ import annotations

import importlib.util
import copy
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

import jsonschema


SCRIPT = Path(__file__).resolve().parents[1] / "validate_us002_records.py"
SPEC = importlib.util.spec_from_file_location("validate_us002_records", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RegistryContractTest(unittest.TestCase):
    def test_repository_records_are_valid(self) -> None:
        self.assertEqual(MODULE.main_for_test(), 0) if hasattr(MODULE, "main_for_test") else None
        errors: list[str] = []
        data = {}
        for name, (registry, schema) in MODULE.REGISTRIES.items():
            data[name] = MODULE.load_yaml(registry)
            MODULE.validate_schema(name, data[name], schema, errors)
        MODULE.validate_references(data, errors)
        self.assertEqual(errors, [])

    def test_component_schema_rejects_collapsed_state(self) -> None:
        schema = MODULE.load_json(MODULE.SCHEMAS / "component-registry.schema.json")
        invalid = {
            "schema_version": 1,
            "components": [
                {
                    "id": "component-example-01",
                    "name": "Example",
                    "category": "controller",
                    "manufacturer": None,
                    "model": None,
                    "variant": None,
                    "quantity": 1,
                    "states": {"identity": "unknown"},
                    "system_role": "test",
                    "owner_subsystem": "pico",
                    "claims": [],
                    "question_ids": [],
                }
            ],
        }
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(invalid, schema)

    def test_claim_requires_provenance(self) -> None:
        schema = MODULE.load_json(MODULE.SCHEMAS / "component-registry.schema.json")
        registry = MODULE.load_yaml(MODULE.REFERENCE / "component-registry.yaml")
        invalid = {"schema_version": 1, "components": [copy.deepcopy(registry["components"][0])]}
        invalid["components"][0]["claims"][0].pop("provenance")
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(invalid, schema)

    def test_source_schema_rejects_unknown_retrieval_host_type(self) -> None:
        schema = MODULE.load_json(MODULE.SCHEMAS / "source-registry.schema.json")
        registry = MODULE.load_yaml(MODULE.REFERENCE / "source-registry.yaml")
        source = copy.deepcopy(next(item for item in registry["sources"] if item.get("retrieval")))
        source["retrieval"]["host_type"] = "unclassified-mirror"
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate({"schema_version": 1, "sources": [source]}, schema)

    def test_component_schema_requires_documentation_classification(self) -> None:
        schema = MODULE.load_json(MODULE.SCHEMAS / "component-registry.schema.json")
        registry = MODULE.load_yaml(MODULE.REFERENCE / "component-registry.yaml")
        component = copy.deepcopy(registry["components"][0])
        component.pop("documentation_requirement")
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate({"schema_version": 1, "components": [component]}, schema)

    def test_component_schema_rejects_duplicate_assembly_members(self) -> None:
        schema = MODULE.load_json(MODULE.SCHEMAS / "component-registry.schema.json")
        registry = MODULE.load_yaml(MODULE.REFERENCE / "component-registry.yaml")
        component = copy.deepcopy(registry["components"][0])
        component["member_component_ids"] = ["component-example-01", "component-example-01"]
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate({"schema_version": 1, "components": [component]}, schema)

    def test_registry_rejects_assembly_cycle(self) -> None:
        data = {
            name: MODULE.load_yaml(registry)
            for name, (registry, _schema) in MODULE.REGISTRIES.items()
        }
        data = copy.deepcopy(data)
        first, second = data["components"]["components"][:2]
        first["member_component_ids"] = [second["id"]]
        second["member_component_ids"] = [first["id"]]
        errors: list[str] = []
        MODULE.validate_references(data, errors)
        self.assertTrue(any("assembly cycle" in error for error in errors), errors)

    def test_dossier_rejects_stale_reviewed_source_hash(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            documentation = root / "docs/assets/components/controllers/example/README.md"
            documentation.parent.mkdir(parents=True)
            documentation.write_text(
                textwrap.dedent(
                    """\
                    ---
                    component_id: component-example-01
                    documentation_status: partial
                    reviewed_on: "2026-11-19"
                    reviewed_sources:
                      - id: source-example
                        sha256: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                    coverage:
                      identity_and_applicability: partial
                      safety_and_limits: pending
                      power_and_electrical: pending
                      interfaces_and_timing: pending
                      configuration_and_calibration: pending
                      mechanical_and_environmental: pending
                      diagnostics_and_failure_modes: pending
                      replacement_and_compatibility: pending
                    ---
                    # Example
                    """
                ),
                encoding="utf-8",
            )
            components = [{
                "id": "component-example-01",
                "documentation_requirement": "required",
                "documentation": "docs/assets/components/controllers/example/README.md",
            }]
            sources = [{
                "id": "source-example",
                "kind": "vendor-manual",
                "path": "docs/assets/components/controllers/example/vendor/example.pdf",
                "sha256": "b" * 64,
                "component_ids": ["component-example-01"],
            }]
            old_root = MODULE.ROOT
            MODULE.ROOT = root
            try:
                errors: list[str] = []
                MODULE.validate_component_documentation(components, sources, errors)
            finally:
                MODULE.ROOT = old_root
            self.assertTrue(any("hash is stale" in error for error in errors), errors)

    def test_dossier_rejects_mismatched_pdf_page_locator(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            documentation = root / "docs/assets/components/controllers/example/README.md"
            documentation.parent.mkdir(parents=True)
            documentation.write_text(
                textwrap.dedent(
                    """\
                    ---
                    component_id: component-example-01
                    documentation_status: partial
                    reviewed_on: null
                    reviewed_sources: []
                    coverage:
                      identity_and_applicability: partial
                      safety_and_limits: pending
                      power_and_electrical: pending
                      interfaces_and_timing: pending
                      configuration_and_calibration: pending
                      mechanical_and_environmental: pending
                      diagnostics_and_failure_modes: pending
                      replacement_and_compatibility: pending
                    ---
                    # Example

                    [source-example, PDF p. 4, §Limits](vendor/example.pdf#page=5)
                    """
                ),
                encoding="utf-8",
            )
            components = [{
                "id": "component-example-01",
                "documentation_requirement": "required",
                "documentation": "docs/assets/components/controllers/example/README.md",
            }]
            sources = [{
                "id": "source-example",
                "kind": "vendor-manual",
                "path": "docs/assets/components/controllers/example/vendor/example.pdf",
                "sha256": "b" * 64,
                "component_ids": ["component-example-01"],
            }]
            old_root = MODULE.ROOT
            MODULE.ROOT = root
            try:
                errors: list[str] = []
                MODULE.validate_component_documentation(components, sources, errors)
            finally:
                MODULE.ROOT = old_root
            self.assertTrue(any("page label and fragment differ" in error for error in errors), errors)

    def test_procedure_contract_rejects_missing_heading(self) -> None:
        with tempfile.TemporaryDirectory(dir=MODULE.ROOT / "temp") as directory:
            procedures = Path(directory)
            procedure = procedures / "US999-PROC-001-example.md"
            headings = [
                heading
                for heading in MODULE.REQUIRED_PROCEDURE_HEADINGS
                if heading != "Stop conditions"
            ]
            procedure.write_text(
                "# Example\n\n" + "\n\n".join(f"## {heading}\n\nText." for heading in headings),
                encoding="utf-8",
            )
            errors: list[str] = []
            MODULE.validate_physical_procedures(errors, procedures)
            self.assertTrue(any("missing procedure heading Stop conditions" in error for error in errors), errors)

    def test_identity_procedure_requires_unknown_isolation_block(self) -> None:
        with tempfile.TemporaryDirectory(dir=MODULE.ROOT / "temp") as directory:
            procedures = Path(directory)
            procedure = procedures / "US002-PROC-001-unpowered-identity.md"
            procedure.write_text(
                "# Example\n\n"
                + "\n\n".join(
                    f"## {heading}\n\nRobot off."
                    for heading in MODULE.REQUIRED_PROCEDURE_HEADINGS
                ),
                encoding="utf-8",
            )
            errors: list[str] = []
            MODULE.validate_physical_procedures(errors, procedures)
            self.assertTrue(any("unknown isolation inaccessible" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
