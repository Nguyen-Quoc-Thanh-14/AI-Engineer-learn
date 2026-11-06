"""J07.01 real CPython 3.15 feature checks; one test per requested feature."""
from __future__ import annotations
import subprocess
import sys
import unittest

class WhatsNew315Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if sys.version_info[:3] != (3,15,2):
            raise RuntimeError("Requires exact CPython 3.15.2; never mark SKIP as PASS")

    def run_py(self, source):
        p=subprocess.run([sys.executable,"-I","-c",source],text=True,
                         capture_output=True,timeout=15)
        self.assertEqual(p.returncode,0,p.stderr[-2500:])
        return p.stdout

    def test_explicit_lazy_import(self):
        self.run_py(
            "import sys\n"
            "lazy import fractions\n"
            "assert 'fractions' not in sys.modules\n"
            "assert fractions.Fraction(1, 2).numerator == 1\n"
            "assert 'fractions' in sys.modules\n"
        )

    def test_frozendict_is_immutable(self):
        self.run_py(
            "from builtins import frozendict\n"
            "f = frozendict({'k': 42})\n"
            "assert f['k'] == 42\n"
            "try: f['k']=99\n"
            "except TypeError: pass\n"
            "else: raise AssertionError('frozendict mutated')\n"
        )

    def test_sentinel_identity(self):
        self.run_py(
            "from builtins import sentinel\n"
            "NOT_SET = sentinel('NOT_SET')\n"
            "assert NOT_SET is NOT_SET\n"
            "assert NOT_SET is not None\n"
        )

if __name__=="__main__":
    unittest.main()
