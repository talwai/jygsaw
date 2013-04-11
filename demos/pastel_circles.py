# pastel_circles.py
#
# Jygsaw demo - draws a cascade of pastel circles
#
# Written by Devin Balkcom

from jygsaw.graphics import *
from random import randint

canvas()
background(black)

while True:

    # clear screen with nearly-transparent black rectangle
    fill(0, 0, 0, 15)
    rect(0, 0, 399, 399)

    # random location for circle
    x = randint(0, 400)
    y = randint(0, 400)

    # random color for circle
    r = randint(128, 255)
    g = randint(128, 255)
    b = randint(128, 255)

    fill(r, g, b)
    circle(x, y, 50)

    refresh(.02)
