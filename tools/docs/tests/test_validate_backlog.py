import importlib.util,json,tempfile,unittest
from pathlib import Path
import jsonschema
SPEC=importlib.util.spec_from_file_location("validate_backlog",Path(__file__).parents[1]/"validate_backlog.py")
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class BacklogValidationTests(unittest.TestCase):
 def test_live_dossiers_validate(self): self.assertEqual([],v.validate())
 def test_discovers_directory_readmes(self): self.assertEqual(6,len(list(v.ITEMS.glob("US-*/README.md"))))
 def test_parse_frontmatter(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/"README.md";p.write_text("---\nid: US-999\n---\n# body\n")
   self.assertEqual("US-999",v.parse(p)[0]["id"])
 def test_task_cycle(self): self.assertEqual(["T001","T002","T001"],v.find_cycle({"T001":["T002"],"T002":["T001"]}))
 def test_marker_replacement_preserves_surroundings(self):
  text=f"before\n{v.BEGIN}\nold\n{v.END}\nafter\n";out=v.replace(text,"new")
  self.assertTrue(out.startswith("before"));self.assertTrue(out.endswith("after\n"));self.assertIn("new",out)
 def test_plan_schema_rejects_incomplete_tdd(self):
  schema=json.loads(v.PS.read_text());task={"id":"T001","title":"x","status":"planned","depends_on":[],"parallel_safe":False,"repositories":["parent"],"subsystems":["docs"],"acceptance":["AC-001"],"test_mode":"tdd","evidence_levels":["host"],"test_support":[]}
  with self.assertRaises(jsonschema.ValidationError):jsonschema.validate({"story_id":"US-999","plan_version":1,"updated":"2026-11-19","tasks":[task]},schema)
 def test_plan_schema_accepts_static_task(self):
  schema=json.loads(v.PS.read_text());task={"id":"T001","title":"x","status":"done","depends_on":[],"parallel_safe":False,"repositories":["parent"],"subsystems":["docs"],"acceptance":["AC-001"],"test_mode":"static-only","evidence_levels":["static"],"test_support":[],"static_check":{"method":"review"}}
  jsonschema.validate({"story_id":"US-999","plan_version":1,"updated":"2026-11-19","tasks":[task]},schema)
 def test_diagram_pairs_exist(self):
  for src in v.BACKLOG.glob("**/diagrams/*.mmd"):self.assertTrue(src.with_suffix(".svg").is_file())
if __name__=="__main__":unittest.main()
