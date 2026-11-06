"""PA03.03: verify a real pyproject console-script and clean wheel installation."""
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import tomllib
import unittest
import venv
import zipfile

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "03_HOC_PHAN/PA/PA03/LAB_CLI"

class PA0303PackagingTests(unittest.TestCase):
    def test_project_metadata_entry_point_is_present(self):
        with (LAB/"pyproject.toml").open("rb") as f:
            cfg=tomllib.load(f)
        self.assertEqual(cfg["project"]["scripts"]["clean-orders"],"orders.cli:main")
        self.assertTrue((LAB/"src/orders/cli.py").is_file())
        self.assertEqual(cfg["project"]["name"],"course-orders-cli-issue9")

    def test_bad_or_missing_input_fails_without_writing(self):
        with TemporaryDirectory() as temp:
            missing=Path(temp)/"missing.csv"
            env=dict(os.environ, PYTHONPATH=str(LAB/"src"))
            cmd=[sys.executable,"-m","orders.cli","--input",str(missing),"--dry-run"]
            p=subprocess.run(cmd,capture_output=True,text=True,env=env)
            self.assertNotEqual(p.returncode,0)
            self.assertFalse(missing.exists())
            cmd.remove("--dry-run")
            p=subprocess.run(cmd,capture_output=True,text=True,env=env)
            self.assertNotEqual(p.returncode,0)

    def test_build_and_install_console_script_from_actual_wheel(self):
        with TemporaryDirectory(prefix="pa0303_") as tmp:
            dest=Path(tmp)
            built=subprocess.run([sys.executable,"-m","pip","wheel","--no-deps",
                                  "--no-build-isolation","--wheel-dir",str(dest),str(LAB)],
                                 text=True,capture_output=True,timeout=150)
            self.assertEqual(built.returncode,0,built.stderr[-2000:])
            wheels=list(dest.glob("course_orders_cli_issue9-*.whl"))
            self.assertEqual(len(wheels),1)
            with zipfile.ZipFile(wheels[0]) as wheel:
                scripts=[n for n in wheel.namelist() if n.endswith(".dist-info/entry_points.txt")]
                self.assertEqual(len(scripts),1)
                self.assertIn("clean-orders = orders.cli:main",wheel.read(scripts[0]).decode("utf8"))
            envdir=dest/"venv"
            venv.EnvBuilder(with_pip=True).create(envdir)
            python=envdir/("Scripts/python.exe" if os.name=="nt" else "bin/python")
            installed=subprocess.run([str(python),"-m","pip","install","--no-index","--no-deps",str(wheels[0])],
                                     capture_output=True,text=True,timeout=100)
            self.assertEqual(installed.returncode,0,installed.stderr[-1800:])
            sample=dest/"orders.csv"
            sample.write_text("order_id,quantity\\n1,2\\n2,3\\n".replace("\\n",chr(10)),encoding="utf8")
            executable=envdir/("Scripts/clean-orders.exe" if os.name=="nt" else "bin/clean-orders")
            tested=subprocess.run([str(executable),"--input",str(sample),"--dry-run"],
                                  capture_output=True,text=True,timeout=30)
            self.assertEqual(tested.returncode,0,tested.stderr)
            self.assertIn("DRY_RUN 2 orders",tested.stdout)

if __name__ == "__main__":
    unittest.main()
