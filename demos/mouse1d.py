import sys
import os
sys.path.append(os.path.pardir + "/lib")
from jygsaw import *

canvas(640, 360)
background(black)
loop()


def draw():
    clear()
    circle(mouseX(), mouseY(), 5, color=red)

onDraw(draw)
