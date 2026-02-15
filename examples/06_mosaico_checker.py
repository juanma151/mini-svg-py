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


    # 06) Mosaico “checker” (doble bucle + condicional)
    W = H = 400
    cell = 20
    parts = [svg_begin(W, H)]

    for fila in range(20):
        for col in range(20):
            x = col * cell
            y = fila * cell

            if (fila + col) % 2 == 0:
                color = "black"
            else:
                color = "white"

            parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{color}" />\n')

    parts.append(svg_end())
    save_svg("06_mosaico_checker.svg", parts)
