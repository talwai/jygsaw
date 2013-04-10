from jygsaw.graphics import *


# Redraws the line when you click the mouse.
def draw():
    clear()

    global y

    y = y - 4
    if y < 0:
        y = height()
    line(0, y, width(), y)

canvas(640, 360)        # Size should be the first statement
stroke(255)             # Set line drawing color to white

y = int(height() * 0.5)

background(black)       # Set the background to black
draw()
onMousePress(draw)

while True:
    refresh(0.01)
