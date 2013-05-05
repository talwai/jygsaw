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
    line_x = random() * 800 + 50
    line_y = random() * 300 + 125
    line_color = choice([LIGHT_GRAY, WHITE, ORANGE, GRAY])
    stroke(line_color)
    line(width() / 2, height(), line_x, line_y)
    point(line_x, line_y - 100)
    refresh(0.1)
