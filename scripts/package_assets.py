"""Package supplemental www files; HACS manages the theme YAMLs separately."""
import argparse
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "yourname_uix-assets.zip")
    args = parser.parse_args()
    with ZipFile(args.output, "w", ZIP_DEFLATED) as archive:
        for source in sorted((ROOT / "www").rglob("*")):
            if source.is_file():
                archive.write(source, source.relative_to(ROOT).as_posix())
    print(args.output)
