# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
tests/test_style.py

Tests for the public style API: mini_svg.style (also re-exported via mini_svg).
"""

from __future__ import annotations

import pytest
import mini_svg as minisvg


def test_colors_are_immutable() -> None:
	with pytest.raises(AttributeError):
		minisvg.COLORS.YELLOW = "#000000"  # type: ignore[attr-defined]


def test_palettes_are_immutable() -> None:
	with pytest.raises(AttributeError):
		minisvg.PALETTES.WARHOL = ("#000000",)  # type: ignore[attr-defined]


def test_palette_pick_wraps() -> None:
	p = minisvg.PALETTES.WARHOL
	assert minisvg.palette_pick(p, 0) == p[0]
	assert minisvg.palette_pick(p, len(p)) == p[0]
	assert minisvg.palette_pick(p, len(p) + 1) == p[1]


def test_set_style_and_get_style_roundtrip() -> None:
	minisvg.set_style(stroke=minisvg.COLORS.DARK_GRAY, stroke_width=3, opacity=0.5)
	assert minisvg.get_style("stroke") == minisvg.COLORS.DARK_GRAY
	assert minisvg.get_style("stroke_width") == 3
	assert minisvg.get_style("opacity") == 0.5

	with pytest.raises(KeyError):
		minisvg.get_style("does_not_exist")

