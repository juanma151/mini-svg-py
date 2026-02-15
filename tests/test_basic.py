# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
Tests for mini_svg basic (flat API).
"""

import mini_svg as minisvg


def test_svg_begin_and_end():
	out = minisvg.svg_begin(400, 300) + minisvg.svg_end()
	assert out.startswith('<?xml version="1.0" encoding="UTF-8"?>')
	assert '<svg xmlns="http://www.w3.org/2000/svg"' in out
	assert 'width="400"' in out
	assert 'height="300"' in out
	assert out.strip().endswith("</svg>")


def test_line_output():
	s = minisvg.line(0, 0, 10, 20)
	assert s.strip().startswith("<line")
	assert 'x1="0"' in s
	assert 'y1="0"' in s
	assert 'x2="10"' in s
	assert 'y2="20"' in s
	assert 'stroke="black"' in s
	assert 'stroke-width="2"' in s


def test_rect_output():
	s = minisvg.rect(5, 6, 70, 80, fill="red")
	assert s.strip().startswith("<rect")
	assert 'x="5"' in s
	assert 'y="6"' in s
	assert 'width="70"' in s
	assert 'height="80"' in s
	assert 'fill="red"' in s


def test_circle_output():
	s = minisvg.circle(10, 20, 30, fill="blue")
	assert s.strip().startswith("<circle")
	assert 'cx="10"' in s
	assert 'cy="20"' in s
	assert 'r="30"' in s
	assert 'fill="blue"' in s

