"""
graphics.py contains the methods that the user calls directly.
"""
from __future__ import with_statement
from graphicsobject import *
from graphicswindow import *
from group import *
from image import *
from shape import *
from text import *
from java.awt import Color
import time
from threading import Lock
from warnings import warn


rectX = 0
rectY = 0
directionX = 1
directionY = 1
_toLoop = False
_fr = 60.0  # Frame Rate


def canvas(width=400, height=400, window_title='Jygsaw Canvas', background=white):
    """
    Creates and returns a new Jygsaw Canvas.
    """

    global window
    window = GraphicsWindow(window_title, int(width), int(height), background)
    window.setVisible(True)
    return window


def width():
    """
    Returns the width of the Canvas.
    """

    return window.w


def height():
    """
    Returns the height of the Canvas.
    """

    return window.h


def point(x, y, color=None):
    """
    Draws and returns a :py:class:`Point` at (x,y).
    """

    new_point = Point(int(x), int(y), color)
    window.draw(new_point)
    return new_point


def line(x1, y1, x2, y2, color=None):
    """
    Returns a Line. Draws a line between coordinates (x1, y1), and (x2 and y2). You can
    optionally set the color as well.
    """

    new_line = Line((int(x1), int(y1)), (int(x2), int(y2)), color)
    window.draw(new_line)
    return new_line


def rect(x, y, rectWidth, rectHeight, color=None, filled=True):
    """
    Return a Rectangle. Creates a rectangle with the upper left corner at the given (x,y)
    coordinates.
    """

    new_rect = Rectangle(
        int(x), int(y), int(rectWidth), int(rectHeight), color, filled)
    window.draw(new_rect)
    return new_rect


def circle(x, y, radius, color=None, filled=True):
    """
    Creates a circle centered at the given (x,y) coordinates. The radius,
    color, filled status, and stoke status can be optionally modified.
    """

    new_circle = Circle(int(x), int(y), int(radius), color, filled)
    window.draw(new_circle)
    return new_circle


def ellipse(x, y, width, height, color=None, filled=True):
    """
    Creates an eclipse centered at the given x, y coordinates. Width, height,
    color, filled status and stroke status can be optionally modified.
    """

    new_ellipse = Ellipse(
        int(x), int(y), int(width), int(height), color, filled)
    window.draw(new_ellipse)
    return new_ellipse


def polygon(vertices, color=None, filled=True):
    """
    Creates a polygon whose points are given in a list as the first argument.
    Width, height, color, filled status and stroke status can be optionally
    modified.
    """

    new_polygon = Polygon(vertices, color, filled)
    window.draw(new_polygon)
    return new_polygon


def regPolygon(x, y, sides, length, color=None, filled=True):
    """
    Creates a regular polygon with the given number of sides at the given x, y
    coordinates. Each side's length is determined by the given length. Color and filled
    determine the color of the shape and if it is filled or not.
    """

    new_reg_polygon = RegPolygon(
        int(x), int(y), int(sides), int(length), color, filled)
    window.draw(new_reg_polygon)
    return new_reg_polygon


def arc(x, y, width, height, startAngle, endAngle,
        color=None, filled=True):
    """
    Creates an arc centered at the given (x,y) coordinates. The width, height,
    start angle, end angle, color, filled status and stoke status can be
    optionally modified. The start and end angle degrees refer to a circle where 0 is on
    the left side of the screen, 90 is at the top, 180 is on the right and 270 is at the bottom.
    """

    new_arc = Arc(
        int(x), int(y), int(width), int(height), startAngle, (endAngle - startAngle), color, filled)
    window.draw(new_arc)
    return new_arc

# It would be nice to have the option to not specify the width
# and height. Is there a way to get the default width/height of image?


def image(x, y, imagePath, width=None, height=None):
    """
    Draws an image with upper left corner at the given (x,y) coordinates.
    The image should be located at imagePath, and the desired width and
    height of the image should be specified in their respective arguments.
    """

    global window
    img = Image(int(x), int(y), imagePath, width, height)
    window.draw(img)
    return img


def fill(r=None, g=None, b=None):
    """
    Sets the color to fill shapes with.
    """

    window.setDefaultColor(color(r, g, b))


def background(r=None, g=None, b=None):
    """
    Sets the background color of the window.
    """

    window.setBackgroundColor(color(r, g, b))

#---------------------------------------------------------------
#-----------Mouse functions-------------------------------------


def mouseX():
    """Returns x coordinate of the mouse"""
    return window.mouseX


def mouseY():
    """Returns y coordinate of the mouse"""
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


def keyPressed():
    """Returns if key was pressed or not."""
    return window.keyEventType is KeyEvent.KEY_PRESSED


def keyReleased():
    """Returns if key was released or not."""
    return window.keyEventType is KeyEvent.KEY_RELEASED


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


def loop():
    """
    Tells the draw function to loop when it is called
    """

    global _toLoop
    _toLoop = True


def noLoop():
    """
    Tells the draw function not to loop when it is called,
    or to stop looping if it has already started. This is the default.
    """

    global _toLoop
    _toLoop = False


def frameRate(rate):
    """
    Sets the frame rate value
    """

    global _fr
    _fr = float(rate)


def stroke(r=None, g=None, b=None):
    """
    Sets stroke to true. If a color is given then set the stroke
    color to that color
    """

    window.setStroke(True)
    if r != None:
        window.setStrokeColor(color(r, g, b))


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

    draw()
    redraw()
    while True:
        while _toLoop:
            with window.draw_lock:
                draw()
            redraw()
            time.sleep(1.0 / _fr)


def redraw(delay=0.0):
    """
    Redraws all of the objects on the window. Not sure there is a point to it.
    """

    window.redraw(delay)


def text((x, y), string, font, size, color=None, attribute=PLAIN):
    """
    Draws specified text "string" to the screen at (x, y), with specified font and size
    and optional color and attribute (PLAIN, BOLD, ITALIC)
    """

    newText = Text(int(x), int(y), string, font, int(size), attribute, color)
    window.draw(newText)
    return newText


def color(r, g=None, b=None):
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

    def draw():
        global rectX
        global rectY
        global directionX
        global directionY

        clear()
        vertices = [(250, 250), (250, 370), (360, 340), (360, 250)]

        fill(red)
        stroke(blue)
        rect(rectX, rectY, 200, 150, filled=True)
        line(150, 10, 200, 10)
        fill(pink)
        ellipse(10, 150, 200, 100, filled=True)

        polygon(vertices, filled=False)
        regPolygon(10, 300, 3, 25, filled=False)
        arc(300, 100, 100, 100, 0, 170, filled=False)
        circle(0, 0, 30, filled=False)

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

        text((200, 200), 'Hello, world', 'Times New Roman', 50, black)

        # image(200, 200, './puppy.jpg', 50, 50)

    def drawImage():
        # image(0, 0, './puppy.jpg')
        image(0, 0, 'http://imgs.xkcd.com/comics/steroids.png')

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
