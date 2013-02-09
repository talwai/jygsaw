# Function Stubs go here:

# Returns width and height of window
width()
height()

# Returns x and y coordinates of mouse
mouseX()
mouseY()

# Returns boolean, whether or not the mouse is pressed
mousePressed()

canvas(title, width, height)

background(125) # Sets background color to (125, 125, 125)
background(red)
background(235, 19, 100)
stroke(30) # Same color scheme as background
fill(30)   # Same color scheme as background
noStroke() # Turns off stroke
noFill() # Turns off fill

point(p4, p4, color = None)
polygon((x1, y1), (x2, y2), (x3, y3)) # Points (triangle)
arc((x, y), width, height, startAngle, endAngle)

# Callback functions
drawFunction(draw)
mousePressedFunction(fun)
mouseReleasedFunction(fun)

# Control functions
noLoop()
loop()
redraw()
frameRate(25)

