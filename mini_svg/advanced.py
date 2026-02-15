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

Adds multi-segment Bézier paths.

Introduces structured data (lists of tuples) and iterative path construction.

For full demonstrations, see the documentation and the `examples/` folder.
"""

from __future__ import annotations
from typing import List, Tuple

from .intermediate import *


def bezier_path_cubic(
	start: Tuple[float, float],
	segments: List[Tuple[float, float, float, float, float, float]],
) -> str:
	"""
	Create a multi-segment cubic Bézier path.

	Args:
		start: Starting point (x0, y0).
		segments: List of (cx1, cy1, cx2, cy2, x, y) tuples.

	Returns:
		str: SVG <path> element.
	"""
	x0, y0 = start
	d_parts = [f"M {x0},{y0}"]
	for (cx1, cy1, cx2, cy2, x, y) in segments:
		d_parts.append(f"C {cx1},{cy1} {cx2},{cy2} {x},{y}")
	return f'<path d="{" ".join(d_parts)}" stroke="black" fill="none" />\n'


__all__ = [
	*intermediate.__all__,
	"bezier_path_cubic",
]

