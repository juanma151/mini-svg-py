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

    # 05) “Fractal” por niveles (sin recursión): capas de radios
    W = H = 500
    cx = cy = 250
    parts = [svg_begin(W, H)]

    for nivel in range(4):
        tamaño = 200 - nivel * 45
        opacidad = 0.25 + 0.15 * nivel

        for i in range(12):
            ang = i * 30 + (nivel * 10)
            x = cx + tamaño * math.cos(math.radians(ang))
            y = cy + tamaño * math.sin(math.radians(ang))

            parts.append(
                f'<line x1="{cx}" y1="{cy}" x2="{x:.2f}" y2="{y:.2f}" '
                f'stroke="black" stroke-opacity="{opacidad:.2f}" stroke-width="1"/>\n'
            )

    parts.append(svg_end())
    save_svg("05_fractal_por_niveles.svg", parts)
