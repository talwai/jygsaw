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
