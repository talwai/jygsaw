# tutorial_points_lines.py
#
# Jysaw demo - draws an animation of points and lines
# shooting from the bottom center of the screen.
#
# Written by Janet Kim for Jygsaw

from jygsaw.graphics import *
from random import random, choice

canvas(900, 500)
background(DARK_GRAY)


def draw():
    lineX = random() * 800 + 50
    lineY = random() * 300 + 125
    line_color = choice([LIGHT_GRAY, WHITE, ORANGE, GRAY])
    stroke(line_color)
    line(width() / 2, height(), lineX, lineY)
    point(lineX, lineY - 100)

on_draw(draw)

jygsaw_start(0.1)
