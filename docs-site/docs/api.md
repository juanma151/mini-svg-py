# API Reference (by levels)

This page documents the library by progressive learning levels.

Most users can simply import the flat API:

```
import mini_svg as minisvg
```

For teaching purposes, you can also import explicit levels:

```
from mini_svg import minisvg_basic
from mini_svg import minisvg_intermediate
from mini_svg import minisvg_advanced
```

---

## Level 1 — Basic (minisvg_basic)

Core SVG building blocks:

- svg_begin
- svg_end
- save_svg
- line
- rect
- circle

::: mini_svg.basic
    options:
      show_root_heading: true
      show_source: false
      show_signature: true
      show_signature_annotations: true
      separate_signature: true

---

## Level 2 — Intermediate (minisvg_intermediate)

Builds on Level 1 and adds:

- text
- group
- regular_polygon
- star
- cubic_bezier

::: mini_svg.intermediate
    options:
      show_root_heading: true
      show_source: false
      show_signature: true
      show_signature_annotations: true
      separate_signature: true

---

## Level 3 — Advanced (minisvg_advanced)

Builds on Level 2 and adds:

- bezier_path_cubic

::: mini_svg.advanced
    options:
      show_root_heading: true
      show_source: false
      show_signature: true
      show_signature_annotations: true
      separate_signature: true

