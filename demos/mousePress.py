import sys
import os
sys.path.append(os.path.pardir + "/lib")
from graphicsWrapper import *

canvas(640, 360)
fillColor(126)
background(102)


def draw():
    if (mousePressed()):
        strokeColor(255)
    else:
        strokeColor(0)

    line((mouseX() - 66, mouseY()), (mouseX() + 66, mouseY()))
    line((mouseX(), mouseY() - 66), (mouseX(), mouseY() + 66))

drawFunction(draw)
