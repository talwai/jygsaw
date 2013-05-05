# mouse2d.py
#
# Jygsaw demo - A ball follows the mouse cursor.

from jygsaw.graphics import *

canvas(640, 360)
background(BLACK)


def draw():
    clear()
    circle(mouse_x(), mouse_y(), 5, color=RED)

on_draw(draw)
jygsaw_start(1.0 / 30)
