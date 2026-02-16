# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
mini_svg/_utils.py
==================

Internal helpers for mini-svg.

This module is intentionally *not* part of the public API.
Public utilities live in `mini_svg.style`.

Notes
-----
- Keep functions here small and dependency-free.
- Functions here may change without notice (internal).
"""

from __future__ import annotations

import math
from typing import Tuple


def clamp(x: float, lo: float, hi: float) -> float:
	"""Clamp x to the inclusive range [lo, hi]."""
	if x < lo:
		return lo
	if x > hi:
		return hi
	return x


def fmt_num(x: float) -> str:
	"""
	Format numbers for SVG attributes.

	- Integers become "12" instead of "12.0"
	- Floats are compacted with trailing zeros removed
	"""
	if isinstance(x, int):
		return str(x)
	if abs(x - round(x)) < 1e-9:
		return str(int(round(x)))
	s = f"{x:.6f}".rstrip("0").rstrip(".")
	return s if s else "0"


def xml_escape(text: str) -> str:
	"""Escape text to be safely embedded in XML."""
	return (
		text.replace("&", "&amp;")
			.replace("<", "&lt;")
			.replace(">", "&gt;")
			.replace('"', "&quot;")
			.replace("'", "&apos;")
	)


def polar(cx: float, cy: float, r: float, angle_deg: float) -> Tuple[float,float]:
	"""Convert polar coordinates to cartesian coordinates."""
	a = math.radians(angle_deg)
	return (cx + r * math.cos(a), cy + r * math.sin(a))


class _Frozen:
	"""Base class to prevent attribute modification after initialization."""
	__is_frozen: bool = False

	def _freeze(self) -> None:
		object.__setattr__(self, "_Frozen__is_frozen", True)

	def __setattr__(self, name: str, value: object) -> None:
		if getattr(self, "_Frozen__is_frozen", False):
			raise AttributeError("This object is immutable.")
		object.__setattr__(self, name, value)


def style_attrs(
	*,
	stroke: str,
	stroke_width: int,
	fill: str,
	opacity: float
) -> str:
	"""
	Build SVG style attributes in a consistent order.

	Note: This helper expects *resolved* values (final values).
	The fallback logic (None -> defaults) belongs to mini_svg.style.
	"""
	return f' stroke="{stroke}" stroke-width="{stroke_width}" fill="{fill}" opacity="{fmt_num(opacity)}"'

