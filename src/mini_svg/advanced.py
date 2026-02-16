# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
mini_svg/advanced.py
====================

Level: Advanced

Builds on `mini_svg.intermediate` and adds:

- bezier_path_cubic(): multi-segment cubic Bézier path

This level introduces structured data:
- a list of cubic segments (control points + end point)

Recommended usage (flat API)
----------------------------
```
import mini_svg as minisvg

parts = [minisvg.svg_begin(400, 300)]
path = minisvg.bezier_path_cubic(
	(50, 150),
	[
		(100, 50, 150, 250, 200, 150),
		(250, 50, 300, 250, 350, 150),
	],
	stroke=minisvg.COLORS.DARK_GRAY,
	fill=minisvg.COLORS.TRANSPARENT,
	stroke_width=3,
)
parts.append(path)
parts.append(minisvg.svg_end())
minisvg.save_svg("out.svg", parts)
```
"""

from __future__ import annotations

from typing import List, Optional, Tuple

from .intermediate import (
	COLORS,
	PALETTES,
	circle,
	cubic_bezier,
	get_style,
	group,
	line,
	palette_pick,
	rect,
	regular_polygon,
	save_svg,
	set_style,
	star,
	svg_begin,
	svg_end,
	text,
)
from .style import _resolve_style
from ._utils import fmt_num, style_attrs


def bezier_path_cubic(
	start: Tuple[float,float],
	segments: List[Tuple[float,float,float,float,float,float]],
	*,
	stroke: Optional[str] = None,
	stroke_width: Optional[int] = None,
	fill: Optional[str] = None,
	opacity: Optional[float] = None
) -> str:
	"""
	Draw a multi-segment cubic Bézier path.

	Parameters
	----------
	start
		Start point (x0, y0).
	segments
		List of cubic segments, each:
		(cx1, cy1, cx2, cy2, x, y)
	stroke, stroke_width, fill, opacity
		Style parameters. If omitted (None), use global defaults.

	Returns
	-------
	str
		SVG <path> fragment.

	Notes
	-----
	This function is "advanced" because it introduces lists and structured data.
	"""
	x0, y0 = start
	d_parts: list[str] = [f"M {fmt_num(x0)} {fmt_num(y0)}"]

	for (cx1, cy1, cx2, cy2, x, y) in segments:
		d_parts.append(
			f"C {fmt_num(cx1)} {fmt_num(cy1)} {fmt_num(cx2)} {fmt_num(cy2)} {fmt_num(x)} {fmt_num(y)}"
		)

	d = " ".join(d_parts)
	s, sw, f, o = _resolve_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)
	return f'<path d="{d}"{style_attrs(stroke=s, stroke_width=sw, fill=f, opacity=o)} />\n'


__all__ = [
	"svg_begin",
	"svg_end",
	"save_svg",
	"line",
	"rect",
	"circle",
	"text",
	"group",
	"regular_polygon",
	"star",
	"cubic_bezier",
	"COLORS",
	"PALETTES",
	"palette_pick",
	"set_style",
	"get_style",
	"bezier_path_cubic",
]

