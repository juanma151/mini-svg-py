# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
Public API tests for mini_svg.

The package root exports:
- a flat API (functions re-exported from the advanced level)
- explicit level modules: minisvg_basic, minisvg_intermediate, minisvg_advanced
"""

import mini_svg as minisvg


def test_level_modules_exist():
	assert hasattr(minisvg, "minisvg_basic")
	assert hasattr(minisvg, "minisvg_intermediate")
	assert hasattr(minisvg, "minisvg_advanced")


def test_flat_api_exposes_common_functions():
	for name in (
		"svg_begin",
		"svg_end",
		"save_svg",
		"circle",
		"rect",
		"line",
		"star",
		"regular_polygon",
	):
		assert hasattr(minisvg, name), f"missing symbol in flat API: {name}"

