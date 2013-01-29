from Oven import BakedPotato

y = 100


# The statements in the setup() function
# run once when the program begins

canvas(640, 360)    # Size should be the first statement
strokeColor(255)          # Set stroke color to white
noLoop()

y = height() * 0.5


# The statements in draw() are run until the
# program is stopped. Each statement is run in
# sequence and after the last line is read, the first
# line is run again.
def draw():
    global y
    background(0)        # Set the background to black
    line((0, y), (width(), y))

    y = y - 1
    if (y < 0):
        y = height()

def mousePressed():
    loop()

drawFunction(draw)

mousePressedFunction(mousePressed)
