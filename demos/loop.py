# loop.py
#
# Jygsaw demo - Loops and draws a moving line.`
#
# Attribution: Inspired by the loop demo in Processing
# from http://processingjs.org/learning/basic/keyboardfunctions/
# written by Casey Reas and Ben Fry.

from jygsaw.graphics import *

y = 100


# The statements in the setup() function
# run once when the program begins

canvas(640, 360)      # Size should be the first statement
stroke(255)           # Set stroke color to white
running = False

y = int(height() * 0.5)


# The statements in draw() are run until the
# program is stopped. Each statement is run in
# sequence and after the last line is read, the first
# line is run again.
def draw():
    global y
    if running:
        clear()
        line(0, y, width(), y)

        y = y - 1
        if (y < 0):
            y = height()


def mousePressed():
    global running
    running = True

onMousePress(mousePressed)
onDraw(draw)
background(black)
jygsawMain(1.0 / 30)
