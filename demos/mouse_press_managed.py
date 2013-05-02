# mouse_press_managed.py
#
# Jygsaw demo - prints a cross-hair centered at the mouse cursor
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


def draw():
    global LINELENGTH
    clear()

    line(mouse_x() - LINELENGTH, mouse_y(), mouse_x() + LINELENGTH, mouse_y())
    line(mouse_x(), mouse_y() - LINELENGTH, mouse_x(), mouse_y() + LINELENGTH)

on_mouse_press(pressed)
on_mouse_release(released)
on_draw(draw)

stroke(BLACK)
jygsaw_start(1.0 / 30)
