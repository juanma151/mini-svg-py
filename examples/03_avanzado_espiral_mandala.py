# 03_avanzado_espiral_mandala.py
# Ejecuta: python 03_avanzado_espiral_mandala.py
# Resultado: 03_avanzado_espiral_mandala.svg

import math
from mini_svg import svg_begin, svg_end, save_svg, rect, circle, line

W = H = 600
cx = cy = 300
parts = [svg_begin(W, H)]
parts.append(rect(0, 0, W, H, fill="white", stroke="none", stroke_width=0))

# Espiral de puntos (bucle + crecimiento + condicional)
radio = 2.0
for i in range(240):
    ang = i * 12
    x = cx + radio * math.cos(math.radians(ang))
    y = cy + radio * math.sin(math.radians(ang))

    if i % 6 == 0:
        color = "gold"
        r = 3
    else:
        color = "purple"
        r = 2

    parts.append(circle(x, y, r, fill=color, stroke="none", stroke_width=0, opacity=0.9))
    radio += 0.9

# Mandala: líneas radiales encima (simetría)
for i in range(48):
    ang = i * (360/48)
    x2 = cx + 250 * math.cos(math.radians(ang))
    y2 = cy + 250 * math.sin(math.radians(ang))

    if i % 3 == 0:
        op = 0.35
    else:
        op = 0.18

    parts.append(line(cx, cy, x2, y2, stroke="black", stroke_width=1, opacity=op))

parts.append(svg_end())
save_svg("03_avanzado_espiral_mandala.svg", parts)
