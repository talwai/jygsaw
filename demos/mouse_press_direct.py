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
