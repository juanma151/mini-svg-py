# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
01_01_lines.py

Level 1 (Basic): line()

Goal
----
Learn:
- coordinates (x, y)
- loops
- simple patterns
"""

from __future__ import annotations

import mini_svg as minisvg
from examples._shared.paths import out_path_for_script


def main() -> None:
	out = out_path_for_script(__file__)

	w, h = 600, 300
	parts: list[str] = [minisvg.svg_begin(w, h)]

	# A fan of lines from the left-middle to the right side.
	x1, y1 = 40, h / 2
	for i in range(0, 11):
		x2 = w - 40
		y2 = 40 + i * (h - 80) / 10
		parts.append(minisvg.line(x1, y1, x2, y2))

	parts.append(minisvg.svg_end())
	minisvg.save_svg(str(out), parts)
	print(out)


if __name__ == "__main__":
	main()

