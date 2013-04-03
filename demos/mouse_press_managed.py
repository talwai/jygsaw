from jygsaw.graphics import *

canvas(640, 360)
fill(126)  # line color is set by stroke?
background(102)
LINELENGTH = 66


def pressed():
    fill(white)


def released():
    fill(black)


def draw():
    global LINELENGTH
    clear()

    line(mouseX() - LINELENGTH, mouseY(), mouseX() + LINELENGTH, mouseY())
    line(mouseX(), mouseY() - LINELENGTH, mouseX(), mouseY() + LINELENGTH)

onMousePress(pressed)
onMouseRelease(released)
onDraw(draw)

fill(black)
jygsawMain(1.0 / 30)
