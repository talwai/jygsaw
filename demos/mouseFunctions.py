from Box import Crayons

bx = 0.0
by = 0.0
boxSize = 75
overBox = False
locked = False
xOffset = 0.0
yOffset = 0.0


canvas(640, 360)
bx = width()/2.0
by = height()/2.0

def draw():
  background(0)

  # Test if the cursor is over the box
  if mouseX() > bx-boxSize && mouseX() < bx+boxSize && \
          mouseY() > by-boxSize && mouseY() < by+boxSize
    overBox = True
    if not locked:
      strokeColor(255)
      fillColor(153)

    else:
      strokeColor(153)
      fillColor(153)
      overBox = False

  # Draw the box
  rect(bx, by, boxSize, boxSize)

def mousePressed():
  if overBox:
    locked = True
    fillColor(255, 255, 255)
  else:
    locked = False

  xOffset = mouseX() - bx
  yOffset = mouseY() - by

def mouseDragged():
  if locked:
    bx = mouseX() - xOffset
    by = mouseY() - yOffset

def mouseReleased():
  locked = False

drawFunction(draw)
mousePressedFunction(mousePressed)
mouseDraggedFunction(mouseDragged)
mouseReleasedFunction(mouseReleased)
