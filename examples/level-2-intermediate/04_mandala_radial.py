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

    # 04) Mandala radial (bucle angular + condicional)
    W = H = 500
    cx = cy = 250
    R = 200
    parts = [svg_begin(W, H)]
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="black" stroke-width="2"/>\n')

    for i in range(36):
        ang = i * 10
        x = cx + R * math.cos(math.radians(ang))
        y = cy + R * math.sin(math.radians(ang))

        if i % 2 == 0:
            color = "black"
        else:
            color = "gray"

        parts.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.2f}" y2="{y:.2f}" stroke="{color}" stroke-width="1"/>\n')

    parts.append(svg_end())
    save_svg("04_mandala_radial.svg", parts)
