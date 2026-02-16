# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
"""
Replace __DOCS_VERSION__ in pyproject.toml with a concrete version.

Usage:
  python scripts/inject_docs_version.py 1.2.3
"""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
	if len(sys.argv) != 2:
		print("Usage: python scripts/inject_docs_version.py <version>", file=sys.stderr)
		return 2

	version = sys.argv[1].strip()
	if not version:
		print("ERROR: empty version", file=sys.stderr)
		return 2

	path = Path("pyproject.toml")
	if not path.exists():
		print("ERROR: pyproject.toml not found", file=sys.stderr)
		return 2

	text = path.read_text(encoding="utf-8")
	if "__DOCS_VERSION__" not in text:
		print("ERROR: placeholder __DOCS_VERSION__ not found in pyproject.toml", file=sys.stderr)
		return 1

	path.write_text(text.replace("__DOCS_VERSION__", version), encoding="utf-8")
	print(f"Injected docs version: {version}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())

