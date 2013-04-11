# mouse2d.py
#
# Jygsaw demo - A ball follows the mouse cursor.

from jygsaw.graphics import *

canvas(640, 360)
background(black)


def draw():
    clear()
    circle(mouseX(), mouseY(), 5, color=red)

onDraw(draw)
jygsawMain(1.0 / 30)
