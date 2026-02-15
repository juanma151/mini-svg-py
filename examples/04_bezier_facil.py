# 04_bezier_facil.py
# Ejecuta: python 04_bezier_facil.py
# Resultado: 04_bezier_facil.svg
#
# Una curva de Bézier cúbica se define con 4 puntos:
#   Inicio, Control1, Control2, Final
#
# En Inkscape los “manejadores” que tiras con el ratón son justo esos puntos de control.

from mini_svg import svg_begin, svg_end, save_svg, rect, circle, line, cubic_bezier

W, H = 600, 260
parts = [svg_begin(W, H)]
parts.append(rect(0, 0, W, H, fill="white", stroke="none", stroke_width=0))

# Puntos (para entenderla visualmente)
P0 = (80, 200)
C1 = (200, 40)
C2 = (400, 240)
P3 = (520, 80)

# Dibujamos “hilos” para ver la estructura
parts.append(line(P0[0], P0[1], C1[0], C1[1], stroke="gray", stroke_width=1, opacity=0.6))
parts.append(line(P3[0], P3[1], C2[0], C2[1], stroke="gray", stroke_width=1, opacity=0.6))

# Puntos
for (x,y), col in [(P0,"red"), (C1,"orange"), (C2,"orange"), (P3,"red")]:
    parts.append(circle(x, y, 6, fill=col, stroke="black", stroke_width=1))

# Curva
parts.append(cubic_bezier(P0[0],P0[1], C1[0],C1[1], C2[0],C2[1], P3[0],P3[1],
                          stroke="black", stroke_width=4, fill="none"))

parts.append(svg_end())
save_svg("04_bezier_facil.svg", parts)
