# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
02_02_groups_layers.py

Level 2 (Intermediate): group()

Goal
----
Learn:
- grouping elements
- applying a transform to a group
"""

from __future__ import annotations

import mini_svg as minisvg
from examples._shared.paths import out_path_for_script


def make_target(cx: float, cy: float, rings: int) -> list[str]:
	parts: list[str] = []
	for i in range(rings, 0, -1):
		r = i * 18
		if i % 2 == 0:
			fill = minisvg.COLORS.HOT_RED
		else:
			fill = minisvg.COLORS.WHITE
		parts.append(minisvg.circle(cx, cy, r, fill=fill))
	return parts


def main() -> None:
	out = out_path_for_script(__file__)

	w, h = 700, 300
	parts: list[str] = [minisvg.svg_begin(w, h)]

	left = minisvg.group(make_target(200, 150, 6), opacity=0.9)
	right = minisvg.group(make_target(200, 150, 6), transform="translate(300 0) rotate(12 200 150)", opacity=0.9)

	parts.append(left)
	parts.append(right)

	parts.append(minisvg.svg_end())
	minisvg.save_svg(str(out), parts)
	print(out)


if __name__ == "__main__":
	main()

