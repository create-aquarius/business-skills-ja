"""Distribution checks, not a test of an LLM's interpretation of the skills."""

import importlib.util
from pathlib import Path
import re
import tempfile
import unittest
from urllib.parse import unquote
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("packager", ROOT / "tools/package_review_skills.py")
PACKAGER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACKAGER)


class ReviewSkillReleaseTests(unittest.TestCase):
    def test_shipped_archives_match_only_allowlisted_sources(self):
        for name in PACKAGER.NAMES:
            with self.subTest(name=name):
                PACKAGER.check(ROOT / "downloads" / f"{name}.zip", PACKAGER.expected_members(name))

    def test_checker_rejects_an_extra_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "extra.zip"
            with ZipFile(path, "w") as archive:
                archive.writestr("skill/SKILL.md", b"example")
                archive.writestr("unintended.txt", b"unexpected")
            with self.assertRaises(ValueError):
                PACKAGER.check(path, {"skill/SKILL.md": b"example"})

    def test_checker_rejects_stale_content(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stale.zip"
            with ZipFile(path, "w") as archive:
                archive.writestr("skill/SKILL.md", b"old")
            with self.assertRaises(ValueError):
                PACKAGER.check(path, {"skill/SKILL.md": b"new"})

    def test_relative_markdown_links_resolve(self):
        pages = [ROOT / "README.md", ROOT / "README.ja.md", ROOT / "docs/two-review-skills.md"]
        pages += list((ROOT / "docs/examples").glob("*.md"))
        pages += list((ROOT / "docs/evals").glob("*.md"))
        for page in pages:
            for target in re.findall(r"\]\(([^)]+)\)", page.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                with self.subTest(page=page.name, target=target):
                    self.assertTrue((page.parent / unquote(target.split("#")[0])).exists())

    def test_two_skills_are_self_contained_and_named(self):
        for name in PACKAGER.NAMES:
            directory = ROOT / "skills" / name
            self.assertEqual([p.name for p in directory.iterdir()], ["SKILL.md"])
            content = (directory / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(f"name: {name}\n", content)
            self.assertNotIn("C:\\Users\\", content)


if __name__ == "__main__":
    unittest.main()
