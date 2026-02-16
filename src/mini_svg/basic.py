# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
mini_svg/basic.py
=================

Level: Basic

Core SVG primitives for educational use.

This module provides:
- SVG document helpers: svg_begin(), svg_end(), save_svg()
- Basic shapes: line(), rect(), circle()

Style behavior
--------------
Most drawing functions accept style parameters (stroke, fill, etc.). If a style
parameter is omitted (passed as None), the global defaults from `mini_svg.style`
are used.

Recommended usage (flat API)
----------------------------
```
import mini_svg as minisvg

parts = [
	minisvg.svg_begin(400, 300),
	minisvg.circle(200, 150, 80, fill=minisvg.COLORS.SUNFLOWER),
	minisvg.svg_end(),
]
minisvg.save_svg("out.svg", parts)
```

See also
--------
- `mini_svg.style` for COLORS, PALETTES and global style defaults.
- The project examples folder for more complete scripts.
"""

from __future__ import annotations

from typing import List, Optional, Tuple

from .style import COLORS, PALETTES, get_style, palette_pick, set_style, _resolve_style
from ._utils import fmt_num, style_attrs


def svg_begin(width: int, height: int, *, viewbox: Optional[Tuple[int,int,int,int]] = None) -> str:
	"""
	Start an SVG document and return the header fragment.

	Parameters
	----------
	width, height
		Document dimensions in pixels.
	viewbox
		Optional SVG viewBox (x, y, w, h). If not provided, defaults to (0, 0, width, height).

	Returns
	-------
	str
		SVG header fragment including XML declaration and opening <svg>.
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

	Returns
	-------
	str
		Closing </svg> fragment.
	"""
	return "</svg>\n"


def save_svg(filename: str, parts: List[str]) -> None:
	"""
	Save a list of SVG fragments into a file.

	Parameters
	----------
	filename
		Output filename (e.g. "out.svg").
	parts
		List of SVG fragments (strings). Usually: [svg_begin(...), ..., svg_end()].
	"""
	with open(filename, "w", encoding="utf-8") as f:
		f.write("".join(parts))


def line(
	x1: float, y1: float, x2: float, y2: float,
	*,
	stroke: Optional[str] = None,
	stroke_width: Optional[int] = None,
	opacity: Optional[float] = None
) -> str:
	"""
	Draw a straight line.

	Parameters
	----------
	x1, y1, x2, y2
		Endpoints of the line.
	stroke
		Stroke color. If None, uses global default `stroke`.
	stroke_width
		Stroke width in pixels. If None, uses global default `stroke_width`.
	opacity
		Opacity 0.0..1.0. If None, uses global default `opacity`.

	Returns
	-------
	str
		SVG <line> fragment.
	"""
	s, w, _, o = _resolve_style(stroke=stroke, stroke_width=stroke_width, fill=COLORS.TRANSPARENT, opacity=opacity)
	return (
		f'<line x1="{fmt_num(x1)}" y1="{fmt_num(y1)}" x2="{fmt_num(x2)}" y2="{fmt_num(y2)}"'
		f'{style_attrs(stroke=s, stroke_width=w, fill=COLORS.TRANSPARENT, opacity=o)} />\n'
	)


def rect(
	x: float, y: float, w: float, h: float,
	*,
	stroke: Optional[str] = None,
	stroke_width: Optional[int] = None,
	fill: Optional[str] = None,
	rx: Optional[float] = None,
	ry: Optional[float] = None,
	opacity: Optional[float] = None
) -> str:
	"""
	Draw a rectangle.

	Parameters
	----------
	x, y
		Top-left corner of the rectangle.
	w, h
		Width and height.
	stroke
		Stroke color. If None, uses global default `stroke`.
	stroke_width
		Stroke width in pixels. If None, uses global default `stroke_width`.
	fill
		Fill color. If None, uses global default `fill`.
	rx, ry
		Optional corner radii (rounded corners).
	opacity
		Opacity 0.0..1.0. If None, uses global default `opacity`.

	Returns
	-------
	str
		SVG <rect> fragment.
	"""
	s, sw, f, o = _resolve_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)
	r = ""
	if rx is not None:
		r += f' rx="{fmt_num(rx)}"'
	if ry is not None:
		r += f' ry="{fmt_num(ry)}"'
	return (
		f'<rect x="{fmt_num(x)}" y="{fmt_num(y)}" width="{fmt_num(w)}" height="{fmt_num(h)}"{r}'
		f'{style_attrs(stroke=s, stroke_width=sw, fill=f, opacity=o)} />\n'
	)


def circle(
	cx: float, cy: float, r: float,
	*,
	stroke: Optional[str] = None,
	stroke_width: Optional[int] = None,
	fill: Optional[str] = None,
	opacity: Optional[float] = None
) -> str:
	"""
	Draw a circle.

	Parameters
	----------
	cx, cy
		Center position.
	r
		Radius.
	stroke
		Stroke color. If None, uses global default `stroke`.
	stroke_width
		Stroke width in pixels. If None, uses global default `stroke_width`.
	fill
		Fill color. If None, uses global default `fill`.
	opacity
		Opacity 0.0..1.0. If None, uses global default `opacity`.

	Returns
	-------
	str
		SVG <circle> fragment.
	"""
	s, sw, f, o = _resolve_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)
	return (
		f'<circle cx="{fmt_num(cx)}" cy="{fmt_num(cy)}" r="{fmt_num(r)}"'
		f'{style_attrs(stroke=s, stroke_width=sw, fill=f, opacity=o)} />\n'
	)


__all__ = [
	"svg_begin",
	"svg_end",
	"save_svg",
	"line",
	"rect",
	"circle",
	# style re-exports for convenience at this level
	"COLORS",
	"PALETTES",
	"palette_pick",
	"set_style",
	"get_style",
]

