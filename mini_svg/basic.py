# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
mini_svg.basic
==============

Level: Basic

Core SVG primitives for educational use.

This module provides the minimal building blocks required to generate
valid SVG documents using plain Python (standard library only).

Included features:
- svg_begin() / svg_end()
- save_svg()
- line()
- rect()
- circle()

All functions return SVG fragments as strings. Users are expected to
accumulate these fragments in a list and write them to a file.

For full classroom examples, see the `examples/` directory and the
documentation pages under "Examples".
"""

from __future__ import annotations
from typing import List, Optional, Tuple


def svg_begin(width: int, height: int, *, viewbox: Optional[Tuple[int, int, int, int]] = None) -> str:
	"""
	Start an SVG document and return the opening XML/SVG header.

	Args:
		width: Width of the SVG in pixels.
		height: Height of the SVG in pixels.
		viewbox: Optional tuple (x, y, w, h). Defaults to (0, 0, width, height).

	Returns:
		str: SVG header string.

	Basic example:

	```
	import mini_svg as minisvg

	parts = []
	parts.append(minisvg.svg_begin(200, 200))
	parts.append(minisvg.svg_end())
	minisvg.save_svg("empty.svg", parts)
	```

	See the documentation "Basic Examples" for more.
	"""
	if viewbox is None:
		viewbox = (0, 0, width, height)
	x, y, w, h = viewbox
	return (
		'<?xml version="1.0" encoding="UTF-8"?>\n'
		f'<svg xmlns="http://www.w3.org/2000/svg" '
		f'width="{width}" height="{height}" '
		f'viewBox="{x} {y} {w} {h}">\n'
	)


def svg_end() -> str:
	"""
	End an SVG document.

	Returns:
		str: Closing </svg> tag.
	"""
	return "</svg>\n"


def save_svg(filename: str, parts: List[str]) -> None:
	"""
	Write a list of SVG fragments to a file.

	Args:
		filename: Output filename.
		parts: List of SVG fragments.

	Returns:
		None
	"""
	with open(filename, "w", encoding="utf-8") as f:
		f.write("".join(parts))


def _style(*, stroke: str, stroke_width: int, fill: str, opacity: Optional[float]) -> str:
	op = f' opacity="{opacity}"' if opacity is not None else ""
	return f' stroke="{stroke}" stroke-width="{stroke_width}" fill="{fill}"{op}'


def line(
	x1: float, y1: float, x2: float, y2: float,
	*, stroke: str = "black", stroke_width: int = 2, opacity: Optional[float] = None
) -> str:
	"""
	Create an SVG <line> element.

	Args:
		x1, y1: Start coordinates.
		x2, y2: End coordinates.
		stroke: Stroke color.
		stroke_width: Stroke width in pixels.
		opacity: Optional opacity.

	Returns:
		str: SVG <line> element.
	"""
	return (
		f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"'
		f'{_style(stroke=stroke, stroke_width=stroke_width, fill="none", opacity=opacity)} />\n'
	)


def rect(
	x: float, y: float, w: float, h: float,
	*, stroke: str = "black", stroke_width: int = 2, fill: str = "none",
	rx: Optional[float] = None, ry: Optional[float] = None,
	opacity: Optional[float] = None
) -> str:
	"""
	Create an SVG <rect> element.

	Args:
		x, y: Top-left corner.
		w, h: Width and height.
		rx, ry: Optional corner radius.
		fill: Fill color.

	Returns:
		str: SVG <rect> element.
	"""
	r = ""
	if rx is not None:
		r += f' rx="{rx}"'
	if ry is not None:
		r += f' ry="{ry}"'
	return (
		f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{r}'
		f'{_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)} />\n'
	)


def circle(
	cx: float, cy: float, r: float,
	*, stroke: str = "black", stroke_width: int = 2, fill: str = "none",
	opacity: Optional[float] = None
) -> str:
	"""
	Create an SVG <circle> element.

	Args:
		cx, cy: Center coordinates.
		r: Radius.
		fill: Fill color.

	Returns:
		str: SVG <circle> element.
	"""
	return (
		f'<circle cx="{cx}" cy="{cy}" r="{r}"'
		f'{_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)} />\n'
	)


__all__ = [
	"svg_begin",
	"svg_end",
	"save_svg",
	"line",
	"rect",
	"circle",
]

