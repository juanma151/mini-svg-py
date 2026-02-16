# mini-svg

**mini-svg** is a lightweight educational Python library for generating SVG graphics using simple programming constructs.

It is designed for classrooms and beginner-friendly workshops where students can:

- write Python code,
- generate an `.svg` file,
- open it in Inkscape,
- and immediately see the visual result.

Repository: https://github.com/juanma151/mini-svg

Documentation: https://juanma151.github.io/mini-svg/ 

---

## Why SVG?

SVG is a standard vector format:

- readable as text,
- editable in tools like Inkscape,
- ideal for “code → visual output” feedback loops.

Small code changes produce immediate visual differences, which makes it perfect for teaching programming concepts.

---

## Features

- Zero dependencies (Python standard library only)
- Progressive learning levels
- Flat API for simplicity
- Explicit modular API for classroom restriction
- Clean packaging (pyproject-based)
- Version read dynamically from package metadata

---

## Installation (recommended)

### Using `venv` + `pip`

Create a virtual environment:

```
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -U pip
pip install -e .
```

Test the installation:

```
python -c "import mini_svg as minisvg; print(minisvg.__version__)"
```

---

## Alternative: using pipenv

If you prefer pipenv:

```
pipenv install -e .
pipenv shell
```

This is optional. The project does not require pipenv.

---

## Quick Start (Flat API — Recommended)

The simplest way to use the library:

```
import mini_svg as minisvg

parts = [minisvg.svg_begin(400, 300)]
parts.append(minisvg.circle(200, 150, 80, fill="red"))
parts.append(minisvg.svg_end())

minisvg.save_svg("demo.svg", parts)
```

Open `demo.svg` in Inkscape.

This flat API exposes the full (advanced) feature set.

---

## Progressive Levels (Classroom Mode)

If you want to restrict students to a specific level, import one of:

- `minisvg_basic`
- `minisvg_intermediate`
- `minisvg_advanced`

---

### Level 1 — minisvg_basic

Includes:

- `svg_begin()`
- `svg_end()`
- `save_svg()`
- `line()`
- `rect()`
- `circle()`

Example:

```
from mini_svg import minisvg_basic

parts = [minisvg_basic.svg_begin(400, 300)]
parts.append(minisvg_basic.circle(200, 150, 80))
parts.append(minisvg_basic.svg_end())

minisvg_basic.save_svg("basic.svg", parts)
```

Recommended for beginners learning:

- Functions
- Parameters
- Simple geometry
- File writing

---

### Level 2 — minisvg_intermediate

Includes everything from Level 1, plus:

- `text()`
- `group()`
- `regular_polygon()`
- `star()`
- `cubic_bezier()`

Example:

```
from mini_svg import minisvg_intermediate

parts = [minisvg_intermediate.svg_begin(500, 300)]
parts.append(minisvg_intermediate.star(5, (150, 50, 200, 200), fill="gold"))
parts.append(minisvg_intermediate.text(20, 30, "Hello SVG!", font_size=24))
parts.append(minisvg_intermediate.svg_end())

minisvg_intermediate.save_svg("intermediate.svg", parts)
```

Recommended for students comfortable with:

- Loops
- Math functions
- Coordinate transformations

---

### Level 3 — minisvg_advanced

Includes everything from Level 2, plus:

- `bezier_path_cubic()`

Example:

```
from mini_svg import minisvg_advanced

parts = [minisvg_advanced.svg_begin(600, 300)]

start = (50, 150)
segments = [
    (150, 50, 250, 250, 350, 150),
    (400, 100, 500, 200, 550, 150),
]

parts.append(minisvg_advanced.bezier_path_cubic(start, segments, stroke="black", stroke_width=3))
parts.append(minisvg_advanced.svg_end())

minisvg_advanced.save_svg("advanced.svg", parts)
```

Recommended for advanced students working with:

- Lists of tuples
- Structured data
- SVG `<path>` syntax

---

## Running the examples

The repository includes example scripts under:

```
examples/
```

Run one:

```
python examples/02_poligonos_y_estrellas.py
```

Generated SVG files may appear in:

```
examples/svgs_generados/
```

---

## Project Structure

```
.
├── README.md
├── pyproject.toml
├── examples/
└── mini_svg/
    ├── __init__.py
    ├── basic.py
    ├── intermediate.py
    └── advanced.py
```

---

## Development

Install development tools:

```
pip install -e ".[dev]"
```

Optional tools defined in `pyproject.toml`:

- pytest
- ruff
- black
- mypy
- build
- twine

---

## Versioning

The package version is defined in `pyproject.toml` and read dynamically via `importlib.metadata`.

Tags follow semantic versioning:

```
v0.1.0
```

---

## Contributing

Issues and pull requests are welcome:

- Issues: https://github.com/juanma151/mini-svg/issues
- Repository: https://github.com/juanma151/mini-svg

Suggested contributions:

- More classroom examples (fractals, spirals, mosaics)
- Additional documentation
- Optional turtle-style abstraction layer

---

## License

MIT.

Make sure a `LICENSE` file is included before publishing to PyPI.

