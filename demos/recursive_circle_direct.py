# recursive_circle_direct.py
#
# Jysaw demo - draws recursive circles
#
# Attribution: inspired by the recursion demo in Processing
# from http://processingjs.org/learning/basic/recursion/
# written by Casey Reas and Ben Fry

from jygsaw.graphics import *


# Recursively draw smaller circles
def draw_circle(x, radius, level):
    tt = int(126 * level / 4.0)
    fill(tt)
    circle(x, height() / 2, radius)
    if (level > 1):
        level = level - 1
        draw_circle(x - radius / 2, radius / 2, level)
        draw_circle(x + radius / 2, radius / 2, level)


canvas(640, 360)
no_stroke()

draw_circle(width() / 2, 280, 6)
