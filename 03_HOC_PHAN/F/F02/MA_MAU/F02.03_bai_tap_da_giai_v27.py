# coding: utf-8
# Bài B F02.03: thực sự ghi file TOML rồi đọc lại từ đĩa.
from pathlib import Path
from tempfile import TemporaryDirectory
import tomllib

PROJECT_TOML = '''[project]
name = "my-demo"
version = "0.1.0"
[project.optional-dependencies]
dev = ["pytest>=8", "ruff>=0.9"]
'''

def write_and_read_project(path: Path) -> dict:
    path.write_text(PROJECT_TOML, encoding="utf-8")
    with path.open("rb") as stream:
        return tomllib.load(stream)

if __name__ == "__main__":
    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "pyproject.toml"
        config = write_and_read_project(path)
        assert path.is_file()
        assert config["project"]["name"] == "my-demo"
        assert "pytest>=8" in config["project"]["optional-dependencies"]["dev"]
        assert len(config["project"]["optional-dependencies"]["dev"]) == 2
    print("PASS F02.03")
