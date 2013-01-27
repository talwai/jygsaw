from graphicsWrapper import *


def setup():
    size(640, 360)


def draw():
    background(0.0)
    drawCircle((mouseX, mouseY), 5.0, color=red)
