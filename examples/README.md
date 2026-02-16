# Examples

This directory contains executable example scripts for **mini-svg**.

The examples are organized by learning level, matching the structure of the
library:

```
examples/
│
├── level-1-basic/
├── level-2-intermediate/
├── level-3-advanced/
├── _shared/
└── generated_svgs/
```

---

## Structure

### level-1-basic

Introduces the core primitives:

- `svg_begin`
- `svg_end`
- `save_svg`
- `line`
- `rect`
- `circle`

Focus:
- Loops
- Conditionals
- Coordinates
- Simple patterns

---

### level-2-intermediate

Builds on Level 1 and introduces:

- `text`
- `group`
- `regular_polygon`
- `star`
- `cubic_bezier`

Focus:
- Bounding boxes
- Rotation
- Transformations
- Bézier control points

---

### level-3-advanced

Adds:

- `bezier_path_cubic`

Focus:
- Lists of segments
- Multi-curve paths
- Structured geometry generation

---

### _shared

Internal utilities used by the examples.

Not part of the public API.

---

### generated_svgs

All example scripts write their output here.

Each script generates an SVG file with the same name as the script.

Example:

```
02_03_polygons_and_stars.py
```

produces:

```
generated_svgs/02_03_polygons_and_stars.svg
```

---

## Running an Example

From the project root:

```
python examples/level-1-basic/01_01_lines.py
```

Then open the generated SVG:

```
examples/generated_svgs/01_01_lines.svg
```

You can open SVG files with:

- A web browser
- Inkscape
- Any vector graphics editor

---

## Educational Intention

These examples are intentionally:

- Small
- Explicit
- Readable
- Loop-driven

The goal is not abstraction — the goal is clarity.

Students should be able to:

- Modify parameters
- Change loop ranges
- Experiment with conditionals
- Produce visual results immediately

---

## Suggested Workflow for Students

1. Run an example.
2. Open the generated SVG.
3. Modify one value.
4. Re-run.
5. Observe the change.

Visual feedback is the fastest way to learn programming.

---

## Notes

All examples use the flat import style:

```
import mini_svg as minisvg
```

Style defaults and colors come from the public API.

Output files are overwritten on each run.

