# mouse_press_direct.py
#
# Jygsaw demo - paints a cross-hair centered at the mouse cursor
#               and can change color
#
# Attribution: inspired by the mousepress demo in Processing
# from http://processingjs.org/learning/basic/mousepress/
# written by Casey Reas and Ben Fry

from jygsaw.graphics import *

canvas(640, 360)
background(102)
LINELENGTH = 66


def pressed():
    stroke(WHITE)


def released():
    stroke(BLACK)

on_mouse_press(pressed)
on_mouse_release(released)
stroke(BLACK)

while True:
    clear()
    line(mouse_x() - LINELENGTH, mouse_y(), mouse_x() + LINELENGTH, mouse_y())
    line(mouse_x(), mouse_y() - LINELENGTH, mouse_x(), mouse_y() + LINELENGTH)
    refresh(1.0 / 30)
