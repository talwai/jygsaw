# setup_and_draw_direct.py
#
# Jysaw demo - draws a square and several points
#
# Attribution: inspired by the SetupDraw demo in Processing
# from http://processingjs.org/learning/basic/setupdraw/
# written by Casey Reas and Ben Fry

from jygsaw.graphics import *
y = 100


# The statements in draw() are executed until the
# program is stopped. Each statement is executed in
# sequence and after the last line is read, the first
# line is executed again.

canvas(640, 360)        # Size must be the first statement
stroke(255)        # Set line drawing color to WHITE
background(0)       # Set the background to BLACK

while True:
    clear()
    y = y - 1
    if (y < 0):
        y = height()
    line(0, y, width(), y)
    refresh(0.02)
