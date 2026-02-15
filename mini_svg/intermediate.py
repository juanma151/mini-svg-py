# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
mini_svg.intermediate
=====================

Level: Intermediate

Builds on the basic module and adds:

- text()
- group()
- regular_polygon()
- star()
- cubic_bezier()

Introduces geometric reasoning and polar coordinates.

For extended examples (mandalas, grids, stars),
see the `examples/` directory and documentation pages.
"""

from __future__ import annotations
import math
from typing import List, Optional, Tuple

from .basic import *


BBox = Tuple[float, float, float, float]

__all__ = [
	"svg_begin", "svg_end", "save_svg",
	"line", "rect", "circle",
	"text", "group",
	"regular_polygon", "star",
	"cubic_bezier",
]


def text(x: float, y: float, content: str, *, font_size: int = 16, fill: str = "black") -> str:
	"""
	Create an SVG <text> element.

	Args:
		x, y: Text baseline coordinates.
		content: Text string.

	Returns:
		str: SVG <text> element.
	"""
	return f'<text x="{x}" y="{y}" font-size="{font_size}" fill="{fill}">{content}</text>\n'


def group(elements: List[str]) -> str:
	"""
	Group multiple SVG fragments inside a <g> element.

	Args:
		elements: List of SVG strings.

	Returns:
		str: SVG <g> group.
	"""
	return "<g>\n" + "".join(elements) + "</g>\n"


def _polar_to_xy(cx: float, cy: float, r: float, angle_deg: float) -> Tuple[float, float]:
	a = math.radians(angle_deg)
	return cx + r * math.cos(a), cy + r * math.sin(a)


def regular_polygon(n_sides: int, bbox: BBox) -> str:
	"""
	Create a regular polygon inside a bounding box.

	Args:
		n_sides: Number of sides (>=3).
		bbox: (x, y, width, height)

	Returns:
		str: SVG <polygon> element.
	"""
	if n_sides < 3:
		raise ValueError("n_sides must be >= 3")

	x, y, w, h = bbox
	cx, cy = x + w/2, y + h/2
	r = min(w, h)/2

	points = []
	step = 360 / n_sides
	for i in range(n_sides):
		px, py = _polar_to_xy(cx, cy, r, i*step)
		points.append(f"{px:.2f},{py:.2f}")

	return f'<polygon points="{" ".join(points)}" stroke="black" fill="none" />\n'


def star(n_points: int, bbox: BBox) -> str:
	"""
	Create a star shape.

	Args:
		n_points: Number of star points.
		bbox: (x, y, width, height)

	Returns:
		str: SVG <polygon> element.
	"""
	x, y, w, h = bbox
	cx, cy = x + w/2, y + h/2
	r_outer = min(w, h)/2
	r_inner = r_outer * 0.5

	points = []
	step = 360 / (n_points*2)
	for i in range(n_points*2):
		r = r_outer if i % 2 == 0 else r_inner
		px, py = _polar_to_xy(cx, cy, r, i*step)
		points.append(f"{px:.2f},{py:.2f}")

	return f'<polygon points="{" ".join(points)}" stroke="black" fill="none" />\n'


def cubic_bezier(x0, y0, cx1, cy1, cx2, cy2, x, y) -> str:
	"""
	Create a single cubic Bézier curve as an SVG <path>.

	Args:
		x0, y0: Start point.
		cx1, cy1: First control point.
		cx2, cy2: Second control point.
		x, y: End point.

	Returns:
		str: SVG <path> element.
	"""
	d = f"M {x0},{y0} C {cx1},{cy1} {cx2},{cy2} {x},{y}"
	return f'<path d="{d}" stroke="black" fill="none" />\n'

