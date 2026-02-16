# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
#
"""
Replace __DOCS_VERSION__ in pyproject.toml with a concrete version.
"""

from __future__ import annotations
import sys
from pathlib import Path


def main() -> int:
	if len(sys.argv) != 2:
		print("Usage: inject_docs_version.py <version>", file=sys.stderr)
		return 2

	version = sys.argv[1].strip()
	if not version:
		print("ERROR: empty version", file=sys.stderr)
		return 2

	path = Path("pyproject.toml")
	text = path.read_text(encoding="utf-8")

	if "__DOCS_VERSION__" not in text:
		print("ERROR: placeholder not found", file=sys.stderr)
		return 1

	text = text.replace("__DOCS_VERSION__", version)
	path.write_text(text, encoding="utf-8")

	print(f"Injected docs version: {version}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())

