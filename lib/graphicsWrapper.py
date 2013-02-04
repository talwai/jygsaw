from GraphicsObject import *
from GraphicsWindow import *
from Group import *
from Image import *
from Shape import *
from Text import *
from java.awt import Color


#class GraphicsWrapper():
window = GraphicsWindow('Empty', 100, 100)
#FillColor = Color.white
toLoop = False

"""
Creates a new window. Width, height and title can be set optionally as well
"""
def canvas(width = 400, height = 400, window_title = ' ', background = white):
    global window
    window = GraphicsWindow(window_title, width, height, background)


"""
Returns the width of the window
"""
def width(): # doesn't work
    return window.width

"""
Returns the width of the window
"""
def height(): # doesn't work
    return window.height

"""
Draws a line between coordinates (x1, y1), and (x2 and y2). You can optionally set the color as well
"""
def line((x1, y1), (x2, y2), color=None):
    #global FillColor
    #if color == None:
    #    color = FillColor
    new_line = Line((x1, y1), (x2, y2))
    window.draw(new_line)
    return new_line

"""
Creates a rectangle with the upper left corner at the given (x,y) coordinates.
"""
def rect((x, y), rectWidth = 100, rectHeight = 100, color=None, filled=True, stroke=False):
    #global FillColor
    #if color == None:
    #    color = FillColor
    new_rect = Rectangle((x, y), rectWidth, rectHeight, color, filled)
    window.draw(new_rect)
    return new_rect

"""
Creates a circle centered at the given (x,y) coordinates. The radius, color, filled status, and stoke status can be
optionally modified.
"""
def circle((x, y), radius = 50, color=None, filled=True, stroke=False):
    #global FillColor
    #if color == None:
    #    color = FillColor
    new_circle = Circle((x, y), radius, color, filled)
    window.draw(new_circle)
    return new_circle

"""
Creates an eclipse centered at the given (x,y) coordinates. Width, height, color, filled status and stroke status
can be optionally modified.
"""
def ellipse((x, y), width = 100, height = 100, color=None, filled=True, stroke=False):
    #global FillColor
    #if color == None:
    #    color = FillColor
    new_ellipse = Ellipse((x, y), width, height, color, filled)
    window.draw(new_ellipse)
    return new_ellipse

"""
Creates a polygon whose points are given in a list as the first argument. Width, height, color, filled status and stroke status can
be optionally modified
"""
def polygon (vertices, color = None, filled = True, stroke = False):
    #global FillColor
    #if color == None:
    #    color = FillColor
    new_polygon = Polygon (vertices, color, filled)
    window.draw(new_polygon)
    return new_polygon

"""
Creates an arc centered at the given (x,y) coordinates. The width, heigh, start angle, end angle, color, filled
status and stoke status can be optionally modified. Start angle and end angle refer to the 
"""
def arc((x, y), width = 100, height = 100, startAngle = 0, endAngle = 180, color = None, filled = True, stroke = False):
    #global FillColor
    #if color == None:
    #   color = FillColor
    new_arc = Arc((x,y), width, height, startAngle, (endAngle - startAngle), color)
    window.draw(new_arc)
    return new_arc

# It would be nice to have the option to not specify the width
# and height. Is there a way to get the default width/height of image?

"""
Draws an image with upper left corner at the given (x,y) coordinates. The image should be located at imagePath,
and the desired width and height of the image should be specified in their respective arguments.
"""
def image((x, y), imagePath, width, height):
    global window
    img = Image((x, y), imagePath, width, height)
    window.draw(img)

"""
Sets the color to fill shapes with.
"""
def fill(color):
    window.setDefaultColor(color)

"""
Sets the background color of the window.
"""
def setBackground(color):
    window.setBackgroundColor(color)
    # It would be nice to be able to accept multiple types of color input (r,g,b or name of color)
    # Doesn't seem to work
    
"""
Draws all of the objects on the window
"""
def draw():
    window.setVisible(True)

def redraw():
    window.redraw()


def mousePressed():
    # Perform some magic
    drawRect((x, y), mouseX, mouseY)

if ( __name__ == '__main__' ) or ( __name__ == 'main' ):
    canvas()
    
    rect((10,10))
    
    line((150,10),(200,10))
    
    ellipse((10,150))
    
    vertices = [(150,150),(160,160), (160, 150)]
    #polygon(vertices)
    
    #arc((250, 250))
        
    #circle((10,110))

    #setBackground(black)
    
    draw()
