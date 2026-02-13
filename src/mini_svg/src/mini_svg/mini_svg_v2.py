"""mini_svg_v2.py — Mini SVG (v2)

v2 = v1 + “figuras inteligentes” + texto/grupos + Bézier simple

Importante:
  - NO repite el código de v1: lo importa y reexporta.
  - Añade:
      - text(), group()
      - regular_polygon(), star()  (bbox + rotación)
      - cubic_bezier()             (1 curva)
"""

from __future__ import annotations
import math
from typing import List, Optional, Tuple

# Reexportamos todo lo de v1 (sin duplicar código)
from mini_svg_v1 import (  # noqa: F401
    svg_begin, svg_end, save_svg,
    _style,
    line, rect, circle,
)


def text(
    x: float, y: float, content: str,
    *, font_size: int = 16, fill: str = "black",
    font_family: str = "sans-serif", anchor: str = "start",
    opacity: Optional[float] = None
) -> str:
    """Dibuja texto SVG. anchor: start | middle | end"""
    op = f' opacity="{opacity}"' if opacity is not None else ""
    safe = (
        content.replace("&", "&amp;")
               .replace("<", "&lt;")
               .replace(">", "&gt;")
    )
    return (
        f'<text x="{x}" y="{y}" font-size="{font_size}" fill="{fill}" '
        f'font-family="{font_family}" text-anchor="{anchor}"{op}>{safe}</text>\n'
    )


def group(elements: List[str], *, transform: Optional[str] = None, opacity: Optional[float] = None) -> str:
    """Agrupa elementos en <g>. Útil para “capas” y transformaciones."""
    t = f' transform="{transform}"' if transform else ""
    op = f' opacity="{opacity}"' if opacity is not None else ""
    return f"<g{t}{op}>\n" + "".join(elements) + "</g>\n"


# --- Coordenadas polares -> cartesianas (para polígonos/estrellas) ---

def _polar_to_xy(cx: float, cy: float, radius: float, angle_deg: float) -> Tuple[float, float]:
    a = math.radians(angle_deg)
    return cx + radius * math.cos(a), cy + radius * math.sin(a)


def regular_polygon(
    n_sides: int, bbox: Tuple[float, float, float, float], rotation_deg: float = 0.0,
    *, stroke: str = "black", stroke_width: int = 2, fill: str = "none", opacity: Optional[float] = None
) -> str:
    """Polígono regular (n lados) dentro de bbox=(x,y,w,h), con rotación."""
    if n_sides < 3:
        raise ValueError("n_sides debe ser >= 3")

    x, y, w, h = bbox
    cx, cy = x + w / 2, y + h / 2
    r = min(w, h) / 2

    start = -90.0 + rotation_deg
    step = 360.0 / n_sides

    pts = []
    for i in range(n_sides):
        px, py = _polar_to_xy(cx, cy, r, start + i * step)
        pts.append(f"{px:.2f},{py:.2f}")

    return f'<polygon points="{" ".join(pts)}"{_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)} />\n'


def star(
    n_points: int, bbox: Tuple[float, float, float, float], rotation_deg: float = 0.0, inner_ratio: float = 0.5,
    *, stroke: str = "black", stroke_width: int = 2, fill: str = "none", opacity: Optional[float] = None
) -> str:
    """Estrella de n puntas dentro de bbox, con rotación.

    inner_ratio controla lo “profunda” que es (0.1 muy puntiaguda, 0.8 más gorda).
    """
    if n_points < 3:
        raise ValueError("n_points debe ser >= 3")
    if not (0.05 <= inner_ratio <= 0.95):
        raise ValueError("inner_ratio debería estar entre 0.05 y 0.95")

    x, y, w, h = bbox
    cx, cy = x + w / 2, y + h / 2
    r_outer = min(w, h) / 2
    r_inner = r_outer * inner_ratio

    start = -90.0 + rotation_deg
    step = 360.0 / (n_points * 2)

    pts = []
    for i in range(n_points * 2):
        r = r_outer if i % 2 == 0 else r_inner
        px, py = _polar_to_xy(cx, cy, r, start + i * step)
        pts.append(f"{px:.2f},{py:.2f}")

    return f'<polygon points="{" ".join(pts)}"{_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)} />\n'


def cubic_bezier(
    x0: float, y0: float,
    x1: float, y1: float,
    x2: float, y2: float,
    x3: float, y3: float,
    *, stroke: str = "black", stroke_width: int = 2, fill: str = "none", opacity: Optional[float] = None
) -> str:
    """Una curva cúbica de Bézier (un solo segmento).

    P0 inicio, C1 control, C2 control, P3 final.
    """
    d = f"M {x0:.2f},{y0:.2f} C {x1:.2f},{y1:.2f} {x2:.2f},{y2:.2f} {x3:.2f},{y3:.2f}"
    return f'<path d="{d}"{_style(stroke=stroke, stroke_width=stroke_width, fill=fill, opacity=opacity)} />\n'
