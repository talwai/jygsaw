# mouse_press_direct.py
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
    print "Pressed!"
    stroke(white)


def released():
    print "Released!"
    stroke(black)

onMousePress(pressed)
onMouseRelease(released)
stroke(black)

while True:
    clear()
    line(mouseX() - LINELENGTH, mouseY(), mouseX() + LINELENGTH, mouseY())
    line(mouseX(), mouseY() - LINELENGTH, mouseX(), mouseY() + LINELENGTH)
    refresh(1.0 / 30)
