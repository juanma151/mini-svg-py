# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
Tests for mini_svg intermediate level.
"""

from mini_svg import minisvg_intermediate as mid


def test_text_escapes_basic_chars():
	s = mid.text(10, 20, "a<b&c>")
	assert s.strip().startswith("<text")
	assert "&lt;" in s
	assert "&amp;" in s
	assert "&gt;" in s


def test_group_wraps_elements():
	g = mid.group(
		[
			mid.circle(0, 0, 5),
			mid.rect(0, 0, 10, 10),
		],
		transform="rotate(10)",
	)
	assert g.strip().startswith("<g")
	assert 'transform="rotate(10)"' in g
	assert "<circle" in g
	assert "<rect" in g
	assert g.strip().endswith("</g>")


def test_regular_polygon_outputs_polygon_tag():
	s = mid.regular_polygon(5, (0, 0, 100, 100))
	assert s.strip().startswith("<polygon")
	assert 'points="' in s


def test_star_outputs_polygon_tag():
	s = mid.star(5, (0, 0, 100, 100))
	assert s.strip().startswith("<polygon")
	assert 'points="' in s


def test_cubic_bezier_outputs_path_tag():
	s = mid.cubic_bezier(0, 0, 10, 0, 10, 10, 20, 20)
	assert s.strip().startswith("<path")
	assert 'd="M ' in s
	assert " C " in s

