# shape_primitives.py
#
# Jysaw demo - draws some base shapes 
#
# Attribution: inspired by the shapeprimitives demo in Processing 
# from http://processingjs.org/learning/basic/shapeprimitives/
# written by Casey Reas and Ben Fry


from jygsaw.graphics import *

canvas(640, 360)
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
arc(0, 0, 280, 280, 180, 360)
