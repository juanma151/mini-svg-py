# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
mini_svg.advanced
=================

Level: Advanced

Part of the mini-svg project by :hagane.

This module builds on top of `mini_svg.intermediate` and introduces more
flexible path-based drawing features.

It reuses all functionality from previous levels and adds:

- bezier_path_cubic()

This function allows defining multi-segment cubic Bézier paths using lists
of control points.

New concepts introduced at this level:
- Lists and tuples as structured data
- Iterating over structured geometry definitions
- SVG <path> syntax
- Multi-segment curve construction
- Optional path closing

This level is appropriate for more advanced students ready to handle
collections, structured data, and more abstract geometric thinking.

Standard library only.
"""

from __future__ import annotations
from typing import List, Optional, Tuple

from . import intermediate
from .intermediate import *
from .intermediate import _style


def bezier_path_cubic(
	start: Tuple[float, float],
	segments: List[Tuple[float, float, float, float, float, float]],
	*,
	closed: bool = False,
	stroke: str = "black",
	stroke_width: int = 2,
	fill: str = "none",
	opacity: Optional[float] = None
) -> str:
	"""
	start = (x0, y0)
	segments = [(cx1, cy1, cx2, cy2, x, y), ...]  # each tuple adds one 'C'
	"""
	x0, y0 = start
	d_parts = [f"M {x0:.2f},{y0:.2f}"]
	for (cx1, cy1, cx2, cy2, x, y) in segments:
		d_parts.append(f"C {cx1:.2f},{cy1:.2f} {cx2:.2f},{cy2:.2f} {x:.2f},{y:.2f}")
	if closed:
		d_parts.append("Z")

	d = " ".join(d_parts)
	return f'<path d="{d}"{_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)} />\n'


__all__ = [
	*intermediate.__all__,
	"bezier_path_cubic",
]

