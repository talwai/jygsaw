# tutorial_points_lines_direct.py
#
# Jysaw demo - draws an animation of points and lines
# shooting from the bottom center of the screen.
#
# Written by Janet Kim for Jygsaw

from jygsaw.graphics import *
from random import random, choice

canvas(900, 500)
background(DARK_GRAY)


while True:
    lineX = random() * 800 + 50
    lineY = random() * 300 + 125
    lineColor = choice([LIGHT_GRAY, WHITE, ORANGE, GRAY])
    stroke(lineColor)
    line(width() / 2, height(), lineX, lineY)
    point(lineX, lineY - 100)
    refresh(0.1)
