from graphicsWrapper import *


def setup():
    openCanvas(640, 360)


def draw():
    setBackground(0.0)
    drawCircle((mouseX, mouseY), 5.0, color=red)
