"""
A simple graphics library that wraps around Java's Swing library.
It's easy to use, and most importantly easy to learn for
both new and old programmers alike.
"""
from graphicsobject import *
from graphicswindow import *
from shape import *
from group import *
from image import *
from text import *
from java.awt import Color
from java.awt.event import MouseEvent

rectX = 0  # Just used for testing - delete or move eventually
rectY = 0  # Just used for testing - delete or move eventually
directionX = 1  # Just used for testing - delete or move eventually
directionY = 1  # Just used for testing - delete or move eventually
_fr = 60.0  # Frame Rate


def canvas(width=400, height=400, window_title='Jygsaw Canvas', background=WHITE):
    """
    Creates and returns a new Jygsaw :py:class:`~jygsaw.graphicswindow.GraphicsWindow` and
    :py:class:`~jygsaw.graphicswindow.Canvas`.

    Keyword arguments:

    * *width* Width of the canvas in the window. Defaults to 400.
    * *height* Height of the canvas in the window. Defaults to 400.
    * *window_title* Title of the window. Defaults to 'Jygsaw Canvas'.
    * *background* Color of the canvas's background. Defaults to white.
    """
    global window
    window = GraphicsWindow(window_title, int(width), int(height), background)
    window.set_visible(True)
    return window


def width():
    """Returns the width of the window's canvas."""
    return window.width


def height():
    """Returns the height of the window's canvas."""
    return window.height


def point(x, y, color=None):
    """
    Creates, draws on the canvas and returns a :py:class:`~jygsaw.shape.Point`
    at x, y. You can optionally set the color.

    Keyword Arguments:

    * *color* Color of the point. Defaults to the color set by the method :py:meth:`~jygsaw.graphics.fill`.
    """
    new_point = Point(int(x), int(y), color)
    window.draw(new_point)
    return new_point


def line(x1, y1, x2, y2, color=None):
    """
    Creates, draws on the canvas and returns a :py:class:`~jygsaw.shape.Line`
    between coordinates x1, y1, and x2, y2. You can optionally set the color.

    Keyword Arguments:

    * *color* Color of the line. Defaults to the color set by the method :py:meth:`~jygsaw.graphics.fill`.
    """
    new_line = Line(int(x1), int(y1), int(x2), int(y2), color)
    window.draw(new_line)
    return new_line


def rect(x, y, rectWidth, rectHeight, color=None):
    """
    Creates, draws on the canvas and returns a :py:class:`~jygsaw.shape.Rect`
    with the upper left corner at the given x, y coordinates. You can optionally set the
    color.

    Keyword Arguments:

    * *color* Color of the rectangle. Defaults to the color set by the method :py:meth:`~jygsaw.graphics.fill`.
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

    * *color* Color of the circle. Defaults to the color set by the method :py:meth:`~jygsaw.graphics.fill`.
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

    * *color* Color of the ellipse. Defaults to the color set by the method :py:meth:`~jygsaw.graphics.fill`.
    """
    new_ellipse = Ellipse(
        int(x), int(y), int(width), int(height), color)
    window.draw(new_ellipse)
    return new_ellipse


def triangle(x1, y1, x2, y2, x3, y3, color=None):
    """
    Creates, draws on the canvas and returns a :py:class:`~jygsaw.shape.Polygon`
    whose points create a triangle. The function takes in six variables describing
    the coordinates of the triangle to be drawn. Color can be optionally set.

    Keyword Arguments:

    * *color* Color of the point. Defaults to the color set by the method :py:meth:`~jygsaw.graphics.fill`.

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

    * *color* Color of the polygon. Defaults to the color set by the method :py:meth:`~jygsaw.graphics.fill`.
    """
    new_polygon = Polygon(vertices, color)
    window.draw(new_polygon)
    return new_polygon


def reg_polygon(x, y, sides, length, color=None):
    """
    Creates, draws on the canvas and returns a :py:class:`~jygsaw.shape.RegPolygon`
    with the given number of sides at the given x, y coordinates. Each side's
    length is determined by the given length. The color can be optionally set.

    Keyword Arguments:

    * *color* Color of the point. Defaults to the color set by the method :py:meth:`~jygsaw.graphics.fill`.
    """
    new_reg_polygon = RegPolygon(
        int(x), int(y), int(sides), int(length), color)
    window.draw(new_reg_polygon)
    return new_reg_polygon


def arc(x, y, width, height, startAngle, endAngle, color=None):
    """
    Creates, draws on the canvas, and returns an :py:class:`~jygsaw.shape.Arc`
    whose bounding box's top left corner is at the given x, y coordinates. The width,
    height, start angle, end angle, set the arc's respective attributes.

    The start and end angle degrees refer to a circle where 0 is on the
    left side of the screen, 90 is at the top, 180 is on the right and 270
    is at the bottom.

    Keyword Arguments:

    * *color* Color of the point. Defaults to the color set by the method :py:meth:`~jygsaw.graphics.fill`.
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

    * *width* Width of the image. Defaults to image's original width.
    * *height* Height of the image. Defaults to image's original height.
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
    window.set_filled(True)
    if r is not None:
        window.set_default_color(color(r, g, b, a))


def no_fill():
    """ Sets library variable _filled to False, so that shapes are drawn as unfilled."""
    window.set_filled(False)


def background(r=None, g=None, b=None, a=255):
    """
    Sets the background color of the window.

    See :py:meth:`~jygsaw.graphics.color` for how the color values are handled.
    """
    window.set_bg_color(color(r, g, b, a))

#---------------------------------------------------------------
#-----------Mouse Methods-------------------------------------


def mouse_x():
    """Returns x coordinate of the mouse."""
    return window.mouse_x


def mouse_y():
    """Returns y coordinate of the mouse."""
    return window.mouse_y


def mouse_pressed():
    """Returns whether the mouse was pressed or not."""
    return (window.mouse_event_type == MouseEvent.MOUSE_PRESSED or
            window.mouse_event_type == MouseEvent.MOUSE_DRAGGED)


def mouse_released():
    """Returns whether the mouse was released or not."""
    return window.mouse_event_type == MouseEvent.MOUSE_RELEASED


def mouse_clicked():
    """Returns whether the mouse was clicked or not."""
    return window.mouse_event_type == MouseEvent.MOUSE_CLICKED


def mouse_dragged():
    """Returns whether the mouse was dragged or not."""
    return window.mouse_event_type == MouseEvent.MOUSE_DRAGGED


def mouse_moved():
    """Returns whether the mouse was moved or not."""
    return window.mouse_event_type == MouseEvent.MOUSE_MOVED


def mouse_entered():
    """Returns whether the mouse has entered the window or not."""
    return window.mouse_event_type == MouseEvent.MOUSE_ENTERED


def mouse_exited():
    """Returns whether the mouse has exited the window or not."""
    return window.mouse_event_type == MouseEvent.MOUSE_EXITED


def on_mouse_press(mousePressed):
    """
    Sets the window's on_,ouse_pressed variable to be the user
    defined mousePressed function. This function will then be called by
    the window's mouse listener when the mouse event occurs.
    """
    window.on_mouse_pressed = mousePressed


def on_mouse_release(mouseReleased):
    """
    Sets the window's on_mouse_released variable to be the user
    defined mouseReleased function. This function will then be called by the
    window's mouse listener when the mouse event occurs.
    """
    window.on_mouse_released = mouseReleased


def on_mouse_click(mouseClicked):
    """
    Sets the window's on_mouse_clicked variable to be the user
    defined mouseClicked function. This function will then be called by the
    window's mouse listener when the mouse event occurs.
    """
    window.on_mouse_clicked = mouseClicked


def on_mouse_drag(mouseDragged):
    """
    Sets the window's on_mouse_dragged variable to be the user
    defined mouseDragged function. This function will then be called by the
    window's mouse listener when the mouse event occurs.
    """
    window.on_mouse_dragged = mouseDragged


def on_mouse_move(mouseMoved):
    """
    Sets the window's on_mouse_moved variable to be the user
    defined mouseMoved function. This function will then be called by the window's
    mouse listener when the mouse event occurs.
    """
    window.on_mouse_moved = mouseMoved


def onMouseEnter(mouseEntered):
    """
    Sets the window's on_mouse_entered variable to be the user
    defined mouseEntered function. This function will then be called by the
    window's mouse listener when the mouse event occurs.
    """
    window.on_mouse_entered = mouseEntered


def on_mouse_exit(mouseExited):
    """
    Sets the window's on_mouse_exited variable to be the user
    defined mouseExited function. This function will then be called by the
    window's mouse listener when the mouse event occurs.
    """
    window.on_mouse_exited = mouseExited

#---------------------------------------------------------------
#--------------------Keyboard Methods---------------------------


def key_pressed():
    """Returns if a key was pressed or not."""
    return window.key_event_type is KeyEvent.KEY_PRESSED


def key_released():
    """Returns if a key was released or not."""
    return window.key_event_type is KeyEvent.KEY_RELEASED


def on_key_press(keyPressed):
    """
    Sets the window's on_key_pressed variable to be the user
    defined keyPressed function. This function will then be called by the
    window's key listener when the key event occurs.
    """
    window.on_key_pressed = keyPressed


def on_key_release(keyReleased):
    """
    Sets the window's on_key_released variable to be the user
    defined keyReleased function. This function will then be called by the
    window's key listener when the key event occurs.
    """
    window.on_key_released = keyReleased


def on_key_type(keyTyped):
    """
    Sets the window's on_key_typed variable to be the user
    defined keyTyped function. This function will then be called by the
    window's key listener when the key event occurs.
    """
    window.on_key_typed = keyTyped


def last_key_char():
    """
    Returns the last key character that was pressed. Non-ascii keys
    will return a question mark.
    """
    return window.last_key_char


def last_key_code():
    """
    Returns the last key code that was pressed. Comparisons with these codes should be
    of the form VK_[CODE], from the key event library. All the codes can be found at
    http://docs.oracle.com/javase/1.4.2/docs/api/java/awt/event/KeyEvent.html.
    """
    return window.last_key_code


def is_key_pressed(char):
    """
    Returns whether *char* is being pressed.
    isKeyPressed() is case-INSENSITIVE
    """
    return char.upper() in window.chars_pressed


def is_code_pressed(code):
    """Returns whether *code* is being pressed."""
    return code in window.codesPressed

#---------------------------------------------------------
#--------------------State Methods------------------------


def frame_rate(rate):
    """Sets the frame rate value."""
    global _fr
    _fr = float(rate)


def stroke(r=None, g=None, b=None, a=255):
    """
    Sets stroke to true. If a color is given then sets the stroke
    color to that color.

    See :py:meth:`~jygsaw.graphics.color` for how color values are handled.

    Keyword Arguments:

    * *r* R value of the RGB stroke color. Defaults to None.
    * *g* G value of the RGB stroke color. Defaults to None.
    * *b* B value of the RGB stroke color. Defaults to None.
    * *a* Alpha value of the RGB stroke color. Default to 255.
    """
    window.set_stroke(True)
    if r is not None:
        window.set_stroke_color(color(r, g, b, a))


def stroke_width(w):
    """Sets the stroke width."""
    window.set_stroke_width(w)


def no_stroke():
    """Sets stroke to False."""
    window.set_stroke(False)


def clear():
    """Clears the window of all objects and redraws screen."""
    window.clear()


def on_draw(user_draw):
    """
    Sets the window's on_draw variable to be the user
    defined draw function. This function will then be called by the main loop of the program in :py:meth:`jygsaw.graphics.jygsawMain`.
    """
    window.on_draw = user_draw


def jygsaw_start(delay=0.0):
    """
    Main loop of the program.
    Repeatedly runs the user-defined draw function that is passed to :py:meth:`jygsaw.graphics.on_draw`
    """
    window.main_running = True
    if delay > 0:
        while True:
            sleep(delay)
            window.frame.contentPane.repaint()
    else:
        window.frame.contentPane.repaint()


def refresh(delay=0.0):
    """
    Redraws all of the objects on the window.

    A delay between redrawing can be optionally set.

    Keyword Arguments:

    * *delay* Delay before the window calls repaint. Defaults to 0.0.
    """
    assert(not window.main_running)
    window.redraw(delay)
    while not window.event_queue.empty():
        event = window.event_queue.get()
        if event.getID() == MouseEvent.MOUSE_PRESSED and window.on_mouse_pressed:
            window.on_mouse_pressed()
        if event.getID() == MouseEvent.MOUSE_RELEASED and window.on_mouse_released:
            window.on_mouse_released()
        if event.getID() == MouseEvent.MOUSE_CLICKED and window.on_mouse_clicked:
            window.on_mouse_clicked()
        if event.getID() == MouseEvent.MOUSE_DRAGGED and window.on_mouse_dragged:
            window.on_mouse_dragged()
        if event.getID() == MouseEvent.MOUSE_MOVED and window.on_mouse_moved:
            window.on_mouse_moved()
        if event.getID() == MouseEvent.MOUSE_ENTERED and window.on_mouse_entered:
            window.on_mouse_entered()
        if event.getID() == MouseEvent.MOUSE_EXITED and window.on_mouse_exited:
            window.on_mouse_exited()


def text(x, y, string, color=None, attribute=PLAIN):
    """
    Draws specified text "string" to the screen at coordinates x, y, with
    specified font and size, and optional color and attribute
    (PLAIN, BOLD, ITALIC)

    Keyword Arguments:

    * *color* Color of the text. Defaults to the color set by method :py:meth:`~jygsaw.graphics.fill`.
    * *attribute* Specifies if text is PLAIN, BOLD, or ITALIC. Defaults to PLAIN.
    """
    newText = Text(int(x), int(y), string, color, attribute)
    window.draw(newText)
    return newText


def font(f):
    """Sets the window font to the font specified by *f*."""
    window.set_font(f)


def text_size(s):
    """Sets the text size to size specified by *s*."""
    window.set_text_size(s)


def get_colors():
    """Returns a list of all the colors imported from java.awt."""
    window.colors


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

    * *g*: G value of RGB color which will be created. b must also be given. Defaults to None.
    * *b*: B value of RGB color which will be created. g must also be given. Defaults to None.
    * *a*: Alpha value of the RBG color which will be created. a does not have to be given, it will default to 255.
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
