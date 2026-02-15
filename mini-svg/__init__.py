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

The library is structured in progressive levels:

- basic        → foundational shapes and SVG structure
- intermediate → polygons, stars, text, grouping, single Bézier curves
- advanced     → multi-segment Bézier paths

You may import levels explicitly:

	from mini_svg import basic
	from mini_svg import intermediate
	from mini_svg import advanced

Or use the alias:

	from mini_svg import all

where `all` points to the most advanced level.

Standard library only.
"""

from . import basic, intermediate, advanced

# Educational alias: the "full" API is the advanced level.
all = advanced

__all__ = ["basic", "intermediate", "advanced", "all"]
__version__ = "0.1.0"

