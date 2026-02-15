# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
Tests for mini_svg advanced level.
"""

from mini_svg import minisvg_advanced as adv


def test_bezier_path_cubic_outputs_path_tag():
	start = (0, 0)
	segments = [
		(10, 0, 10, 10, 20, 20),
		(30, 30, 40, 40, 50, 50),
	]
	s = adv.bezier_path_cubic(start, segments)
	assert s.strip().startswith("<path")
	assert 'd="M ' in s
	assert " C " in s


def test_bezier_path_cubic_closed_adds_Z():
	start = (0, 0)
	segments = [(10, 0, 10, 10, 20, 20)]
	s = adv.bezier_path_cubic(start, segments, closed=True)
	assert "Z" in s

