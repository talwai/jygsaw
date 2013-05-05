# tutorial_shapes.py
#
# Jygsaw demo - draws some shapes
#
# Written by Janet Kim for Jygsaw

from jygsaw.graphics import *

canvas(700, 300)
background(BLUE)


def draw():
    circle(350, 150, 50, color=RED)
    point(350, 150)
    rect(0, 0, 150, 75, color=ORANGE)
    polygon([(450, 250), (650, 250), (500, 300)], color=YELLOW)
    ellipse(150, 75, 100, 250, color=GREEN)
    reg_polygon(550, 85, sides=6, length=80, color=MAGENTA)

on_draw(draw)
jygsaw_start()
