# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
tests/test_intermediate.py

Tests for intermediate-level API.
"""

from __future__ import annotations

import mini_svg as minisvg


def test_text_uses_default_font_size_and_opacity() -> None:
	minisvg.set_style(font_size=21, opacity=0.6)

	out = minisvg.text(10, 20, "Hello")

	assert "<text" in out
	assert 'font-size="21"' in out
	assert 'opacity="0.6"' in out


def test_regular_polygon_default_rotation_matches_explicit_rotation() -> None:
	bbox = (0.0, 0.0, 100.0, 100.0)

	minisvg.set_style(rotation_deg=33)

	a = minisvg.regular_polygon(6, bbox)
	b = minisvg.regular_polygon(6, bbox, rotation_deg=33)

	assert a == b


def test_star_default_rotation_matches_explicit_rotation() -> None:
	bbox = (10.0, 10.0, 80.0, 80.0)

	minisvg.set_style(rotation_deg=12)

	a = minisvg.star(5, bbox)
	b = minisvg.star(5, bbox, rotation_deg=12)

	assert a == b


def test_group_wraps_elements() -> None:
	minisvg.set_style(opacity=0.5)

	els = [minisvg.circle(10, 10, 3), minisvg.circle(20, 10, 3)]
	g = minisvg.group(els, transform="translate(5 0)")

	assert g.startswith("<g")
	assert 'transform="translate(5 0)"' in g
	assert 'opacity="0.5"' in g
	assert g.strip().endswith("</g>")
	assert g.count("<circle") == 2


def test_cubic_bezier_is_path() -> None:
	minisvg.set_style(stroke=minisvg.COLORS.BLACK, stroke_width=2, fill=minisvg.COLORS.TRANSPARENT, opacity=1.0)

	out = minisvg.cubic_bezier(0, 0, 10, 0, 10, 10, 20, 10)

	assert out.startswith('<path d="M ')
	assert " C " in out
	assert 'stroke-width="2"' in out

