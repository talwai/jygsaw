# mouse2d.py
#
# Jygsaw demo - A ball follows the mouse cursor.

from jygsaw.graphics import *

canvas(640, 360)
background(BLACK)


while True:
    clear()
    circle(mouse_x(), mouse_y(), 5, color=RED)
    refresh(1.0 / 30)
