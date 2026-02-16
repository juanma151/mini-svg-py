# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
mini_svg/__init__.py
====================

Educational SVG generation library with progressive levels.

This package is part of the mini-svg project by :hagane.

Recommended usage (flat API)
----------------------------
```
import mini_svg as minisvg
# then use minisvg.circle(), minisvg.regular_polygon(), minisvg.set_style(), etc.
```

Progressive levels
------------------
```
from mini_svg import minisvg_basic
from mini_svg import minisvg_intermediate
from mini_svg import minisvg_advanced
```

Public utilities
----------------
- Colors, palettes and style utilities are provided by `mini_svg.style`.
- They are re-exported at package level for convenience.

See the documentation website and examples folder for full scripts.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version as _pkg_version

from .style import *  # noqa: F403
from .basic import *  # noqa: F403
from .intermediate import *  # noqa: F403
from .advanced import *  # noqa: F403

from . import basic as minisvg_basic
from . import intermediate as minisvg_intermediate
from . import advanced as minisvg_advanced
from . import style as utils


try:
	__version__ = _pkg_version("mini-svg")
except PackageNotFoundError:
	# When running from source without installation (or weird environments)
	__version__ = "0.0.0+local"


__all__ = [
	# version
	"__version__",
	# level modules
	"minisvg_basic",
	"minisvg_intermediate",
	"minisvg_advanced",
	# public style module as "utils"
	"utils",
]

