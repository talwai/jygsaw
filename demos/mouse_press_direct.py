from jygsaw.graphics import *

canvas(640, 360)
fill(126)  # line color is set by stroke?
background(102)
LINELENGTH = 66


def pressed():
    fill(white)


def released():
    fill(black)

onMousePress(pressed)
onMouseRelease(released)
fill(black)

while True:
    clear()
    line(mouseX() - LINELENGTH, mouseY(), mouseX() + LINELENGTH, mouseY())
    line(mouseX(), mouseY() - LINELENGTH, mouseX(), mouseY() + LINELENGTH)
    refresh(1.0 / 30)
