# recursive_circle.py
#
# Jysaw demo - draws recursive circles
#
# Attribution: inspiRED by the recursion demo in Processing
# from http://processingjs.org/learning/basic/recursion/
# written by Casey Reas and Ben Fry

from jygsaw.graphics import *


def draw():
    recursive_circle(width() / 2, 280, 6)


# Recursively draw smaller circles
def recursive_circle(x, radius, level):
    tt = int(126 * level / 4.0)
    fill(tt)
    circle(x, height() / 2, radius)
    if (level > 1):
        level = level - 1
        recursive_circle(x - radius / 2, radius / 2, level)
        recursive_circle(x + radius / 2, radius / 2, level)


canvas(640, 360)
no_stroke()

on_draw(draw)
jygsaw_start()
