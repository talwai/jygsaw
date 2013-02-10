# Basic shapes demo

from graphicsWrapper import *

canvas(640, 800)
background(black)
noStroke()

fill(gray)
polygon([(18, 18), (18, 360), (81, 360)])

fill(white)
rect(81, 81, 63, 63)

fill(gray)
polygon([(189, 18), (216, 18), (216, 360), (144, 360)])

fill(white)
ellipse(252, 144, 72, 72)

fill(gray)
polygon([(288, 18), (351, 360), (288, 360)])

fill(red)
arc(479, 300, 280, 280, 180, 360)
