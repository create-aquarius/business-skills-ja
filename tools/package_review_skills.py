"""Build/check the two review-skill ZIPs from an explicit, small file allowlist."""

import argparse
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("lp-claim-audit", "feedback-to-repro")


def expected_members(name):
    return {
        f"{name}/SKILL.md": (ROOT / "skills" / name / "SKILL.md").read_bytes(),
        f"{name}/LICENSE": (ROOT / "LICENSE").read_bytes(),
    }


def check(path, expected):
    with ZipFile(path) as archive:
        if sorted(archive.namelist()) != sorted(expected):
            raise ValueError(f"Unexpected archive members: {path.name}")
        for member, data in expected.items():
            if archive.read(member) != data:
                raise ValueError(f"Archive content differs from source: {member}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check only; do not rewrite archives")
    args = parser.parse_args()
    for name in NAMES:
        members = expected_members(name)
        path = ROOT / "downloads" / f"{name}.zip"
        if not args.check:
            path.parent.mkdir(exist_ok=True)
            with ZipFile(path, "w", compression=ZIP_DEFLATED) as archive:
                for member, data in members.items():
                    info = ZipInfo(member, date_time=(2026, 9, 17, 0, 0, 0))
                    info.compress_type = ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info, data)
        check(path, members)
        print(f"OK {path.name}: {', '.join(members)}")


if __name__ == "__main__":
    main()
