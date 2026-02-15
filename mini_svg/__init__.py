# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
mini_svg
========

mini-svg is a lightweight educational Python library for generating SVG
graphics using simple programming constructs.

Created and maintained by :hagane.

Overview
--------

The library is structured in progressive levels, each building on top
of the previous one.

Level 1 — minisvg_basic
-----------------------

Foundational SVG primitives:

- svg_begin()
- svg_end()
- save_svg()
- line()
- rect()
- circle()

This level introduces:
- Functions
- Parameters
- Simple geometry
- Writing files
- Building SVG documents from fragments

Recommended for absolute beginners.

Level 2 — minisvg_intermediate
------------------------------

Includes everything from Level 1, plus:

- text()
- group()
- regular_polygon()
- star()
- cubic_bezier()

This level introduces:
- Polar coordinates
- Bounding boxes
- Rotation
- Parametric shapes
- Basic Bézier curves
- SVG grouping (<g>)

Recommended for students comfortable with loops and basic math.

Level 3 — minisvg_advanced
--------------------------

Includes everything from Level 2, plus:

- bezier_path_cubic()

This level introduces:
- Lists of structured tuples
- Multi-segment path construction
- SVG <path> syntax
- More abstract geometric reasoning

Recommended for advanced students working with collections and
structured data.

Usage styles
------------

1) Flat API (recommended for most users):

	import mini_svg as minisvg
	minisvg.circle(...)
	minisvg.star(...)
	minisvg.bezier_path_cubic(...)

This exposes the full (advanced) API directly.

2) Progressive level import:

	from mini_svg import minisvg_basic
	from mini_svg import minisvg_intermediate
	from mini_svg import minisvg_advanced

Useful when restricting available functionality in a classroom.

Versioning
----------

The package version is read dynamically from installed metadata
(pyproject.toml).
"""

from importlib.metadata import PackageNotFoundError, version

# Progressive levels (public descriptive names)
from . import basic as minisvg_basic
from . import intermediate as minisvg_intermediate
from . import advanced as minisvg_advanced

# Flat API: re-export the most advanced level
from .advanced import *  # noqa: F403

# Public exports: flat API + named levels
__all__ = [
	*minisvg_advanced.__all__,  # type: ignore[attr-defined]
	"minisvg_basic",
	"minisvg_intermediate",
	"minisvg_advanced",
]

# Dynamic version reading
try:
	__version__ = version("mini-svg")
except PackageNotFoundError:
	__version__ = "0.0.0-dev"

