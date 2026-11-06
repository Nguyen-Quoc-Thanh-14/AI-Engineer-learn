"""N02.02 synthetic direct/transitive dependency graph and negative cases."""
from copy import deepcopy
from pathlib import Path
import json
import runpy
import unittest

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"03_HOC_PHAN/N/N02/MA_MAU/N02.02_bai_B_sbom_audit.py"
SBOM=ROOT/"03_HOC_PHAN/N/N02/MA_MAU/N02.02_bai_B_synthetic_sbom.json"

class N0202SBOMTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tool=runpy.run_path(str(SRC))
        cls.bom=json.loads(SBOM.read_text(encoding="utf8"))
    def test_direct_and_transitive_nodes_are_different(self):
        r=self.tool["validate_graph"](self.bom)
        self.assertEqual(r["direct"],{"pkg:pypi/example-alpha@1.0.0"})
        self.assertEqual(r["transitive"],{"pkg:pypi/example-beta@1.0.0"})
    def test_unknown_dependency_rejected(self):
        fake=deepcopy(self.bom)
        fake["dependencies"][0]["dependsOn"].append("pkg:pypi/not-present@1.0.0")
        with self.assertRaises(ValueError):
            self.tool["validate_graph"](fake)
    def test_cycle_or_duplicate_bom_ref_rejected(self):
        for kind in ("cycle","duplicate"):
            fake=deepcopy(self.bom)
            if kind=="cycle":
                fake["dependencies"][-1]["dependsOn"]=["app:demo-orders"]
            else:
                fake["components"][1]["bom-ref"]=fake["components"][0]["bom-ref"]
            with self.subTest(kind=kind),self.assertRaises(ValueError):
                self.tool["validate_graph"](fake)
    def test_synthetic_advisory_remediation_updates_entire_graph(self):
        old="pkg:pypi/example-beta@1.0.0"
        changed=self.tool["remediation"](self.bom,old,"1.0.1")
        after=self.tool["validate_graph"](changed)
        self.assertNotIn(old,after["all_reachable"])
        self.assertIn("pkg:pypi/example-beta@1.0.1",after["transitive"])
        self.assertIn(old,self.tool["validate_graph"](self.bom)["transitive"])

if __name__=="__main__":
    unittest.main()
