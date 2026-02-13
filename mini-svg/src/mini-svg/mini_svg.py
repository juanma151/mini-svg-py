"""mini_svg.py — FACHADA/ATAJO (compatibilidad)

Este archivo existe para que quien ya hacía:
    import mini_svg
siga funcionando.

Por defecto, expone TODO lo de v3 (que incluye v1 + v2 + v3).
"""

from mini_svg_v3 import *  # noqa: F401,F403
