from __future__ import annotations

import importlib.util
import copy
import sys
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


if __name__ == "__main__":
    unittest.main()
