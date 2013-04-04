"""
A simple graphics library that wraps around Java's Swing library.
It's robust, easy to use, and most importantly easy to learn for
both new and old programmers alike.
"""
from graphicsobject import *
from graphicswindow import *
from shape import *
from group import *
from image import *
from text import *
from java.awt import Color


rectX = 0  # Just used for testing - delete or move eventually
rectY = 0  # Just used for testing - delete or move eventually
directionX = 1  # Just used for testing - delete or move eventually
directionY = 1  # Just used for testing - delete or move eventually
_fr = 60.0  # Frame Rate


def canvas(width=400, height=400, window_title='Jygsaw Canvas', background=white):
    """
    Creates and returns a new Jygsaw :py:class:`~jygsaw.graphicswindow.GraphicsWindow` and
    :py:class:`~jygsaw.graphicswindow.Canvas`.

    Keyword arguments:

    * *width* -- Width of the canvas in the window. Defaults to 400.
    * *height* -- Height of the canvas in the window. Defaults to 400.
    * *window_title* -- Title of the window. Defaults to 'Jygsaw Canvas'.
    * *background* -- Color of the canvas's background. Defaults to white.
    """
    global window
    window = GraphicsWindow(window_title, int(width), int(height), background)
    window.setVisible(True)
    return window


def width():
    """
    Returns the width of the window's canvas.
    """
    return window.width


def height():
    """
    Returns the height of the window's canvas.
    """
    return window.height


def point(x, y, color=None):
    """
    Creates, draws on the canvas and returns a :py:class:`~jygsaw.shape.Point`
    at (x,y). You can optionally set the color.

    Keyword Arguments:

    * *color* -- Color of the point. Defaults to fill color.
    """
    new_point = Point(int(x), int(y), color)
    window.draw(new_point)
    return new_point


def line(x1, y1, x2, y2, color=None):
    """
    Creates, draws on the canvas and returns a :py:class:`~jygsaw.shape.Line`
    between coordinates x1, y1, and x2, y2. You can optionally set the color.

    Keyword Arguments:

    * *color* -- Color of the line. Defaults to fill color.
    """
    new_line = Line(int(x1), int(y1), int(x2), int(y2), color)
    window.draw(new_line)
    return new_line


def rect(x, y, rectWidth, rectHeight, color=None):
    """
    Creates, draws on the canvas and returns a :py:class:`~jygsaw.shape.Rect`
    with the upper left corner at the given x, y coordinates. You can optionally set the color.

    Keyword Arguments:

    * *color* -- Color of the rectangle. Defaults to fill color.
    """
    new_rect = Rectangle(
        int(x), int(y), int(rectWidth), int(rectHeight), color)
    window.draw(new_rect)
    return new_rect


def circle(x, y, radius, color=None):

    """
    Creates, draws on the canvas and returns a :py:class:`~jygsaw.shape.Circle`
    centered at the given x, y coordinates with the given radius.
    The color can be optionally set.

    Keyword Arguments:

    * *color* -- Color of the circle. Defaults to fill color.
    """
    new_circle = Circle(int(x), int(y), int(radius), color)
    window.draw(new_circle)
    return new_circle


def ellipse(x, y, width, height, color=None):

    """
    Creates, draws on the canvas and returns an :py:class:`~jygsaw.shape.Ellipse`
    centered at the given x, y coordinates, with the given width and height.
    Color can be optionally set.

    Keyword Arguments:

    * *color* -- Color of the ellipse. Defaults to fill color.
    """
    new_ellipse = Ellipse(
        int(x), int(y), int(width), int(height), color)
    window.draw(new_ellipse)
    return new_ellipse


def triangle(x1, y1, x2, y2, x3, y3, color=None):
    """
    Creates, draws on the canvas and returns a :py:class:`~jygsaw.shape.Polygon`
    whose points create a triangle. The function takes in six variables describing
    the coordinates of the triangle to be drawn. Color can be optionally
    set.

    Keyword Arguments:

    * *color* -- Color of the polygon. Defaults to fill color.

    """
    vertices = [(x1, y1), (x2, y2), (x3, y2)]

    new_polygon = Polygon(vertices, color)
    window.draw(new_polygon)
    return new_polygon


def polygon(vertices, color=None):
    """
    Creates, draws on the canvas and returns a :py:class:`~jygsaw.shape.Polygon`
    whose points are given in a list as the first argument.
    Color can be optionally set.

    Keyword Arguments:

    * *color* -- Color of the polygon. Defaults to fill color.
    """
    new_polygon = Polygon(vertices, color)
    window.draw(new_polygon)
    return new_polygon


def regPolygon(x, y, sides, length, color=None):
    """
    Creates, draws on the canvas and returns a :py:class:`~jygsaw.shape.Polygon`
    with the given number of sides at the given x, y coordinates. Each side's
    length is determined by the given length. The color can be optionally set.

    Keyword Arguments:

    * *color* -- Color of the regular polygon. Defaults to fill color.
    """
    new_reg_polygon = RegPolygon(
        int(x), int(y), int(sides), int(length), color)
    window.draw(new_reg_polygon)
    return new_reg_polygon


def arc(x, y, width, height, startAngle, endAngle,
        color=None):
    """
    Creates, draws on the canvas, and returns an :py:class:`~jygsaw.shape.Arc`
    centered at the given x, y coordinates. The width, height, start angle,
    end angle, set the arc's respective attributes.

    The start and end angle degrees refer to a circle where 0 is on the
    left side of the screen, 90 is at the top, 180 is on the right and 270
    is at the bottom.

    Keyword Arguments:

    * *color* -- Color of the arc. Defaults to fill color.
    """
    new_arc = Arc(
        int(x), int(y), int(width), int(height), startAngle, (endAngle - startAngle), color)
    window.draw(new_arc)
    return new_arc


def image(x, y, imagePath, width=None, height=None):
    """
    Creates, draws on the canvas, and returns an :py:class:`~jygsaw.image.Image`
    with upper left corner at the given x, y coordinates.

    The image should be located on your computer or online
    at the location specified by imagePath. The width and height of the
    image can be optionally set, otherwise the image's original width and height
    will be used.

    Keyword Arguments:

    * *width* -- Width of the image. Defaults to image's original width.
    * *height* -- Height of the image. Defaults to image's original height.
    """
    global window
    img = Image(int(x), int(y), imagePath, width, height)
    window.draw(img)
    return img


def fill(r=None, g=None, b=None, a=255):
    """
    Sets the color to fill shapes with.

    See :py:meth:`~jygsaw.graphics.color` for how the color values are handled.
    """
    window.setFilled(True)
    if r is not None:
        window.setDefaultColor(color(r, g, b, a))


def noFill():
    """ Sets filled to False."""
    window.setFilled(False)


def background(r=None, g=None, b=None, a=255):
    """
    Sets the background color of the window.

    See :py:meth:`~jygsaw.graphics.color` for how the color values are handled.
    """
    window.setBackgroundColor(color(r, g, b, a))

#---------------------------------------------------------------
#-----------Mouse Methods-------------------------------------


def mouseX():
    """Returns x coordinate of the mouse."""
    return window.mouseX


def mouseY():
    """Returns y coordinate of the mouse."""
    return window.mouseY


def mousePressed():
    """Returns whether the mouse was pressed or not."""
    return window.mouseEventType == MouseEvent.MOUSE_PRESSED \
        or window.mouseEventType == MouseEvent.MOUSE_DRAGGED


def mouseReleased():
    """Returns whether the mouse was released or not."""
    return window.mouseEventType == MouseEvent.MOUSE_RELEASED


def mouseClicked():
    """Returns whether the mouse was clicked or not."""
    return window.mouseEventType == MouseEvent.MOUSE_CLICKED


def mouseDragged():
    """Returns whether the mouse was dragged or not."""
    return window.mouseEventType == MouseEvent.MOUSE_DRAGGED


def mouseMoved():
    """Returns whether the mouse was moved or not."""
    return window.mouseEventType == MouseEvent.MOUSE_MOVED


def mouseEntered():
    """Returns whether the mouse has entered the window or not."""
    return window.mouseEventType == MouseEvent.MOUSE_ENTERED


def mouseExited():
    """Returns whether the mouse has exited the window or not."""
    return window.mouseEventType == MouseEvent.MOUSE_EXITED


def onMousePress(mousePressed):
    """
    Sets the window's onMousePressed variable to be the user
    defined mousePressed function. It will then be called by
    the window's mouse listener when the event occurs.
    """
    window.onMousePressed = mousePressed


def onMouseRelease(mouseReleased):
    """
    Sets the window's onMouseReleased variable to be the user
    defined mouseReleased function. It will then be called by the
    window's mouse listener when the event occurs.
    """
    window.onMouseReleased = mouseReleased


def onMouseClick(mouseClicked):
    """
    Sets the window's onMouseClicked variable to be the user
    defined mouseClicked function. It will then be called by the
    window's mouse listener when the event occurs.
    """
    window.onMouseClicked = mouseClicked


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
    VK_[CODE], from the key event library. All the codes can be found at
    http://docs.oracle.com/javase/1.4.2/docs/api/java/awt/event/KeyEvent.html.
    """
    return window.lastKeyCode


def isKeyPressed(char):
    """
    Returns whether *char* is being pressed.
    """
    return char in window.charsPressed


def isCodePressed(code):
    """
    Returns whether *code* is being pressed.
    """
    return code in window.codesPressed

#---------------------------------------------------------


def frameRate(rate):
    """Sets the frame rate value."""
    global _fr
    _fr = float(rate)


def stroke(r=None, g=None, b=None, a=255):
    """
    Sets stroke to true. If a color is given then set the stroke
    color to that color.

    See :py:meth:`~jygsaw.graphics.color` for how color values are handled.

    Keyword Arguments:

    * *r* -- R value of the RGB stroke color. Defaults to None.
    * *g* -- G value of the RGB stroke color. Defaults to None.
    * *b* -- B value of the RGB stroke color. Defaults to None.
    * *a* -- Alpha value of the RGB stroke color. Default to 255.
    """
    window.setStroke(True)
    if r is not None:
        window.setStrokeColor(color(r, g, b, a))


def strokeWidth(w):
    window.setStrokeWidth(w)


def noStroke():
    """Sets stroke to false."""
    window.setStroke(False)


def clear():
    """Clears the window of all objects and redraws screen."""
    window.clear()


def onDraw(user_draw):
    """Callback function which calls the user defined draw function."""
    window.onDraw = user_draw


def jygsawMain(delay=0.0):
    """Repeatedly runs user-defined draw function."""
    window.mainRunning = True
    if delay > 0:
        while True:
            "JygsawMain"
            sleep(delay)
            window.frame.contentPane.repaint()
    else:
        window.frame.contentPane.repaint()


def refresh(delay=0.0):
    """
    Redraws all of the objects on the window.

    A delay between redrawing can be optionally set.

    Keyword Arguments:

    * *delay* -- Delay before the window calls repaint. Defaults to 0.0.
    """
    assert(not window.mainRunning)
    window.redraw(delay)
    while not window.eventQueue.empty():
        event = window.eventQueue.get()
        if event.getID() == MouseEvent.MOUSE_PRESSED and window.onMousePressed:
            window.onMousePressed()
        if event.getID() == MouseEvent.MOUSE_RELEASED and window.onMouseReleased:
            window.onMouseReleased()
        if event.getID() == MouseEvent.MOUSE_CLICKED and window.onMouseClicked:
            window.onMouseClicked()
        if event.getID() == MouseEvent.MOUSE_DRAGGED and window.onMouseDragged:
            window.onMouseDragged()
        if event.getID() == MouseEvent.MOUSE_MOVED and window.onMouseMoved:
            window.onMouseMoved()
        if event.getID() == MouseEvent.MOUSE_ENTERED and window.onMouseEntered:
            window.onMouseEntered()
        if event.getID() == MouseEvent.MOUSE_EXITED and window.onMouseExited:
            window.onMouseExited()


def text(x, y, string, color=None, attribute=PLAIN):
    """
    Draws specified text "string" to the screen at (x, y), with
    specified font and size and optional color and attribute
    (PLAIN, BOLD, ITALIC)

    Keyword Arguments:

    * *color* -- Color of the text. Defaults to fill color.
    * *attribute* -- Specifies if text is PLAIN, BOLD, or ITALIC. Defaults to PLAIN.
    """
    newText = Text(int(x), int(y), string, color, attribute)
    window.draw(newText)
    return newText


def font(f):
    """Sets the font to the given font in 'f'."""
    window.setFont(f)


def textSize(s):
    """Sets the text size to the given size in 's'."""
    window.setTextSize(s)


def color(r, g=None, b=None, a=255):
    """
    Returns a color based on the values passed to the function.

    If *r* is the only value passed and it's the name of a color,
    then that color will be created and returned.

    If *r* is the only value passed and it's an integer, a color
    will be created and returned where all three values of the
    color's r, g, b are the same as *r*.

    If *r*, *g*, and *b* all have values then a color will be
    created and returned with the corresponding r, g, b values.


    Otherwise an assert is thrown.

    Keyword Arguments:

    * *g* -- G value of RGB color which will be created. b must also be given. Defaults to None.
    * *b* -- B value of RGB color which will be created. g must also be given. Defaults to None.
    * *a* -- Alpha value of the RBG color which will be created. a does not have to be given, it will default to 255.
    """
    if g is None or b is None:
        assert r is not None and g is None and b is None, \
            "color takes exactly 1 or 3 or 4 parameters"
        if isinstance(r, int):
            # Will create color (r, r, r)
            return Color(r, r, r, a)
        if isinstance(r, Color):
            return r
        else:
            # r is of an unrecognized type
            pass
    else:
        assert r is not None and g is not None and b is not None, \
            "color takes exactly 1 or 3 or 4 parameters"
        assert isinstance(r, int) and isinstance(
            g, int) and isinstance(b, int), "color takes 3 integers"
        return Color(r, g, b, a)
