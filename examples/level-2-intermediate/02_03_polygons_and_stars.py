# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
02_03_polygons_and_stars.py

Level 2 (Intermediate): regular_polygon(), star()

Goal
----
Learn:
- bounding boxes
- rotation
- parameters that control geometry
"""

from __future__ import annotations

import mini_svg as minisvg
from examples._shared.paths import out_path_for_script


def main() -> None:
	out = out_path_for_script(__file__)

	w, h = 800, 320
	parts: list[str] = [minisvg.svg_begin(w, h)]

	parts.append(minisvg.text(w / 2, 30, "Polygons and Stars (bounding boxes)", anchor="middle", font_size=20))

	boxes = [
		(40, 70, 160, 160),
		(240, 70, 160, 160),
		(440, 70, 160, 160),
		(640, 70, 160, 160),
	]

	# Draw bounding boxes lightly
	for (x, y, bw, bh) in boxes:
		parts.append(minisvg.rect(x, y, bw, bh, stroke=minisvg.COLORS.LIGHT_GRAY, fill=minisvg.COLORS.TRANSPARENT))

	parts.append(minisvg.regular_polygon(3, boxes[0], fill=minisvg.COLORS.SUNFLOWER, rotation_deg=0))
	parts.append(minisvg.regular_polygon(6, boxes[1], fill=minisvg.COLORS.EMERALD, rotation_deg=30))
	parts.append(minisvg.star(5, boxes[2], fill=minisvg.COLORS.BRIGHT_BLUE, rotation_deg=0, inner_ratio=0.5))
	parts.append(minisvg.star(8, boxes[3], fill=minisvg.COLORS.MAGENTA, rotation_deg=20, inner_ratio=0.35))

	parts.append(minisvg.svg_end())
	minisvg.save_svg(str(out), parts)
	print(out)


if __name__ == "__main__":
	main()

