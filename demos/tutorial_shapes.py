# tutorial_shapes.py
#
# Jygsaw demo - draws some shapes
#
# Written by Janet Kim for Jygsaw

from jygsaw.graphics import *

canvas(700, 300)
background(blue)


def draw():
    circle(350, 150, 50, color=red)
    point(350, 150)
    rect(0, 0, 150, 75, color=orange)
    polygon([(450, 250), (650, 250), (500, 300)], color=yellow)
    ellipse(150, 75, 100, 250, color=green)
    regPolygon(550, 85, sides=6, length=80, color=magenta)

onDraw(draw)
jygsawMain()
