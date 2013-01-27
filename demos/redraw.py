y = 0
 
# The statements in the setup() function 
# execute once when the program begins
def setup():
  openCanvas(640, 360); # Size should be the first statement
  setStroke(255);     # Set line drawing color to white
  noLoop();
  global y
  y = height * 0.5;

# The statements in draw() are executed until the 
# program is stopped. Each statement is executed in 
# sequence and after the last line is read, the first 
# line is executed again.
def draw():
  setBackground(0)   # Set the background to black
  global y
  y = y - 4
  if y < 0:
    y = height 
  drawLine(0, y, width, y)

def mousePressed():
  redraw()
