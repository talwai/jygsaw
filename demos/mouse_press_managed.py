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
    stroke(white)


def released():
    stroke(black)


def draw():
    global LINELENGTH
    clear()

    line(mouseX() - LINELENGTH, mouseY(), mouseX() + LINELENGTH, mouseY())
    line(mouseX(), mouseY() - LINELENGTH, mouseX(), mouseY() + LINELENGTH)

onMousePress(pressed)
onMouseRelease(released)
onDraw(draw)

stroke(black)
jygsawMain(1.0 / 30)
