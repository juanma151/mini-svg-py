# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
tests/test_public_api.py

Sanity checks for the flat public API and the progressive level modules.
"""

from __future__ import annotations

import mini_svg as minisvg


def test_flat_api_exposes_levels() -> None:
	assert hasattr(minisvg, "minisvg_basic")
	assert hasattr(minisvg, "minisvg_intermediate")
	assert hasattr(minisvg, "minisvg_advanced")


def test_flat_api_exposes_style_utilities() -> None:
	assert hasattr(minisvg, "COLORS")
	assert hasattr(minisvg, "PALETTES")
	assert hasattr(minisvg, "set_style")
	assert hasattr(minisvg, "palette_pick")


def test_level_imports_work() -> None:
	from mini_svg import minisvg_basic
	from mini_svg import minisvg_intermediate
	from mini_svg import minisvg_advanced

	assert hasattr(minisvg_basic, "circle")
	assert hasattr(minisvg_intermediate, "regular_polygon")
	assert hasattr(minisvg_advanced, "bezier_path_cubic")

