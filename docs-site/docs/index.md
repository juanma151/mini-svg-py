# mini-svg

mini-svg is a lightweight educational Python library for generating SVG graphics using simple programming constructs.

It is designed for teaching:

- loops
- conditionals
- geometric reasoning
- progressive abstraction

The library exposes a **flat API**:

```
import mini_svg as minisvg
```

---

## Quick Start

```
import mini_svg as minisvg

parts = []
parts.append(minisvg.svg_begin(400, 300))
parts.append(minisvg.circle(200, 150, 80, fill="red"))
parts.append(minisvg.svg_end())

minisvg.save_svg("demo.svg", parts)
```

Open `demo.svg` in Inkscape.

---

## Philosophy

mini-svg is intentionally:

- minimal
- readable
- explicit
- educational

The goal is not performance, but clarity.

