from jygsaw.graphics import *
from random import random, choice

canvas(900, 500)
background(darkGray)

def draw():
    lineX = random() * 800 + 50
    lineY = random() * 300 + 125
    lineColor = choice([lightGray, white, orange, gray])
    stroke(lineColor)
    line(width() / 2, height(), lineX, lineY)
    point(lineX, lineY - 100)

onDraw(draw)

jygsawMain(0.1)
