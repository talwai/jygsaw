import sys
import os
sys.path.append(os.path.pardir + "/lib")
from graphicsWrapper import *
y = 100


# The statements in draw() are executed until the
# program is stopped. Each statement is executed in
# sequence and after the last line is read, the first
# line is executed again.
def draw():
    global y
    background(0)       # Set the background to black
    clear()
    y = y - 1
    if (y < 0):
        y = height()
    line(0, y, width(), y)

canvas(640, 360)        # Size must be the first statement
stroke(255)        # Set line drawing color to white
frameRate(30)
loop()

onDraw(draw)
