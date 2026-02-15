# Examples

This page presents classroom-oriented examples built with **mini-svg**.

Each example focuses on a specific programming concept and geometric idea.

Full source code can be found in the `examples/` directory of the repository.

---

## 1. Alternating Circles (Loops)

Concepts practiced:

- for loops
- arithmetic progression
- color alternation using conditionals

```
import mini_svg as minisvg

parts = []
parts.append(minisvg.svg_begin(400, 200))

for i in range(10):
    color = "red" if i % 2 == 0 else "blue"
    parts.append(minisvg.circle(40 + i*35, 100, 15, fill=color))

parts.append(minisvg.svg_end())
minisvg.save_svg("alternating.svg", parts)
```

This example demonstrates how geometry can emerge from simple iteration.

---

## 2. Regular Polygon (Geometry)

Concepts practiced:

- polar coordinates
- division of 360 degrees
- parametric thinking

```
from mini_svg import minisvg_intermediate as svg

parts = []
parts.append(svg.svg_begin(300, 300))
parts.append(svg.regular_polygon(6, (50, 50, 200, 200)))
parts.append(svg.svg_end())

svg.save_svg("hexagon.svg", parts)
```

Students can experiment by changing:

- Number of sides
- Bounding box
- Rotation

---

## 3. Star Pattern (Nested Loops)

Concepts practiced:

- geometric repetition
- nested loops
- transformations

```
from mini_svg import minisvg_intermediate as svg

parts = []
parts.append(svg.svg_begin(400, 400))

for i in range(12):
    parts.append(
        svg.star(
            5,
            (100, 100, 200, 200),
            rotation_deg=i * 30
        )
    )

parts.append(svg.svg_end())
svg.save_svg("radial_star.svg", parts)
```

This example shows how rotation inside a loop produces radial symmetry.

---

## 4. Simple Bézier Curve

Concepts practiced:

- control points
- curve shape manipulation
- visual experimentation

```
from mini_svg import minisvg_intermediate as svg

parts = []
parts.append(svg.svg_begin(400, 200))

parts.append(
    svg.cubic_bezier(
        20, 100,
        120, 0,
        280, 200,
        380, 100
    )
)

parts.append(svg.svg_end())
svg.save_svg("curve.svg", parts)
```

Encourage students to move control points and observe how the curve changes.

---

## 5. Multi-Segment Path (Advanced)

Concepts practiced:

- structured data (lists of tuples)
- iterative geometry
- abstraction

```
from mini_svg import minisvg_advanced as svg

segments = [
    (80, 0, 120, 200, 200, 200),
    (280, 200, 320, 0, 400, 0),
]

parts = []
parts.append(svg.svg_begin(450, 250))
parts.append(svg.bezier_path_cubic((0, 0), segments))
parts.append(svg.svg_end())

svg.save_svg("path.svg", parts)
```

This introduces structured geometric definitions and iterative path construction.

---

# Teaching Strategy

The examples are intentionally progressive:

- Basic level → primitives
- Intermediate → geometric reasoning
- Advanced → structured curve composition

Encourage experimentation by changing:

- Loop ranges
- Rotation angles
- Colors
- Bounding boxes
- Control points

Visual feedback reinforces computational thinking.

