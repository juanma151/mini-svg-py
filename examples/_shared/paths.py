# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
examples/_shared/paths.py

Shared helpers for example scripts.

This file is not part of the mini_svg library. It only exists to keep the
examples clean and consistent.
"""

from __future__ import annotations

from pathlib import Path


def project_root_from_here() -> Path:
	"""
	Return the project root assuming this file is located at:

	<root>/examples/_shared/paths.py
	"""
	return Path(__file__).resolve().parents[2]


def generated_dir() -> Path:
	"""Return <root>/examples/generated_svgs and create it if missing."""
	out = project_root_from_here() / "examples" / "generated_svgs"
	out.mkdir(parents=True, exist_ok=True)
	return out


def out_path_for_script(script_file: str) -> Path:
	"""
	Compute output svg path from a script filename.

	The SVG will be created under examples/generated_svgs/ and will share the same
	stem name as the script.

	Example
	-------
	If script is "02_01_polygons_and_stars.py", output is:
	"examples/generated_svgs/02_01_polygons_and_stars.svg"
	"""
	name = Path(script_file).name
	stem = Path(name).with_suffix("").name
	return generated_dir() / f"{stem}.svg"

