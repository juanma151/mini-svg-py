# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
01_02_rectangles.py

Level 1 (Basic): rect()

Goal
----
Learn:
- loops
- parameters
- building a grid
"""

from __future__ import annotations

import mini_svg as minisvg
from examples._shared.paths import out_path_for_script


def main() -> None:
	out = out_path_for_script(__file__)

	w, h = 600, 300
	parts: list[str] = [minisvg.svg_begin(w, h)]

	cell = 50
	for row in range(0, h // cell):
		for col in range(0, w // cell):
			x = col * cell
			y = row * cell
			# Checker pattern with a simple conditional.
			if (row + col) % 2 == 0:
				fill = minisvg.COLORS.LIGHT_GRAY
			else:
				fill = minisvg.COLORS.TRANSPARENT
			parts.append(minisvg.rect(x, y, cell, cell, fill=fill))

	parts.append(minisvg.svg_end())
	minisvg.save_svg(str(out), parts)
	print(out)


if __name__ == "__main__":
	main()

