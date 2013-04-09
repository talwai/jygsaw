from jygsaw.graphics import *

bx = 0.0
by = 0.0
boxSize = 75
overBox = False
locked = False
xOffset = 0.0
yOffset = 0.0


canvas(640, 360)
bx = width() / 2
by = height() / 2


def draw():
    global overBox
    clear()
    background(0)

    # Test if the cursor is over the box
    if (mouseX() > bx and mouseX() < bx + boxSize and
            mouseY() > by and mouseY() < by + boxSize):
        overBox = True
        if not locked:
            stroke(255)
            fill(153)
    else:
        stroke(153)
        fill(153)
        overBox = False

    # Draw the box
    rect(bx, by, boxSize, boxSize)


def mousePressed():
    global locked, xOffset, yOffset

    if overBox:
        locked = True
        fill(255, 255, 255)
        print "should fill"
    else:
        locked = False

    xOffset = mouseX() - bx
    yOffset = mouseY() - by


def mouseDragged():
    global bx, by
    if locked:
        bx = mouseX() - xOffset
        by = mouseY() - yOffset


def mouseReleased():
    global locked
    locked = False


onMousePress(mousePressed)
onMouseDrag(mouseDragged)
onMouseRelease(mouseReleased)
onDraw(draw)
jygsawMain(1.0 / 30)
