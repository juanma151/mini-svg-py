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


    # 01) Círculos alternos (bucle + condicional)
    W, H = 400, 200
    parts = [svg_begin(W, H)]

    for i in range(10):
        x = 20 + i * 35

        if i % 2 == 0:
            color = "red"
        else:
            color = "green"

        parts.append(f'<circle cx="{x}" cy="100" r="15" fill="{color}" />\n')

    parts.append(svg_end())
    save_svg("01_circulos_alternos.svg", parts)
