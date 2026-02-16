# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
01_03_circles.py

Level 1 (Basic): circle()

Goal
----
Learn:
- loops
- changing values each iteration
"""

from __future__ import annotations

import mini_svg as minisvg
from examples._shared.paths import out_path_for_script


def main() -> None:
	out = out_path_for_script(__file__)

	w, h = 600, 300
	parts: list[str] = [minisvg.svg_begin(w, h)]

	cx, cy = w / 2, h / 2
	for i in range(1, 11):
		r = i * 12
		parts.append(minisvg.circle(cx, cy, r, stroke=minisvg.COLORS.DARK_GRAY, fill=minisvg.COLORS.TRANSPARENT))

	parts.append(minisvg.svg_end())
	minisvg.save_svg(str(out), parts)
	print(out)


if __name__ == "__main__":
	main()

