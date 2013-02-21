from jygsaw.graphics import *
from random import random, choice

canvas(900, 500)
background(darkGray)


#   def point(x, y, color=None):
def draw():
    lineX = random() * 800 + 50
    lineY = random() * 300 + 125
    lineColor = choice([lightGray, white, orange, gray])
    line(width() / 2, height(), lineX, lineY, color=lineColor)
    point(lineX, lineY - 100, color=lineColor)
    loop()

onDraw(draw)
