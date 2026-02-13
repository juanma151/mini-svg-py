import svgwrite
import math

dwg = svgwrite.Drawing("espiral.svg", size=("400px", "400px"))

centro_x = 200
centro_y = 200
radio = 5

for i in range(60):
    angulo = i * 10
    x = centro_x + radio * math.cos(math.radians(angulo))
    y = centro_y + radio * math.sin(math.radians(angulo))

    if i % 2 == 0:
        color = "blue"
    else:
        color = "purple"

    dwg.add(dwg.circle(center=(x, y), r=3, fill=color))
    radio += 2

dwg.save()