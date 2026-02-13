# 01_basico_patron.py
# Ejecuta: python 01_basico_patron.py
# Resultado: 01_basico_patron.svg (ábrelo en Inkscape)

from mini_svg import svg_begin, svg_end, save_svg, circle, rect

W, H = 420, 200
parts = [svg_begin(W, H)]

# Fondo
parts.append(rect(0, 0, W, H, fill="white", stroke="none", stroke_width=0))

# Fila de círculos con colores alternos (bucle + condicional)
for i in range(10):
    x = 30 + i * 38

    if i % 2 == 0:
        color = "red"
    else:
        color = "green"

    parts.append(circle(x, 100, 15, fill=color, stroke="black", stroke_width=2))

parts.append(svg_end())
save_svg("01_basico_patron.svg", parts)
