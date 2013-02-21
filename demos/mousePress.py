import sys
import os
sys.path.append(os.path.pardir + "/lib")
from jygsaw import *

canvas(640, 360)
fill(126)  # line color is set by stroke?
background(102)
loop()


def draw():
    if (mousePressed()):
        fill(white)
    else:
        fill(black)

    line(mouseX() - 66, mouseY(), mouseX() + 66, mouseY())
    line(mouseX(), mouseY() - 66, mouseX(), mouseY() + 66)

onDraw(draw)
