from GraphicsObject import *
from GraphicsWindow import *
from Group import *
from Image import *
from Shape import *
from Text import *
from java.awt.Color import *
import time


toLoop = False
Stroke = False
fr = 60 # Frame Rate

def canvas(width=400, height=400, window_title=' ', background=white):
    """
    Creates a new window. Width, height and title can be set optionally as well
    """

    global window
    window = GraphicsWindow(window_title, width, height, background)
    window.setVisible(True)

def width():
    """
    Returns the width of the window
    """

    return window.w

def height():
    """
    Returns the height of the window
    """

    return window.h

def point(x, y, color=None):
    """
    Draws a point.
    """

    new_point = Point((x,y), color)
    window.draw(new_point)
    return new_point

def line(x1, y1, x2, y2, color=None):
    """
    Draws a line between coordinates (x1, y1), and (x2 and y2). You can
    optionally set the color as well
    """

    new_line = Line((x1, y1), (x2, y2))
    window.draw(new_line)
    return new_line

def rect(x, y, rectWidth=100, rectHeight=100, color=None, filled=True):
    """
    Creates a rectangle with the upper left corner at the given (x,y)
    coordinates.
    """

    new_rect = Rectangle((x, y), rectWidth, rectHeight, color, filled)
    window.draw(new_rect)
    return new_rect

def circle(x, y, radius=50, color=None, filled=True):
    """
    Creates a circle centered at the given (x,y) coordinates. The radius,
    color, filled status, and stoke status can be optionally modified.
    """

    new_circle = Circle((x, y), radius, color, filled)
    window.draw(new_circle)
    return new_circle

def ellipse(x, y, width=100, height=100, color=None, filled=True):
    """
    Creates an eclipse centered at the given (x,y) coordinates. Width, height,
    color, filled status and stroke status can be optionally modified.
    """

    new_ellipse = Ellipse((x, y), width, height, color, filled)
    window.draw(new_ellipse)
    return new_ellipse

def polygon(vertices, color=None, filled=True):
    """
    Creates a polygon whose points are given in a list as the first argument.
    Width, height, color, filled status and stroke status can be optionally
    modified
    """

    new_polygon = Polygon(vertices, color, filled)
    window.draw(new_polygon)
    return new_polygon

def arc(x, y, width=100, height=100, startAngle=0, endAngle=180, \
            color=None, filled=True):
    """
    Creates an arc centered at the given (x,y) coordinates. The width, height,
    start angle, end angle, color, filled status and stoke status can be
    optionally modified. Start angle and end angle refer to the
    """

    new_arc = Arc((x, y), width, height, startAngle, (endAngle - startAngle), color)
    window.draw(new_arc)
    return new_arc

# It would be nice to have the option to not specify the width
# and height. Is there a way to get the default width/height of image?
def image(x, y, imagePath, width, height):
    """
    Draws an image with upper left corner at the given (x,y) coordinates.
    The image should be located at imagePath, and the desired width and
    height of the image should be specified in their respective arguments.
    """

    global window
    img = Image((x, y), imagePath, width, height)
    window.draw(img)
    return img

def fill(r = None, g = None, b = None):
    """
    Sets the color to fill shapes with.
    """

    window.setDefaultColor(_color(r, g, b))

def background(r = None, g = None, b = None):
    """
    Sets the background color of the window.
    """

    window.setBackgroundColor(_color(r, g, b))

#---------------------------------------------------------------
#-----------Mouse functions-------------------------------------

def mouseX():
    """
    Returns x coordinate of the mouse
    """

    return window.mouseX

def mouseY():
    """
    Returns y coordinate of the mouse
    """

    return window.mouseY

def onMousePress(mousePressed):
    """
    Sets the window's onMousePressed variable to be the user defined
    mouseClicked function. It will then be called by the window's mouse
    listener when the event occurs.
    """

    window.onMousePressed = mousePressed

def onMouseRelease(mouseReleased):
    """
    Sets the window's onMouseReleased variable to be the user defined
    mouseClicked function. It will then be called by the window's mouse
    listener when the event occurs.
    """

    window.onMouseReleased = mouseReleased

def onMouseClick(mouseClicked):
    """
    Sets the window's onMouseClick variable to be the user defined
    mouseClicked function. It will then be called by the window's mouse
    listener when the event occurs.
    """

    window.onMouseClick = mouseClicked

def onMouseDrag(mouseDragged):
    """
    Sets the window's onMouseDragged variable to be the user defined
    mouseDragged function. It will then be called by the window's mouse
    listener when the event occurs.
    """

    window.onMouseDragged = mouseDragged

def onMouseMove(mouseMoved):
    """
    Sets the window's onMouseMoved variable to be the user defined
    mouseMoved function. It will then be called by the window's mouse
    listener when the event occurs.
    """

    window.onMouseMoved = mouseMoved

#---------------------------------------------------------------
#--------------------Keyboard Methods---------------------------

def onKeyPress(keyPressed):
    """
    Callback for window's key listener. Passes the user defined function to the window's keyPressed
    method.
    """
    window.onKeyPressed = keyPressed

def onKeyRelease(keyReleased):
    """
    Callback for window's key listener. Passes the user defined function to the window's keyReleased
    method.
    """
    window.onKeyReleased = keyReleased


def onKeyType(keyTyped):
    """
    Callback for window's key listener. Passes the user defined function to the window's keyTyped
    method.
    """
    window.onKeyTyped = keyTyped


def lastKeyChar():
    """
    Returns the last key character that was pressed. Non-ascii keys will return a question mark.
    """
    return window.lastKeyChar

def lastKeyCode():
    """
    Returns the last key code that was pressed. Codes are of the form VK_CODE, from the swing library. All the
    codes can be found at http://docs.oracle.com/javase/1.4.2/docs/api/java/awt/event/KeyEvent.html.
    """
    return window.lastKeyCode

#---------------------------------------------------------------


def noStroke():
    """
    Sets stroke to false
    """

    global Stroke
    Stroke = False

def loop():
    """
    Tells the draw function to loop when it is called
    """

    global toLoop
    toLoop = True

def noLoop():
    """
    Tells the draw function not to loop when it is called,
    or to stop looping if it has already started. This is the default.
    """

    global toLoop
    toLoop = False

def frameRate(rate):
    """
    Sets the frame rate value
    """

    global fr
    fr = rate

def stroke(r = None, g = None, b = None):
    """
    Sets stroke to true. If a color is given then set the stroke
    color to that color
    """

    window.setStroke(True)
    window.setStrokeColor(_color(r, g, b))

def noStroke():
    """
    Sets stroke to false
    """

    window.setStroke(False)

def clear():
    """
    Clears the window of all objects and redraws screen
    """

    window.clear()

def onDraw(draw):
    """
    Callback function which calls the user defined draw function.
    It repeatedly loops if loop() has been called.
    """

    if toLoop:
        while toLoop:
            draw()
            redraw()
            time.sleep(1/fr)
    else:
        draw()
        redraw()

def redraw():
    """
    Redraws all of the objects on the window. Not sure there is a point to it.
    """

    window.redraw()

def text((x, y), s, font, size, color=None, attribute=PLAIN):
    """
    Draws specified text to the screen at (x, y), with specified font and size
    and optional color and attribute (PLAIN, BOLD, ITALIC)
    """

    newText = Text((x, y), s, font, size, color, attribute)
    window.draw(newText)
    return newText

def _color(r, g = None, b = None):
    if g == None or b == None:
        assert r != None and g == None and b == None, \
            "color takes exactly 1 or 3 parameters"
        if isinstance(r, int):
            # Will create color (r, r, r)
            return Color(r, r, r)
        if isinstance(r, Color):
            return r
        else:
            # r is of an unrecognized type
            pass
    else:
        assert r != None and g != None and b != None, \
            "color takes exactly 1 or 3 parameters"
        assert isinstance(r, int) and isinstance(g, int) and isinstance(b, int), "color takes 3 integers"
        return Color(r, g, b)

if ( __name__ == '__main__' ) or ( __name__ == 'main' ):
    canvas()
    loop()
    frameRate(60)

    x = None
    y = None

    rectX = 10
    rectY = 10

    def draw():
        global rectX
        global rectY
        clear()
        vertices = [(250,250),(360,360), (360, 250)]

        fill(red)
        rect(rectX,rectY)
        line(150, 10, 200, 10)
        fill(pink)
        ellipse(10, 150)

        polygon(vertices)
        arc(300, 100)
        circle(10,50)

        background(black)
        w = width()
        h = height()
        
        if rectX < (w - 10):
            rectX = rectX + 1
        else:
            rectX = rectX - 1

        if rectY < (h - 10):
            rectY = rectY + 1
        else:
            rectY = rectY - 1

        text((200, 200), 'Hello, world', 'Times New Roman', 24, green)

    def mousePressed():
        print 'Mouse was pressed.'

    def mouseDragged():
        print 'Mouse is being dragged.'
        print 'X = ' + str(x) + ' Y = ' + str(y)

    def mouseReleased():
        print 'Mouse released'

    def mouseClicked():
        print 'Mouse clicked'

    def mouseMoved():
        global x, y
        x = mouseX()
        y = mouseY()
        print 'Mouse moved x = %d, y = %d' % (x, y)

    def keyPressed():
        char = lastKeyChar()
        code = lastKeyCode()
        print 'Key Pressed! Char = %s Code = %s' % (char,code)

    def keyReleased():
        char = lastKeyChar()
        code = lastKeyCode()
        print 'Key Released! Char = %s Code = %s' % (char,code)

    def keyTyped():
        char = lastKeyChar()
        code = lastKeyCode()
        print 'Key Typed! Char = %s Code = %s' % (char,code)

    #onMousePress(mousePressed)
    #onMouseRelease(mouseReleased)
    #onMouseDrag(mouseDragged)
    #onMouseMove(mouseMoved)
    #onMouseClick(mouseClicked)
    onKeyPress(keyPressed)
    onKeyRelease(keyReleased)
    onKeyType(keyTyped)
    onDraw(draw)

