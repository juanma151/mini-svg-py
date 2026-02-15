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


    # 02) Cuadrícula tipo “bandera” (doble bucle + condicional)
    W, H = 420, 160
    size = 20
    parts = [svg_begin(W, H)]

    for fila in range(6):
        for col in range(21):
            x = col * size
            y = fila * size

            if (fila + col) % 2 == 0:
                color = "navy"
            else:
                color = "gold"

            parts.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{color}" />\n')

    parts.append(svg_end())
    save_svg("02_cuadricula_bandera.svg", parts)
