import sys
import os
sys.path.append(os.path.pardir + "/lib")
from graphicsWrapper import *

y = 100


# The statements in the setup() function
# run once when the program begins

canvas(640, 360)    # Size should be the first statement
# stroke(255)          # Set stroke color to white
noLoop()

y = int(height() * 0.5)


# The statements in draw() are run until the
# program is stopped. Each statement is run in
# sequence and after the last line is read, the first
# line is run again.
def draw():
    global y
    print "Y: ", y
    background(black)        # Set the background to black
    line(0, y, width(), y)

    y = y - 1
    if (y < 0):
        y = height()

onDraw(draw)
onMousePressed(draw)
