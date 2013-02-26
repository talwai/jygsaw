"""
A simple graphics library that wraps around Java's Swing library.
It's robust, easy to use, and most importantly easy to learn for
both new and old programmers alike.
"""
from graphicsobject import *
from graphicswindow import *
from group import *
from image import *
from shape import *
from text import *
from java.awt import Color
import time


rectX = 0 # Just used for testing - delete or move eventually
rectY = 0 # Just used for testing - delete or move eventually
directionX = 1 # Just used for testing - delete or move eventually
directionY = 1 # Just used for testing - delete or move eventually
_toLoop = False
_fr = 60.0  # Frame Rate


def canvas(width=400, height=400, window_title='Jygsaw Canvas', background=white):
    """
    Creates and returns a new Jygsaw Window and Canvas.
    """
    global window
    window = GraphicsWindow(window_title, int(width), int(height), background)
    window.setVisible(True)
    return window


def width():
    """
    Returns the width of the Canvas.
    """
    return window.width


def height():
    """
    Returns the height of the Canvas.
    """
    return window.height


def point(x, y, color=None):
    """
    Draws and returns a :py:class:`Point` at (x,y).
    """
    new_point = Point(int(x), int(y), color)
    window.draw(new_point)
    return new_point


def line(x1, y1, x2, y2, color=None):
    """
    Returns a Line. Draws a line between coordinates (x1, y1), and
    (x2 and y2). You can optionally set the color as well.
    """
    new_line = Line((int(x1), int(y1)), (int(x2), int(y2)), color)
    window.draw(new_line)
    return new_line


def rect(x, y, rectWidth, rectHeight, color=None):
    """
    Return a Rectangle. Creates a rectangle with the upper left corner
    at the given (x,y) coordinates.
    """
    new_rect = Rectangle(
        int(x), int(y), int(rectWidth), int(rectHeight), color)
    window.draw(new_rect)
    return new_rect


def circle(x, y, radius, color=None):

    """
    Creates a circle centered at the given (x,y) coordinates. The
    radius, color, filled status, and stoke status can be optionally
    modified.
    """
    new_circle = Circle(int(x), int(y), int(radius), color)
    window.draw(new_circle)
    return new_circle


def ellipse(x, y, width, height, color=None):

    """
    Creates an eclipse centered at the given x, y coordinates. Width,
    height, color, filled status and stroke status can be optionally
    modified.
    """
    new_ellipse = Ellipse(
        int(x), int(y), int(width), int(height), color)
    window.draw(new_ellipse)
    return new_ellipse


def polygon(vertices, color=None):
    """
    Creates a polygon whose points are given in a list as the first
    argument. Width, height, color, filled status and stroke status
    can be optionally modified.
    """
    new_polygon = Polygon(vertices, color)
    window.draw(new_polygon)
    return new_polygon


def regPolygon(x, y, sides, length, color=None):
    """
    Creates a regular polygon with the given number of sides at the
    given x, y coordinates. Each side's length is determined by the
    given length. Color and filled determine the color of the shape
    and if it is filled or not.
    """
    new_reg_polygon = RegPolygon(
        int(x), int(y), int(sides), int(length), color)
    window.draw(new_reg_polygon)
    return new_reg_polygon


def arc(x, y, width, height, startAngle, endAngle,
        color=None):
    """
    Creates an arc centered at the given (x,y) coordinates. The
    width, height, start angle, end angle, color, filled status
    and stoke status can be optionally modified. The start and end
    angle degrees refer to a circle where 0 is on the left side of
    the screen, 90 is at the top, 180 is on the right and 270 is at
    the bottom.
    """
    new_arc = Arc(
        int(x), int(y), int(width), int(height), startAngle, (endAngle - startAngle), color)
    window.draw(new_arc)
    return new_arc


def image(x, y, imagePath, width=None, height=None):
    """
    Draws an image with upper left corner at the given (x,y)
    coordinates. The image should be located at imagePath, and the
    desired width and height of the image should be specified in their
    respective arguments.
    """
    global window
    img = Image(int(x), int(y), imagePath, width, height)
    window.draw(img)
    return img


def fill(r=None, g=None, b=None):
    """ Sets the color to fill shapes with."""
    window.setFilled(True)
    if r != None:
        window.setDefaultColor(color(r, g, b))


def noFill():
    """ Sets filled to False."""
    window.setFilled(False)


def background(r=None, g=None, b=None):
    """ Sets the background color of the window."""
    window.setBackgroundColor(color(r, g, b))

#---------------------------------------------------------------
#-----------Mouse Methods-------------------------------------


def mouseX():
    """Returns x coordinate of the mouse."""
    return window.mouseX


def mouseY():
    """Returns y coordinate of the mouse."""
    return window.mouseY


def mousePressed():
    """Returns if mouse was pressed or not."""
    return window.mouseEventType == MouseEvent.MOUSE_PRESSED \
        or window.mouseEventType == MouseEvent.MOUSE_DRAGGED


def mouseReleased():
    """Returns if mouse was released or not."""
    return window.mouseEventType == MouseEvent.MOUSE_RELEASED


def mouseClicked():
    """Returns if mouse was clicked or not."""
    return window.mouseEventType == MouseEvent.MOUSE_CLICKED


def mouseDragged():
    """Returns if mouse was dragged or not."""
    return window.mouseEventType == MouseEvent.MOUSE_DRAGGED


def mouseMoved():
    """Returns if mouse was moved or not."""
    return window.mouseEventType == MouseEvent.MOUSE_MOVED


def mouseEntered():
    """Returns if mouse has entered the window or not."""
    return window.mouseEventType == MouseEvent.MOUSE_ENTERED


def mouseExited():
    """Returns if mouse has exited the window or not."""
    return window.mouseEventType == MouseEvent.MOUSE_EXITED


def onMousePress(mousePressed):
    """
    Sets the window's onMousePressed variable to be the user
    defined mouseClicked function. It will then be called by
    the window's mouse listener when the event occurs.
    """
    window.onMousePressed = mousePressed


def onMouseRelease(mouseReleased):
    """
    Sets the window's onMouseReleased variable to be the user
    defined mouseClicked function. It will then be called by the
    window's mouse listener when the event occurs.
    """
    window.onMouseReleased = mouseReleased


def onMouseClick(mouseClicked):
    """
    Sets the window's onMouseClick variable to be the user
    defined mouseClicked function. It will then be called by the
    window's mouse listener when the event occurs.
    """
    window.onMouseClick = mouseClicked


def onMouseDrag(mouseDragged):
    """
    Sets the window's onMouseDragged variable to be the user
    defined mouseDragged function. It will then be called by the
    window's mouse listener when the event occurs.
    """
    window.onMouseDragged = mouseDragged


def onMouseMove(mouseMoved):
    """
    Sets the window's onMouseMoved variable to be the user
    defined mouseMoved function. It will then be called by the window's
    mouse listener when the event occurs.
    """
    window.onMouseMoved = mouseMoved

def onMouseEnter(mouseEntered):
    """
    Sets the window's onMouseEntered variable to be the user
    defined mouseEntered function. It will then be called by the
    window's mouse listener when the event occurs.
    """
    window.onMouseEntered = mouseEntered

def onMouseExit(mouseExited):
    """
    Sets the window's onMouseEntered variable to be the user
    defined mouseEntered function. It will then be called by the
    window's mouse listener when the event occurs.
    """
    window.onMouseExited = mouseExited

#---------------------------------------------------------------
#--------------------Keyboard Methods---------------------------


def keyPressed():
    """Returns if key was pressed or not."""
    return window.keyEventType is KeyEvent.KEY_PRESSED


def keyReleased():
    """Returns if key was released or not."""
    return window.keyEventType is KeyEvent.KEY_RELEASED


def onKeyPress(keyPressed):
    """
    Callback for window's key listener. Passes the user defined
    function to the window's keyPressed method.
    """
    window.onKeyPressed = keyPressed


def onKeyRelease(keyReleased):
    """
    Callback for window's key listener. Passes the user defined
    function to the window's keyReleased method.
    """
    window.onKeyReleased = keyReleased


def onKeyType(keyTyped):
    """
    Callback for window's key listener. Passes the user defined
    function to the window's keyTyped method.
    """
    window.onKeyTyped = keyTyped


def lastKeyChar():
    """
    Returns the last key character that was pressed. Non-ascii keys
    will return a question mark.
    """
    return window.lastKeyChar


def lastKeyCode():
    """
    Returns the last key code that was pressed. Codes are of the form
    VK_CODE, from the swing library. All the codes can be found at
    http://docs.oracle.com/javase/1.4.2/docs/api/java/awt/event/KeyEvent.html.
    """
    return window.lastKeyCode

#---------------------------------------------------------------


def loop():
    """
    Tells the draw function to loop when it is called.
    """
    global _toLoop
    _toLoop = True


def noLoop():
    """
    Tells the draw function not to loop when it is called,
    or to stop looping if it has already started.
    This is the default.
    """
    global _toLoop
    _toLoop = False


def frameRate(rate):
    """
    Sets the frame rate value.
    """
    global _fr
    _fr = float(rate)


def stroke(r=None, g=None, b=None):
    """
    Sets stroke to true. If a color is given then set the stroke
    color to that color.
    """
    window.setStroke(True)
    if r != None:
        window.setStrokeColor(color(r, g, b))


def noStroke():
    """
    Sets stroke to false.
    """
    window.setStroke(False)


def clear():
    """
    Clears the window of all objects and redraws screen.
    """
    window.clear()


def onDraw(user_draw):
    """
    Callback function which calls the user defined draw function.
    It repeatedly loops if loop() has been called.
    """
    user_draw()
    window.frame.contentPane.repaint()
    window.user_draw_fn = user_draw
    while True:
        while _toLoop:
            window.frame.contentPane.repaint()
            time.sleep(1.0 / _fr)


def redraw(delay=0.0):
    """
    Redraws all of the objects on the window.
    """
    window.redraw(delay)


def text(x, y, string, color=None, attribute=PLAIN):
    """
    Draws specified text "string" to the screen at (x, y), with
    specified font and size and optional color and attribute
    (PLAIN, BOLD, ITALIC)
    """
    newText = Text(int(x), int(y), string, color, attribute)
    window.draw(newText)
    return newText


def font(f):
    """
    Sets the font to the given font in 'f'.
    """
    window.setFont(f)


def textSize(s):
    """
    Sets the text size to the given size in 's'.
    """
    window.setTextSize(s)


def color(r, g=None, b=None):
    """
    Returns a color based on the values passed to the function.

    If 'r' is the only value passed and it's the name of a color,
    then that color will be created and returned.

    If 'r' is the only value passed and it's an integer, a color
    will be created and returned where all three values of the
    color's r, g, b are the same as 'r'.

    If 'r', 'g', and 'b' all have values then a color will be
    created and returned with the corresponding r, g, b values.

    Otherwise an assert is thrown.
    
    """
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
        assert isinstance(r, int) and isinstance(
            g, int) and isinstance(b, int), "color takes 3 integers"
        return Color(r, g, b)

if (__name__ == '__main__') or (__name__ == 'main'):
    canvas()
    loop()
    stroke()
    frameRate(160.0)

    rectX = 150
    rectY = 30

    image(200, 200, './puppy.jpg', 50, 50)

    def draw():
        global rectX
        global rectY
        global directionX
        global directionY

        clear()
        vertices = [(250, 250), (250, 370), (360, 340), (360, 250)]

        fill(red)
        stroke(blue)
        rect(rectX, rectY, 200, 150)
        line(150, 10, 200, 10)
        fill(pink)
        ellipse(10, 150, 200, 100)

        fill(green)
        polygon(vertices)
        regPolygon(10, 300, 3, 25)
        arc(300, 100, 100, 100, 0, 170)
        circle(0, 0, 30)

        background(white)
        w = width()
        h = height()

        if rectX >= w:
            directionX = -1
        elif rectX < -10:
            directionX = 1

        rectX = rectX + directionX

        if rectY >= h:
            directionY = -1
        elif rectY < -10:
            directionY = 1

        rectY = rectY + directionY

        font('Times New Roman')
        textSize(50)

        text(200, 200, 'Hello, world', black)

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
        print 'Key Pressed! Char = %s Code = %s' % (char, code)

    def keyReleased():
        char = lastKeyChar()
        code = lastKeyCode()
        print 'Key Released! Char = %s Code = %s' % (char, code)

    def keyTyped():
        char = lastKeyChar()
        code = lastKeyCode()
        print 'Key Typed! Char = %s Code = %s' % (char, code)

    # onMousePress(mousePressed)
    # onMouseRelease(mouseReleased)
    # onMouseDrag(mouseDragged)
    # onMouseMove(mouseMoved)
    # onMouseClick(mouseClicked)
    onKeyPress(keyPressed)
    onKeyRelease(keyReleased)
    onKeyType(keyTyped)
    onDraw(draw)