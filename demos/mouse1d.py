import sys
import os
sys.path.append(os.path.pardir + "/lib")
from graphicsWrapper import *


canvas(640, 360)
loop()


def draw():
    background(black)
    circle(mouseX(), mouseY(), 5, color=red)
    print (mouseX(), mouseY())

onDraw(draw)
