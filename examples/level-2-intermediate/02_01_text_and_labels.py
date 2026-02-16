# -*- coding: utf-8 -*-
# vim: set filetype=python fileencoding=utf-8 tabstop=3 shiftwidth=3 noexpandtab :
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 hagane
#
"""
02_01_text_and_labels.py

Level 2 (Intermediate): text()

Goal
----
Learn:
- adding labels to shapes
- anchoring text
"""

from __future__ import annotations

import mini_svg as minisvg
from examples._shared.paths import out_path_for_script


def main() -> None:
	out = out_path_for_script(__file__)

	w, h = 700, 250
	parts: list[str] = [minisvg.svg_begin(w, h)]

	parts.append(minisvg.text(w / 2, 40, "mini-svg: text labels", anchor="middle", font_size=22))

	# Three labeled circles
	xs = [150, 350, 550]
	labels = ["A", "B", "C"]

	for x, label in zip(xs, labels):
		parts.append(minisvg.circle(x, 140, 60, fill=minisvg.COLORS.SUNFLOWER))
		parts.append(minisvg.text(x, 150, label, anchor="middle", font_size=32, fill=minisvg.COLORS.BLACK))

	parts.append(minisvg.svg_end())
	minisvg.save_svg(str(out), parts)
	print(out)


if __name__ == "__main__":
	main()

