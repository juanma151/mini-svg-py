# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
03_01_bezier_path_cubic.py

Level 3 (Advanced): bezier_path_cubic()

Goal
----
Learn:
- lists of segments
- generating multi-curve paths
"""

from __future__ import annotations

import mini_svg as minisvg
from examples._shared.paths import out_path_for_script


def main() -> None:
	out = out_path_for_script(__file__)

	w, h = 800, 300
	parts: list[str] = [minisvg.svg_begin(w, h)]

	parts.append(minisvg.text(w / 2, 30, "Multi-segment cubic Bézier path", anchor="middle", font_size=20))

	start = (80, 150)
	segments = [
		(180, 40, 260, 260, 360, 150),
		(460, 40, 540, 260, 640, 150),
		(700, 120, 740, 180, 760, 150),
	]

	parts.append(
		minisvg.bezier_path_cubic(
			start,
			segments,
			stroke=minisvg.COLORS.BRIGHT_BLUE,
			stroke_width=4,
			fill=minisvg.COLORS.TRANSPARENT,
		)
	)

	parts.append(minisvg.svg_end())
	minisvg.save_svg(str(out), parts)
	print(out)


if __name__ == "__main__":
	main()

