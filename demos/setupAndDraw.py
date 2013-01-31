from GraphicsWrapper import *
y = 100.0


# The statements in draw() are executed until the
# program is stopped. Each statement is executed in
# sequence and after the last line is read, the first
# line is executed again.
def draw():
    global y
    background(0)       # Set the background to black
    y = y - 1
    if (y < 0):
        y = height
    drawLine(0, y, width, y)

canvas(640, 360)        # Size must be the first statement
strokeColor(255)        # Set line drawing color to white
frameRate(30)

drawFunction(draw)
