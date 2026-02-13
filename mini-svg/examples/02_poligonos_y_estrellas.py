# 02_poligonos_y_estrellas.py
# Ejecuta: python 02_poligonos_y_estrellas.py
# Resultado: 02_poligonos_y_estrellas.svg

from mini_svg import svg_begin, svg_end, save_svg, rect, regular_polygon, star

W, H = 600, 240
parts = [svg_begin(W, H)]
parts.append(rect(0, 0, W, H, fill="white", stroke="none", stroke_width=0))

# Dibujamos polígonos de 3 a 8 lados, cada uno en su “bounding box”
for n in range(3, 9):
    x = 20 + (n - 3) * 70
    bbox = (x, 30, 60, 60)

    # Si es par, rota un poco para que se vean diferentes
    if n % 2 == 0:
        rot = 15
        fill = "gold"
    else:
        rot = 0
        fill = "skyblue"

    parts.append(regular_polygon(n, bbox, rotation_deg=rot, fill=fill, stroke="black", stroke_width=2))

# Estrellas abajo
for k in range(5, 10):
    x = 20 + (k - 5) * 70
    bbox = (x, 130, 60, 60)

    # Condicional para variar “lo puntiaguda”
    if k % 2 == 0:
        inner = 0.45
        fill = "plum"
    else:
        inner = 0.60
        fill = "lightgreen"

    parts.append(star(k, bbox, rotation_deg=0, inner_ratio=inner, fill=fill, stroke="black", stroke_width=2))

parts.append(svg_end())
save_svg("02_poligonos_y_estrellas.svg", parts)
