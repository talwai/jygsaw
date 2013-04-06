from jygsaw.graphics import *

# The statements in draw() are executed until the
# program is stopped. Each statement is executed in
# sequence and after the last line is read, the first
# line is executed again.


def draw():
    clear()

    global y

    y = y - 4
    if y < 0:
        y = height()
    line(0, y, width(), y)

canvas(640, 360)        # Size should be the first statement
stroke(255)       # Se t line drawing color to white

y = int(height() * 0.5)

background(black)            # Set the background to black
draw()
onMousePress(draw)

while True:
    refresh(0.01)
