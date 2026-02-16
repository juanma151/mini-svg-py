# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
02_04_cubic_bezier.py

Level 2 (Intermediate): cubic_bezier()

Goal
----
Learn:
- Bézier control points
- using a curve as an SVG path
"""

from __future__ import annotations

import mini_svg as minisvg
from examples._shared.paths import out_path_for_script


def main() -> None:
	out = out_path_for_script(__file__)

	w, h = 800, 300
	parts: list[str] = [minisvg.svg_begin(w, h)]

	parts.append(minisvg.text(w / 2, 30, "Cubic Bézier curve", anchor="middle", font_size=20))

	# Curve points
	x0, y0 = 100, 200
	cx1, cy1 = 250, 50
	cx2, cy2 = 550, 250
	x, y = 700, 100

	# Draw helper lines
	parts.append(minisvg.line(x0, y0, cx1, cy1, stroke=minisvg.COLORS.LIGHT_GRAY))
	parts.append(minisvg.line(x, y, cx2, cy2, stroke=minisvg.COLORS.LIGHT_GRAY))

	# Draw control points as small circles
	for (px, py) in [(x0, y0), (cx1, cy1), (cx2, cy2), (x, y)]:
		parts.append(minisvg.circle(px, py, 6, fill=minisvg.COLORS.SUNFLOWER))

	# Draw the curve
	parts.append(minisvg.cubic_bezier(x0, y0, cx1, cy1, cx2, cy2, x, y, stroke=minisvg.COLORS.DARK_GRAY, stroke_width=3, fill=minisvg.COLORS.TRANSPARENT))

	parts.append(minisvg.svg_end())
	minisvg.save_svg(str(out), parts)
	print(out)


if __name__ == "__main__":
	main()

