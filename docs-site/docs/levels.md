# Progressive Levels

mini-svg is structured in three progressive levels.

Each level builds on the previous one.

---

## Level 1 — minisvg_basic

Core SVG primitives:

- svg_begin
- svg_end
- save_svg
- line
- rect
- circle

Example:

```
from mini_svg import minisvg_basic

parts = []
parts.append(minisvg_basic.svg_begin(400, 300))
parts.append(minisvg_basic.circle(200, 150, 60))
parts.append(minisvg_basic.svg_end())

minisvg_basic.save_svg("basic.svg", parts)
```

---

## Level 2 — minisvg_intermediate

Adds:

- text
- group
- regular_polygon
- star
- cubic_bezier

Example:

```
from mini_svg import minisvg_intermediate as svg

parts = []
parts.append(svg.svg_begin(400, 300))
parts.append(svg.star(5, (50, 50, 300, 200)))
parts.append(svg.svg_end())

svg.save_svg("star.svg", parts)
```

---

## Level 3 — minisvg_advanced

Adds:

- bezier_path_cubic

For more advanced Bézier path composition.

Example:

```
from mini_svg import minisvg_advanced as svg

segments = [
   (100, 0, 100, 200, 200, 200),
   (300, 200, 300, 0, 400, 0),
]

parts = []
parts.append(svg.svg_begin(500, 300))
parts.append(svg.bezier_path_cubic((0, 0), segments))
parts.append(svg.svg_end())

svg.save_svg("advanced.svg", parts)
```

