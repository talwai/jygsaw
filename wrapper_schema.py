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
strokeColor(30) # Same color scheme as background
fillColor(30)   # Same color scheme as background

point(p4, p4, color = None)
line((x1, y1), (x2, y2), color = None)
circle((x, y), radius, color = None, filled = True, stroke = False)
rect((x, y), width, height, color = None, filled = True, stroke = False)
ellipse((x, y), width, height, color = None, filled = True, stroke = Falset)
polygon((x1, y1), (x2, y2), (x3, y3), color = None, filled = True, stroke = False) # Points (triangle)
arc((x, y), width, height, startAngle, endAngle, color = None, filled = True, stroke = False)

# Callback functions
drawFunction(draw)
mousePressedFunction(fun)
mouseReleasedFunction(fun)

# Control functions
noLoop()
loop()
redraw()
frameRate(25)

