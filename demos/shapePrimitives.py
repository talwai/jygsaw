# Basic shapes demo

from GraphicsWrapper import *

canvas(640, 360)
background(0)
noStroke()

fillColor(204)
polygon((18, 18), (18, 360), (81, 360))

fillColor(102)
rect((81, 81), 63, 63)

fillColor(204)
polygon((189, 18), (216, 18), (216, 360), (144, 360))

fillColor(255)
ellipse((252, 144), 72, 72)

fillColor(204)
polygon((288, 18), (351, 360), (288, 360))

fillColor(255)
arc((479, 300), 280, 280, 180, 360)
