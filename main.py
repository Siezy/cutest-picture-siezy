"""Cutest picture entry: copy the bundled picture to the output directory.

The picture is entry.png beside this file. Per the competition rules the
file is a JPEG told apart by its first bytes, and the name stays entry.png.
The copy is byte-for-byte deterministic: the program runs twice and both
runs write the same bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = HERE / "entry.png"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    # Fail loudly on a truncated write instead of shipping a broken picture.
    if dst.stat().st_size != src.stat().st_size:
        raise RuntimeError("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
