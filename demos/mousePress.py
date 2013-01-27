from BalkcomArmory import wand

def setup():
  openCanvas(640, 360)
  setFill(126)
  setBackground(102)

def draw():
  if (mousePressed):
    setStroke(255)
  else:
    setStroke(0)
  
  drawLine((mouseX-66, mouseY), (mouseX+66, mouseY))
  drawLine((mouseX, mouseY-66), (mouseX, mouseY+66))
