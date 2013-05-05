# points_and_lines_managed.py
#
# Jysaw demo - draws a square and several points
#
# Attribution: inspired by the pointslines demo in Processing
# from http://processingjs.org/learning/basic/pointslines/
# written by Casey Reas and Ben Fry

from jygsaw.graphics import *

d = 70
p1 = d
p2 = p1 + d
p3 = p2 + d
p4 = p3 + d

canvas(640, 360)
background(BLACK)


def draw():
    # Draw gray box
    stroke(GRAY)
    line(p3, p3, p2, p3)
    line(p2, p3, p2, p2)
    line(p2, p2, p3, p2)
    line(p3, p2, p3, p3)

    # Draw white points
    stroke(WHITE)
    point(p1, p1)
    point(p1, p3)
    point(p2, p4)
    point(p3, p1)
    point(p4, p2)
    point(p4, p4)

on_draw(draw)
jygsaw_start()
