from balkcomsArmory import *

y = height * 0.5

canvas(640, 360)    # Size should be the first statement
strokeColor(255)          # Set line drawing color to white
noLoop()


# The statements in draw() are executed until the
# program is stopped. Each statement is executed in
# sequence and after the last line is read, the first
# line is executed again.
def draw():
    global y
    background(0)        # Set the background to black
    y = y - 1
    if y < 0:
        y = height()
    line(0, y, width(), y)

drawFunction(draw)
