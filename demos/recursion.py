from GraphicsWrapper import *


def draw():
    drawCircle(width / 2, 280, 6)


# Recursively draw smaller circles
def drawCircle(x, radius, level):
    tt = 126 * level / 4.0
    fillColor(tt)
    ellipse(x, height / 2, radius * 2, radius * 2)
    if (level > 1):
        level = level - 1
        drawCircle(x - radius / 2, radius / 2, level)
        drawCircle(x + radius / 2, radius / 2, level)


canvas(640, 360)
noStroke()
noLoop()

drawFunction(draw)
