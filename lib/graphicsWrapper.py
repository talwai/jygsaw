from GraphicsLibrary import *
import threading 

# Still figuring out how to implement threads...
class Graphics():
    Window = GraphicsWindow('Empty',100,100)
    FillColor = Color.none
    mouseX, mouseY
    toLoop = False
    
    #Actually we probably should start thread in draw
    def setup(window_title, width, height):
        thread_draw = GraphicsWrapper()
        thread_draw.start()
        thread_draw.gSetup(window_title, width, height)


class GraphicsWrapper(threading.Thread):
    global Window
    
    def __init__(self, window):
        Thread.__init__()
        Window = window
        
    def run(self):
        while (global toLoop):
            draw()
      
    def gSetup(window_title,width,height):
        Window = GraphicsWindow (window_title,width,height)
        #modify Window attributes
    
    def drawLine((x1,y1),(x2,y2)):
        global Window
        line = Line(self, (x1,y1),(x2,y2))
        Window.draw(line)    
    
    def drawRect((x, y), rectWidth, rectHeight, filled = True, stroke = False):
        global Window, FillColor
        rect = Rectangle(self, (x, y), rectWidth, rectHeight, FillColor, true)
        Window.draw(rect)

    def drawCircle ((x,y), radius, color = global FillColor, filled = True, stroke = False):
        global Window
        circle = Circle(self, (x,y), radius, color, filled, stroke)
        Window.draw(circle)
        
    def drawEllipse ((x,y), width, height, color = global Fillcolor, filled = True, stroke = False):
        global Window
        ellipse = Ellipse(self, (x,y) , width, height, color, filled)
        Window.draw(ellipse)
    
# It would be nice to have the option to not specify the width
# and height. Is there a way to get the default width/height of image?
    def drawImage((x,y), imagePath, width, height):
        global Window
        img = Image((x,y), imagePath, width, height)
        Window.draw(img)
    
    def setBackground(r, g, b):
        global Window
        Window.contentPane.background = (r,g,b)
    
    def draw():
        for img in Window.objs:
            img._draw(Window)

    
#################################### Example #####################################

# Can create static sketches by not using setup or draw and putting code in "main"
drawLine((x1, y1), (x2, y2))
drawRect((x, y), rectWidth, rectHeight)
drawPolygon((x1, y1), (x2, y2), (x3, y3))
# What if have code in "main" and have setup and draw methods

# Gets called once
setup():
    setSize(300, 400) # sets window size
    setFrameRate(35) # Can be set or not (default)
    setStroke(red) # Sets line drawing color to red
    setStroke(125) # Sets line drawing color to (125, 125, 125) (easy for white/grays/black)
    setStroke(126, 35, 92) # Sets line drawing color to (126, 35, 92)
    
    noLoop() # Causes draw to not be looped
    loop() # Causes draw to be looped (default?)
    redraw() # Calls draw once; useful for events

# Gets repeatedly called until program ends (window closes?)
draw():
    setBackground(blue)

    # height and width are global variables and are from setSize()
    y = height
    x = width
    
    drawLine((x1, y1), (x2, y2))
    drawRect((x, y), rectwidth, rectheight)
    # etc.
    
    if (mousePressed):
        setStroke(255);
    else:
        setStroke(0);
    
    setFill() # Takes all the color defintions like setStroke
    # If drawFilledRect() is called with different stroke and fill colors, 
     
    # mouseX and mouseY are the current mouse coordinates
    drawLine(mouseX-66, mouseY, mouseX+66, mouseY);
    drawLine(mouseX, mouseY-66, mouseX, mouseY+66);

    img = loadImage('path')
    drawImage(img, (x, y), imageWidth, imageHeight)
    drawImage(img, (x, y)) # Draws image at the original width and height

def mousePressed():
    # Perform some magic
    drawRect((x, y), mouseX, mouseY)
