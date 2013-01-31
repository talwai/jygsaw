from graphicsWrapper import *


canvas(640, 360)


def draw():
    background(0.0)
    circle((mouseX(), mouseY()), 5.0, color=red)

drawFunction(draw)
