# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
mini_svg/style.py
=================

Public style utilities for the mini-svg project by :hagane.

This module is part of the public API and is meant to be documented.

It provides:

Colors
------
- rgb(), hex_to_rgb()
- gray_255(), gray_percent()
- hsl()
- COLORS (immutable constants)

Palettes
--------
- PALETTES (immutable tuples of colors)
- palette_pick()

Global defaults
---------------
- set_style(...)
- get_style(field)

The default style is used by drawing functions when style parameters
are omitted (passed as None).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

from ._utils import _Frozen, clamp


def rgb(r: int, g: int, b: int) -> str:
	"""
	Convert RGB components (0..255) to a hex SVG color string.

	Parameters
	----------
	r, g, b
		Red, green and blue components as integers in the range 0..255.

	Returns
	-------
	str
		A hex color string like "#ff8800", suitable for SVG `fill` or `stroke`.

	Examples
	--------
	```
	import mini_svg as minisvg
	color = minisvg.rgb(255, 136, 0)
	# "#ff8800"
	```
	"""
	r = int(clamp(r, 0, 255))
	g = int(clamp(g, 0, 255))
	b = int(clamp(b, 0, 255))
	return f"#{r:02x}{g:02x}{b:02x}"


def hex_to_rgb(hex_color: str) -> Tuple[int,int,int]:
	"""
	Convert a hex color string "#rrggbb" to an (r, g, b) tuple.

	Parameters
	----------
	hex_color
		A hex color string like "#ff8800".

	Returns
	-------
	Tuple[int, int, int]
		(r, g, b) tuple with integers in the range 0..255.

	Raises
	------
	ValueError
		If `hex_color` is not in the form "#rrggbb".

	Examples
	--------
	```
	import mini_svg as minisvg
	r, g, b = minisvg.hex_to_rgb("#ff8800")
	```
	"""
	h = hex_color.lower()
	if not (h.startswith("#") and len(h) == 7):
		raise ValueError("Expected hex color like '#rrggbb'")
	return (int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16))


def gray_255(v: int) -> str:
	"""
	Create a grayscale color from an integer intensity (0..255).

	Parameters
	----------
	v
		Intensity from 0 (black) to 255 (white).

	Returns
	-------
	str
		A hex grayscale color string like "#808080".
	"""
	v = int(clamp(v, 0, 255))
	return rgb(v, v, v)


def gray_percent(p: float) -> str:
	"""
	Create a grayscale color from a percentage in the range 0.0..1.0.

	Parameters
	----------
	p
		0.0 produces black, 1.0 produces white.

	Returns
	-------
	str
		A hex grayscale color string.
	"""
	p = clamp(p, 0.0, 1.0)
	return gray_255(int(round(p * 255)))


def _hue_to_rgb(p: float, q: float, t: float) -> float:
	if t < 0:
		t += 1
	if t > 1:
		t -= 1
	if t < 1/6:
		return p + (q - p) * 6 * t
	if t < 1/2:
		return q
	if t < 2/3:
		return p + (q - p) * (2/3 - t) * 6
	return p


def hsl(h: float, s: float, l: float) -> str:
	"""
	Convert HSL (Hue, Saturation, Lightness) to a hex SVG color string.

	Parameters
	----------
	h
		Hue in degrees (any value; wraps around 360).
	s
		Saturation in the range 0.0..1.0.
	l
		Lightness in the range 0.0..1.0.

	Returns
	-------
	str
		A hex color string like "#33aaff".

	Notes
	-----
	This is very convenient for generative art: sweep hue in a loop.

	Examples
	--------
	```
	import mini_svg as minisvg
	for i in range(10):
		c = minisvg.hsl(i * 36, 0.8, 0.5)
	```
	"""
	h = (h % 360.0) / 360.0
	s = clamp(s, 0.0, 1.0)
	l = clamp(l, 0.0, 1.0)

	if s == 0:
		return gray_percent(l)

	q = l * (1 + s) if l < 0.5 else l + s - l * s
	p = 2 * l - q
	rf = _hue_to_rgb(p, q, h + 1/3)
	gf = _hue_to_rgb(p, q, h)
	bf = _hue_to_rgb(p, q, h - 1/3)

	return rgb(int(round(rf * 255)), int(round(gf * 255)), int(round(bf * 255)))


class _Colors(_Frozen):
	"""
	Immutable collection of predefined SVG color constants.

	Each attribute is a string valid for SVG `fill` / `stroke`.

	Examples
	--------
	```
	import mini_svg as minisvg
	fill = minisvg.COLORS.SUNFLOWER
	stroke = minisvg.COLORS.DARK_GRAY
	```
	"""

	def __init__(self) -> None:
		self.BLACK = "#000000"
		self.WHITE = "#ffffff"
		self.TRANSPARENT = "none"

		self.RED = "#ff0000"
		self.GREEN = "#00aa00"
		self.BLUE = "#0000ff"
		self.YELLOW = "#ffff00"
		self.CYAN = "#00ffff"
		self.MAGENTA = "#ff00ff"
		self.ORANGE = "#ff8800"
		self.PURPLE = "#800080"

		self.GRAY = "#808080"
		self.LIGHT_GRAY = "#cccccc"
		self.DARK_GRAY = "#444444"

		self.HOT_RED = "#ff3b3b"
		self.BRIGHT_BLUE = "#2d7dff"
		self.EMERALD = "#2ecc71"
		self.SUNFLOWER = "#ffd23f"
		self.TEAL = "#1abc9c"

		self._freeze()


COLORS = _Colors()


@dataclass
class _Style:
	stroke: str = COLORS.BLACK
	fill: str = COLORS.TRANSPARENT
	stroke_width: int = 1
	opacity: float = 1.0
	rotation_deg: float = 0.0
	font_size: int = 12


_STYLE = _Style()


def set_style(
	*,
	stroke: Optional[str] = None,
	fill: Optional[str] = None,
	stroke_width: Optional[int] = None,
	opacity: Optional[float] = None,
	rotation_deg: Optional[float] = None,
	font_size: Optional[int] = None
) -> None:
	"""
	Set global default drawing style.

	Any parameter left as None remains unchanged.

	Parameters
	----------
	stroke
		Default stroke (outline) color.
	fill
		Default fill color.
	stroke_width
		Default stroke width (integer pixels).
	opacity
		Default opacity (0.0..1.0).
	rotation_deg
		Default rotation angle in degrees (used by polygons/stars).
	font_size
		Default font size (used by text()).

	Notes
	-----
	Drawing functions use these defaults when their style parameters are omitted.

	Examples
	--------
	```
	import mini_svg as minisvg
	minisvg.set_style(stroke=minisvg.COLORS.DARK_GRAY, stroke_width=2, opacity=0.9)
	```
	"""
	if stroke is not None:
		_STYLE.stroke = stroke
	if fill is not None:
		_STYLE.fill = fill
	if stroke_width is not None:
		_STYLE.stroke_width = int(stroke_width)
	if opacity is not None:
		_STYLE.opacity = float(opacity)
	if rotation_deg is not None:
		_STYLE.rotation_deg = float(rotation_deg)
	if font_size is not None:
		_STYLE.font_size = int(font_size)


def get_style(field: str) -> object:
	"""
	Get one global default style field by name.

	Parameters
	----------
	field
		Name of the field.

	Returns
	-------
	object
		The current value.

	Raises
	------
	KeyError
		If field does not exist.

	Examples
	--------
	```
	import mini_svg as minisvg
	current = minisvg.get_style("stroke_width")
	```
	"""
	if not hasattr(_STYLE, field):
		raise KeyError(f"Unknown style field: {field}")
	return getattr(_STYLE, field)


def _resolve_style(
	*,
	stroke: Optional[str],
	stroke_width: Optional[int],
	fill: Optional[str],
	opacity: Optional[float]
) -> Tuple[str,int,str,float]:
	"""
	Internal: resolve None parameters into current global defaults.

	This is used by the drawing modules (basic/intermediate/advanced).
	"""
	s = _STYLE.stroke if stroke is None else stroke
	w = _STYLE.stroke_width if stroke_width is None else int(stroke_width)
	f = _STYLE.fill if fill is None else fill
	o = _STYLE.opacity if opacity is None else float(opacity)
	return (s, w, f, o)


class _Palettes(_Frozen):
	"""
	Immutable collection of predefined palettes.

	Each palette is a tuple[str, ...] containing SVG-ready color values.

	Examples
	--------
	```
	import mini_svg as minisvg
	p = minisvg.PALETTES.WARHOL
	fill = p[3]
	```
	"""

	def __init__(self) -> None:
		self.WARHOL = (
			COLORS.HOT_RED,
			COLORS.BRIGHT_BLUE,
			COLORS.SUNFLOWER,
			COLORS.EMERALD,
			COLORS.PURPLE,
			COLORS.TEAL,
		)

		self.PRIMARY = (
			COLORS.RED,
			COLORS.GREEN,
			COLORS.BLUE,
			COLORS.YELLOW,
			COLORS.CYAN,
			COLORS.MAGENTA,
		)

		self.GRAYS_10 = tuple(gray_percent(i / 9) for i in range(10))

		self.SOFT = (
			hsl(210, 0.55, 0.65),
			hsl(140, 0.45, 0.60),
			hsl(35, 0.70, 0.65),
			hsl(290, 0.35, 0.70),
			hsl(0, 0.55, 0.70),
		)

		self._freeze()


PALETTES = _Palettes()


def palette_pick(palette: Tuple[str, ...], i: int) -> str:
	"""
	Pick a color from a palette using wrap-around indexing.

	Parameters
	----------
	palette
		A palette tuple, for example `PALETTES.WARHOL`.
	i
		Any integer index. The palette wraps around automatically.

	Returns
	-------
	str
		A color string.

	Examples
	--------
	```
	import mini_svg as minisvg
	p = minisvg.PALETTES.WARHOL
	c0 = minisvg.palette_pick(p, 0)
	c1 = minisvg.palette_pick(p, 999)  # wraps around
	```
	"""
	if not palette:
		raise ValueError("Palette is empty")
	return palette[i % len(palette)]


__all__ = [
	"COLORS",
	"PALETTES",
	"rgb",
	"hex_to_rgb",
	"gray_255",
	"gray_percent",
	"hsl",
	"palette_pick",
	"set_style",
	"get_style",
]

