    # Mini "librería" SVG sin dependencias (1º ESO friendly)
# Genera un SVG como texto y lo guarda en un .svg para abrirlo en Inkscape.

def svg_begin(w, h):
    return f'<?xml version="1.0" encoding="UTF-8"?>\n' \
           f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">\n'

def svg_end():
    return '</svg>\n'

def save_svg(filename, parts):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(parts))

    import math

    # 03) Espiral (bucle + crecimiento + condicional)
    W = H = 500
    cx = cy = 250
    radio = 2.0
    parts = [svg_begin(W, H)]

    for i in range(200):
        angulo = i * 10
        x = cx + radio * math.cos(math.radians(angulo))
        y = cy + radio * math.sin(math.radians(angulo))

        if i % 5 == 0:
            color = "gold"
        else:
            color = "purple"

        parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2" fill="{color}" />\n')
        radio += 0.8

    parts.append(svg_end())
    save_svg("03_espiral_avanzada.svg", parts)
