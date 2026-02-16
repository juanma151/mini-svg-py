# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
tests/test_basic.py

Tests for basic primitives and default-style behavior.
"""

from __future__ import annotations

import mini_svg as minisvg


def test_circle_uses_global_defaults_when_kwargs_none() -> None:
	minisvg.set_style(
		stroke=minisvg.COLORS.HOT_RED,
		fill=minisvg.COLORS.SUNFLOWER,
		stroke_width=4,
		opacity=0.75,
	)

	out = minisvg.circle(10, 20, 5)

	assert '<circle' in out
	assert 'stroke="#ff3b3b"' in out
	assert 'fill="#ffd23f"' in out
	assert 'stroke-width="4"' in out
	assert 'opacity="0.75"' in out


def test_rect_override_beats_default() -> None:
	minisvg.set_style(stroke=minisvg.COLORS.BLACK, fill=minisvg.COLORS.SUNFLOWER, stroke_width=2, opacity=1.0)

	out = minisvg.rect(0, 0, 10, 10, fill=minisvg.COLORS.EMERALD, stroke_width=7)

	assert 'fill="#2ecc71"' in out
	assert 'stroke-width="7"' in out
	assert 'stroke="#000000"' in out


def test_svg_begin_end_and_save(tmp_path) -> None:
	parts = [
		minisvg.svg_begin(100, 100),
		minisvg.circle(50, 50, 10, fill=minisvg.COLORS.BRIGHT_BLUE),
		minisvg.svg_end(),
	]

	p = tmp_path / "out.svg"
	minisvg.save_svg(str(p), parts)

	data = p.read_text(encoding="utf-8")
	assert data.startswith('<?xml version="1.0"')
	assert data.strip().endswith("</svg>")
	assert "<circle" in data

