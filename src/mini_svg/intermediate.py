# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
mini_svg/intermediate.py
========================

Level: Intermediate

Builds on `mini_svg.basic` and adds:

- text(): draw text labels
- group(): group elements (like layers)
- regular_polygon(): regular polygon in a bounding box
- star(): star polygon in a bounding box
- cubic_bezier(): a single cubic Bézier curve as a path

Recommended usage (flat API)
----------------------------
```
import mini_svg as minisvg

parts = [minisvg.svg_begin(400, 300)]
parts.append(minisvg.text(200, 30, "Hello", anchor="middle"))
parts.append(minisvg.regular_polygon(6, (150, 80, 100, 100), fill=minisvg.COLORS.SUNFLOWER))
parts.append(minisvg.svg_end())
minisvg.save_svg("out.svg", parts)
```

See also
--------
Look at the repository examples folder for complete scripts.
"""

from __future__ import annotations

from typing import List, Optional, Tuple

from .basic import (
	COLORS,
	PALETTES,
	circle,
	get_style,
	line,
	palette_pick,
	rect,
	save_svg,
	set_style,
	svg_begin,
	svg_end,
)
from .style import _resolve_style
from ._utils import fmt_num, polar, style_attrs, xml_escape


def text(
	x: float,
	y: float,
	content: str,
	*,
	font_size: Optional[int] = None,
	fill: Optional[str] = None,
	anchor: str = "start",
	opacity: Optional[float] = None
) -> str:
	"""
	Draw text.

	Parameters
	----------
	x, y
		Text position.
	content
		Text content (will be XML-escaped).
	font_size
		Font size in pixels. If None, uses global default `font_size`.
	fill
		Text color. If None, defaults to COLORS.BLACK.
	anchor
		SVG text-anchor: "start", "middle", or "end".
	opacity
		Opacity 0.0..1.0. If None, uses global default `opacity`.

	Returns
	-------
	str
		SVG <text> fragment.
	"""
	if font_size is None:
		font_size = int(get_style("font_size"))
	if fill is None:
		fill = COLORS.BLACK
	if opacity is None:
		opacity = float(get_style("opacity"))

	return (
		f'<text x="{fmt_num(x)}" y="{fmt_num(y)}" '
		f'font-size="{int(font_size)}" fill="{fill}" text-anchor="{anchor}" opacity="{fmt_num(opacity)}">'
		f'{xml_escape(content)}</text>\n'
	)


def group(
	elements: List[str],
	*,
	transform: Optional[str] = None,
	opacity: Optional[float] = None
) -> str:
	"""
	Group multiple SVG fragments inside a <g> element.

	Parameters
	----------
	elements
		List of SVG fragments.
	transform
		Raw SVG transform string (e.g. "rotate(30 200 200)").
	opacity
		Group opacity. If None, uses global default `opacity`.

	Returns
	-------
	str
		SVG <g> fragment containing all elements.
	"""
	if opacity is None:
		opacity = float(get_style("opacity"))
	tf = f' transform="{transform}"' if transform else ""
	return f'<g{tf} opacity="{fmt_num(opacity)}">\n{"".join(elements)}</g>\n'


def _bbox_center(bbox: Tuple[float,float,float,float]) -> Tuple[float,float]:
	x, y, w, h = bbox
	return (x + w / 2, y + h / 2)


def regular_polygon(
	n_sides: int,
	bbox: Tuple[float,float,float,float],
	*,
	rotation_deg: Optional[float] = None,
	stroke: Optional[str] = None,
	stroke_width: Optional[int] = None,
	fill: Optional[str] = None,
	opacity: Optional[float] = None
) -> str:
	"""
	Draw a regular polygon inside a bounding box.

	Parameters
	----------
	n_sides
		Number of sides (>= 3).
	bbox
		Bounding box (x, y, width, height).
	rotation_deg
		Rotation angle in degrees. If None, uses global default `rotation_deg`.
	stroke, stroke_width, fill, opacity
		Style parameters. If omitted (None), use global defaults.

	Returns
	-------
	str
		SVG <polygon> fragment.

	Raises
	------
	ValueError
		If n_sides < 3.
	"""
	if n_sides < 3:
		raise ValueError("n_sides must be >= 3")

	if rotation_deg is None:
		rotation_deg = float(get_style("rotation_deg"))

	cx, cy = _bbox_center(bbox)
	_, _, w, h = bbox
	r = min(w, h) / 2

	points: list[str] = []
	for i in range(n_sides):
		ang = float(rotation_deg) - 90 + (360.0 * i / n_sides)
		px, py = polar(cx, cy, r, ang)
		points.append(f"{fmt_num(px)},{fmt_num(py)}")

	s, sw, f, o = _resolve_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)
	return f'<polygon points="{" ".join(points)}"{style_attrs(stroke=s, stroke_width=sw, fill=f, opacity=o)} />\n'


def star(
	n_points: int,
	bbox: Tuple[float,float,float,float],
	*,
	rotation_deg: Optional[float] = None,
	inner_ratio: float = 0.5,
	stroke: Optional[str] = None,
	stroke_width: Optional[int] = None,
	fill: Optional[str] = None,
	opacity: Optional[float] = None
) -> str:
	"""
	Draw a star inside a bounding box.

	Parameters
	----------
	n_points
		Number of outer points (>= 3).
	bbox
		Bounding box (x, y, width, height).
	rotation_deg
		Rotation angle in degrees. If None, uses global default `rotation_deg`.
	inner_ratio
		Inner radius ratio (0..1). Typical values: 0.4..0.6.
	stroke, stroke_width, fill, opacity
		Style parameters. If omitted (None), use global defaults.

	Returns
	-------
	str
		SVG <polygon> fragment.

	Raises
	------
	ValueError
		If n_points < 3 or inner_ratio not in (0, 1).
	"""
	if n_points < 3:
		raise ValueError("n_points must be >= 3")
	if not (0.0 < float(inner_ratio) < 1.0):
		raise ValueError("inner_ratio must be between 0 and 1 (exclusive)")

	if rotation_deg is None:
		rotation_deg = float(get_style("rotation_deg"))

	cx, cy = _bbox_center(bbox)
	_, _, w, h = bbox
	r_outer = min(w, h) / 2
	r_inner = r_outer * float(inner_ratio)

	points: list[str] = []
	total = n_points * 2
	for i in range(total):
		r = r_outer if i % 2 == 0 else r_inner
		ang = float(rotation_deg) - 90 + (360.0 * i / total)
		px, py = polar(cx, cy, r, ang)
		points.append(f"{fmt_num(px)},{fmt_num(py)}")

	s, sw, f, o = _resolve_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)
	return f'<polygon points="{" ".join(points)}"{style_attrs(stroke=s, stroke_width=sw, fill=f, opacity=o)} />\n'


def cubic_bezier(
	x0: float, y0: float,
	cx1: float, cy1: float,
	cx2: float, cy2: float,
	x: float, y: float,
	*,
	stroke: Optional[str] = None,
	stroke_width: Optional[int] = None,
	fill: Optional[str] = None,
	opacity: Optional[float] = None
) -> str:
	"""
	Draw a single cubic Bézier curve using an SVG path.

	Parameters
	----------
	x0, y0
		Start point.
	cx1, cy1
		Control point 1.
	cx2, cy2
		Control point 2.
	x, y
		End point.
	stroke, stroke_width, fill, opacity
		Style parameters. If omitted (None), use global defaults.

	Returns
	-------
	str
		SVG <path> fragment.
	"""
	d = (
		f"M {fmt_num(x0)} {fmt_num(y0)} "
		f"C {fmt_num(cx1)} {fmt_num(cy1)} {fmt_num(cx2)} {fmt_num(cy2)} {fmt_num(x)} {fmt_num(y)}"
	)
	s, sw, f, o = _resolve_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)
	return f'<path d="{d}"{style_attrs(stroke=s, stroke_width=sw, fill=f, opacity=o)} />\n'


__all__ = [
	"svg_begin",
	"svg_end",
	"save_svg",
	"line",
	"rect",
	"circle",
	"COLORS",
	"PALETTES",
	"palette_pick",
	"set_style",
	"get_style",
	"text",
	"group",
	"regular_polygon",
	"star",
	"cubic_bezier",
]

