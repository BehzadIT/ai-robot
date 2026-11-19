from __future__ import annotations

import json
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))

from robotlib import core
import yaml


class CoreContractTest(unittest.TestCase):
    def test_redacts_secret_and_home(self) -> None:
        value = core.redact(f"password=bad {Path.home()}/private")
        self.assertNotIn("bad", value)
        self.assertNotIn(str(Path.home()), value)

    def test_local_config_rejects_unknown_keys(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "local.yaml"
            path.write_text("schema_version: 1\nunknown: true\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                core.load_local_config(path)

    def test_local_config_rejects_placeholder_device(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "local.yaml"
            path.write_text(
                "schema_version: 1\ndevice_aliases:\n  pico:\n    kind: pico\n    usb_serial: replace-me\n",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                core.load_local_config(path)

    def test_result_contract_validates(self) -> None:
        payload = core.result("test")
        payload["checks"].append(core.check("contract", "pass", "valid", "valid"))
        core.finish(payload)
        core.validate_result(payload)

    def test_exit_code_families(self) -> None:
        payload = core.result("test")
        payload["outcome"] = "blocked"
        payload["checks"] = [core.check("device", "blocked", "present", "absent", category="device_absent")]
        self.assertEqual(core.exit_code(payload), 21)

    def test_gate_three_records_each_confirmation(self) -> None:
        with mock.patch.object(sys.stdin, "isatty", return_value=True), mock.patch(
            "builtins.input", side_effect=["y", "y", "y", "y", "y"]
        ):
            approvals = core.request_approval(3, "pico", "STOP-001", "pico_control", "safe stop")
        self.assertEqual(len(approvals), 5)

    def test_platform_descriptions_use_protocol_one(self) -> None:
        for name in ("android", "esp32", "pico"):
            payload = core.describe(name)
            self.assertEqual(payload["environment"]["adapter_protocol"], 1)
            self.assertTrue(payload["environment"]["scenarios"])

    def test_integration_scenarios_have_adapter_actions(self) -> None:
        registry = yaml.safe_load((core.ROOT / "docs" / "reference" / "scenario-registry.yaml").read_text(encoding="utf-8"))
        descriptions = {name: core.describe(name)["environment"]["scenarios"] for name in ("android", "esp32", "pico")}
        for scenario in registry["scenarios"]:
            platform = "pico" if scenario["target"].startswith("pico-") else scenario["target"]
            actions = {entry["id"]: entry for entry in descriptions[platform]}
            self.assertIn(scenario["adapter_action"], actions)
            self.assertEqual(actions[scenario["adapter_action"]]["gate"], scenario["gate"])


if __name__ == "__main__":
    unittest.main()
