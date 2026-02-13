"""mini_svg_v3.py — Mini SVG (v3)

v3 = v2 + paths Bézier múltiples (lista de segmentos)
- Importa todo lo de v2 (no repite código)
- Añade bezier_path_cubic()
"""

from __future__ import annotations
from typing import List, Optional, Tuple

# Reexportamos todo lo de v2
from mini_svg_v2 import (  # noqa: F401
    svg_begin, svg_end, save_svg,
    _style,
    line, rect, circle,
    text, group,
    regular_polygon, star,
    cubic_bezier,
)


def bezier_path_cubic(
    start: Tuple[float, float],
    segments: List[Tuple[float, float, float, float, float, float]],
    *,
    closed: bool = False,
    stroke: str = "black",
    stroke_width: int = 2,
    fill: str = "none",
    opacity: Optional[float] = None
) -> str:
    """Ruta Bézier cúbica con varios segmentos.

    start = (x0,y0)
    segments = [(cx1,cy1,cx2,cy2,x,y), ...]
    """
    x0, y0 = start
    d_parts = [f"M {x0:.2f},{y0:.2f}"]
    for (cx1, cy1, cx2, cy2, x, y) in segments:
        d_parts.append(f"C {cx1:.2f},{cy1:.2f} {cx2:.2f},{cy2:.2f} {x:.2f},{y:.2f}")
    if closed:
        d_parts.append("Z")

    d = " ".join(d_parts)
    return f'<path d="{d}"{_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)} />\n'
