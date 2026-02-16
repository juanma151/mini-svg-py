# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
tests/test_advanced.py

Tests for advanced-level API.
"""

from __future__ import annotations

import mini_svg as minisvg


def test_bezier_path_cubic_builds_multi_segment_path() -> None:
	minisvg.set_style(stroke=minisvg.COLORS.DARK_GRAY, stroke_width=3, fill=minisvg.COLORS.TRANSPARENT, opacity=0.9)

	out = minisvg.bezier_path_cubic(
		(0, 0),
		[
			(10, 0, 10, 10, 20, 10),
			(30, 10, 30, 20, 40, 20),
		],
	)

	assert out.startswith('<path d="M ')
	assert out.count(" C ") == 2
	assert 'stroke="#444444"' in out
	assert 'stroke-width="3"' in out
	assert 'opacity="0.9"' in out

