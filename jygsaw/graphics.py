# graphics.py
# by Balkcom's Army
#
# These are the functions for end-users for Jygsaw.

from graphicsobject import *
from graphicswindow import *
from shape import *
from group import *
from image import *
from text import *
from java.awt import Color
from java.awt.event import MouseEvent, KeyEvent


#-----------------------Canvas Functions------------------------
def canvas(width=400, height=400, window_title='Jygsaw Canvas', background=WHITE):
    """
    Creates and returns a new Jygsaw
    :py:class:`~jygsaw.graphicswindow.GraphicsWindow` and
    :py:class:`~jygsaw.graphicswindow.Canvas`.

    :param width: Width of the :py:class:`~jygsaw.graphicswindow.Canvas`.
    :type width: int, optional
    :param height: Height of the :py:class:`~jygsaw.graphicswindow.Canvas`.
    :type height: int, optional
    :param window_title: Title of the window.
    :type window_title: str, optional
    :param background: Color of the background.
    :type background: :py:class:`Color`, optional
    :rtype: :py:class:`~jygsaw.graphicswindow.GraphicsWindow`
    """
    global window
    window = GraphicsWindow(window_title, int(width), int(height), background)
    window.set_visible(True)
    return window


def width():
    """
    Returns the width of the :py:class:`~jygsaw.graphicswindow.Canvas`.

    :rtype: int
    """
    return window.width


def height():
    """
    Returns the height of the :py:class:`~jygsaw.graphicswindow.Canvas`.

    :rtype: int
    """
    return window.height


#----------------------Drawing Functions------------------------
def point(x, y, color=None):
    """
    Draws and returns a :py:class:`~jygsaw.shape.Point`.

    :param x: x-coordinate of point.
    :type x: int
    :param y: y-coordinate of point.
    :type y: int
    :param color: Color of the point. Defaults to the color set by :py:meth:`~jygsaw.graphics.fill`.
    :type color: :py:class:`Color`, optional
    :rtype: :py:class:`~jygsaw.shape.Point`
    """
    new_point = Point(int(x), int(y), color)
    window.draw(new_point)
    return new_point


def line(x1, y1, x2, y2, color=None):
    """
    Draws and returns a :py:class:`~jygsaw.shape.Line` between two points.

    :param x1: x-coordinate of first point.
    :type x: int
    :param y1: y-coordinate of first point.
    :type y: int
    :param x2: x-coordinate of second point.
    :type x: int
    :param y2: y-coordinate of second point.
    :type y: int
    :param color: Color of the line. Defaults to the color set by :py:meth:`~jygsaw.graphics.fill`.
    :type color: :py:class:`Color`, optional
    :rtype: :py:class:`~jygsaw.shape.Line`
    """
    new_line = Line(int(x1), int(y1), int(x2), int(y2), color)
    window.draw(new_line)
    return new_line


def rect(x, y, rectWidth, rectHeight, color=None):
    """
    Draws and returns a :py:class:`~jygsaw.shape.Rectangle`.

    :param x: x-coordinate of upper-left corner.
    :type x: int
    :param y: y-coordinate of upper-left corner.
    :type y: int
    :param color: Color of the rectangle. Defaults to the color set by :py:meth:`~jygsaw.graphics.fill`.
    :type color: :py:class:`Color`, optional
    :rtype: :py:class:`~jygsaw.shape.Rectangle`
    """
    new_rect = Rectangle(
        int(x), int(y), int(rectWidth), int(rectHeight), color)
    window.draw(new_rect)
    return new_rect


def circle(x, y, radius, color=None):
    """
    Draws and returns a :py:class:`~jygsaw.shape.Circle`.

    :param x: x-coordinate of center.
    :type x: int
    :param y: y-coordinate of center.
    :type y: int
    :param radius: Radius of circle.
    :type radius: int
    :param color: Color of the circle. Defaults to the color set by :py:meth:`~jygsaw.graphics.fill`.
    :type color: :py:class:`Color`, optional
    :rtype: :py:class:`~jygsaw.shape.Circle`
    """
    new_circle = Circle(int(x), int(y), int(radius), color)
    window.draw(new_circle)
    return new_circle


def ellipse(x, y, width, height, color=None):
    """
    Draws and returns an :py:class:`~jygsaw.shape.Ellipse`.

    :param x: x-coordinate of center.
    :type x: int
    :param y: y-coordinate of center.
    :type y: int
    :param width: width of ellipse.
    :type width: int
    :param height: height of ellipse.
    :type height: int
    :param color: Color of the ellipse. Defaults to the color set by :py:meth:`~jygsaw.graphics.fill`.
    :type color: :py:class:`Color`, optional
    :rtype: :py:class:`~jygsaw.shape.Ellipse`
    """
    new_ellipse = Ellipse(
        int(x), int(y), int(width), int(height), color)
    window.draw(new_ellipse)
    return new_ellipse


def triangle(x1, y1, x2, y2, x3, y3, color=None):
    """
    Draws and returns a triangular :py:class:`~jygsaw.shape.Polygon`.

    :param x1: x-coordinate of first point.
    :type x: int
    :param y1: y-coordinate of first point.
    :type y: int
    :param x2: x-coordinate of second point.
    :type x: int
    :param y2: y-coordinate of second point.
    :type y: int
    :param x3: x-coordinate of third point.
    :type x: int
    :param y3: y-coordinate of third point.
    :type y: int
    :param color: Color of the point. Defaults to the color set by :py:meth:`~jygsaw.graphics.fill`.
    :type color: :py:class:`Color`, optional
    :rtype: :py:class:`~jygsaw.shape.Polygon`
    """
    vertices = [(x1, y1), (x2, y2), (x3, y2)]

    new_polygon = Polygon(vertices, color)
    window.draw(new_polygon)
    return new_polygon


def polygon(vertices, color=None):
    """
    Draws and returns a :py:class:`~jygsaw.shape.Polygon` determined by a list
    of vertices.

    :param vertices: List of vertices to join to form a polygon.
    :type vertices: list of pairs (2-tuples) of ints
    :param color: Color of the polygon. Defaults to the color set by :py:meth:`~jygsaw.graphics.fill`.
    :type color: :py:class:`Color`, optional
    :rtype: :py:class:`~jygsaw.shape.Polygon`
    """
    new_polygon = Polygon(vertices, color)
    window.draw(new_polygon)
    return new_polygon


def reg_polygon(x, y, sides, length, color=None):
    """
    Draws and returns a regular polygon (:py:class:`~jygsaw.shape.RegPolygon`).

    :param x: x-coordinate of center.
    :type x: int
    :param y: y-coordinate of center.
    :type y: int
    :param sides: Number of sides.
    :type sides: int
    :param length: Length of each side.
    :type length: int
    :param color: Color of the polygon. Defaults to the color set by :py:meth:`~jygsaw.graphics.fill`.
    :type color: :py:class:`Color`, optional
    :rtype: :py:class:`~jygsaw.shape.RegPolygon`
    """
    new_reg_polygon = RegPolygon(
        int(x), int(y), int(sides), int(length), color)
    window.draw(new_reg_polygon)
    return new_reg_polygon


def arc(x, y, width, height, start_angle, end_angle, color=None):
    """
    Draws and returns an :py:class:`~jygsaw.shape.Arc` within a bounding box.

    :param x: x-coordinate of upper-left corner of bounding box.
    :type x: int
    :param y: y-coordinate of upper-left corner of bounding box.
    :type y: int
    :param width: width of bounding box.
    :type width: int
    :param height: height of bounding box.
    :type height: int
    :param start_angle: Starting angle.
    :type start_angle: int
    :param end_angle: Ending angle.
    :type end_angle: int
    :param color: Color of the arc. Defaults to the color set by :py:meth:`~jygsaw.graphics.fill`.
    :type color: :py:class:`Color`, optional
    :rtype: :py:class:`~jygsaw.shape.Arc`

    **Notes**

    The start and end angle degrees refer to a circle where 0 is on the
    left side of the screen, 90 is at the top, 180 is on the right and 270
    is at the bottom.
    """
    new_arc = Arc(
        int(x), int(y), int(width), int(height), start_angle, (end_angle - start_angle), color)
    window.draw(new_arc)
    return new_arc


def image(x, y, path, width=None, height=None):
    """
    Draws and returns an :py:class:`~jygsaw.image.Image`.

    :param x: x-coordinate of upper-left corner.
    :type x: int
    :param y: y-coordinate of upper-left corner.
    :type y: int
    :param path: Internet URL or local file path to the image.
    :type path: str
    :param width: Width of the image. Defaults to image's original width.
    :type width: int, optional
    :param height: Height of the image. Defaults to image's original height.
    :type height: int, optional
    :rtype: :py:class:`~jygsaw.image.Image`

    **Notes**

    The image will fail to be created if the URL or local file path is invalid.
    """
    global window
    img = Image(int(x), int(y), path, width, height)
    window.draw(img)
    return img


#-----------------------Mouse Functions-------------------------
def mouse_x():
    """
    Returns x-coordinate of the mouse with respect to the upper-left corner
    of the Canvas. Starts at 0 and stays at its last coordinate when the mouse
    leaves the Canvas.

    :rtype: int
    """
    return window.mouse_x


def mouse_y():
    """
    Returns y-coordinate of the mouse with respect to the upper-left corner
    of the Canvas. Starts at 0 and stays at its last coordinate when the mouse
    leaves the Canvas.

    :rtype: int
    """
    return window.mouse_y


def mouse_pressed():
    """
    Returns :py:class:`True` if any mouse button is pressed or not, else
    :py:class:`False`.

    :rtype: bool
    """
    return bool(window.mouse_buttons)


def is_button_pressed(button):
    """
    Determines if a mouse button is being pressed.

    :param button: Name of button to test for.
    :type button: int or constant such as ``MouseEvent.BUTTON1``
    :rtype: bool

    **Notes**

    The list of ``MouseEvent`` button constants can be found at the
    `MouseEvent documentation <http://docs.oracle.com/javase/7/docs/api/java/awt/event/MouseEvent.html#getButton()>`_.
    """
    return button in window.mouse_buttons


def on_mouse_press(f):
    """
    Sets the function that runs when the mouse is pressed.

    :param f: Function that runs on mouse press.
    :type f: function
    """
    window.on_mouse_pressed = f


def on_mouse_release(f):
    """
    Sets the function that runs when the mouse is released.

    :param f: Function that runs on mouse release.
    :type f: function
    """
    window.on_mouse_released = f


def on_mouse_click(f):
    """
    Sets the function that runs when the mouse is clicked.

    :param f: Function that runs on mouse click.
    :type f: function
    """
    window.on_mouse_clicked = f


def on_mouse_drag(f):
    """
    Sets the function that runs when the mouse is dragged.

    :param f: Function that runs on mouse drag.
    :type f: function
    """
    window.on_mouse_dragged = f


def on_mouse_move(f):
    """
    Sets the function that runs when the mouse moves.

    :param f: Function that runs on mouse move.
    :type f: function
    """
    window.on_mouse_moved = f


def on_mouse_enter(f):
    """
    Sets the function that runs when the mouse enters the Canvas.

    :param f: Function that runs on mouse enter.
    :type f: function
    """
    window.on_mouse_entered = f


def on_mouse_exit(f):
    """
    Sets the function that runs when the mouse exits the Canvas.

    :param f: Function that runs on mouse exit.
    :type f: function
    """
    window.on_mouse_exited = f


#--------------------Keyboard Functions-------------------------
def key_pressed():
    """
    :py:class:`True` if any key is being pressed, else :py:class:`False`.

    :rtype: bool
    """
    return bool(window.codes_pressed)


def on_key_press(f):
    """
    Sets the function that runs when a key is pressed.

    :param f: Function that runs on key pressed.
    :type f: function
    """
    window.on_key_pressed = f


def on_key_release(f):
    """
    Sets the function that runs when a key is released.

    :param f: Function that runs on key released.
    :type f: function
    """
    window.on_key_released = f


def on_key_type(f):
    """
    Sets the function that runs when a key is typed.

    :param f: Function that runs on key typed.
    :type f: function
    """
    window.on_key_typed = f


def last_key_char():
    """
    Returns the last character that was pressed. Non-ASCII keys
    will be returned as "?".

    :rtype: str
    """
    return window.last_key_char


def last_key_code():
    """
    Returns the last key code that was pressed.

    :rtype: int

    **Notes**

    The codes are of the form ``KeyEvent.VK_KEY``. All the codes can be found at
    the `KeyEvent documentation <http://docs.oracle.com/javase/7/docs/api/java/awt/event/KeyEvent.html#field_summary>`_.
    """
    return window.last_key_code


def is_key_pressed(char):
    """
    Determines if a key is being pressed.

    :param code: Case-insensitive string containing name of key to test.
    :type code: str
    :rtype: bool

    **Notes**

    The names of the keys come from
    `java.awt.event.KeyEvent.getKeyText <http://docs.oracle.com/javase/7/docs/api/java/awt/event/KeyEvent.html#getKeyText(int)>`_
    and change depending on the locale of the user's Java AWT installation.

    Therefore, it is recommended to use
    :py:meth:`~jygsaw.graphics.last_key_code` when testing for non-ASCII keys
    because of this inconsistency across different systems.
    """
    return char.upper() in window.chars_pressed


def is_code_pressed(code):
    """
    Determines if a key is being pressed.

    :param code: Code of the key to test.
    :type code: int
    :rtype: bool

    **Notes**

    The code should be of the form ``KeyEvent.VK_KEY``. All the codes can be found
    at the `KeyEvent documentation <http://docs.oracle.com/javase/7/docs/api/java/awt/event/KeyEvent.html#field_summary>`_.
    """
    return code in window.codes_pressed


#--------------------State Functions----------------------
def fill(r=None, g=None, b=None, a=255):
    """
    Sets the fill color.

    **Notes**

    See :py:meth:`~jygsaw.graphics.color` for how colors are specified.
    """
    window.set_filled(True)
    if r is not None:
        window.set_default_color(color(r, g, b, a))


def no_fill():
    """
    Disables filling geometry. If both :py:meth:`~jygsaw.graphics.no_stroke()`
    and :py:meth:`~jygsaw.graphics.no_fill()` are called, nothing will be drawn
    to the screen.
    """
    window.set_filled(False)


def stroke(r=None, g=None, b=None, a=255):
    """
    Turns on the stroke. If a color is given, then sets the stroke
    to that color.

    **Notes**

    See :py:meth:`~jygsaw.graphics.color` for how colors are specified.
    """
    window.set_stroke(True)
    if r is not None:
        window.set_stroke_color(color(r, g, b, a))


def stroke_width(width):
    """
    Sets the stroke width.

    :param width: Width of stroke in pixels.
    :type width: int
    """
    window.set_stroke_width(width)


def no_stroke():
    """
    Disables drawing the stroke (outline). If both
    :py:meth:`~jygsaw.graphics.no_stroke()` and
    :py:meth:`~jygsaw.graphics.no_fill()` are called, nothing will be drawn to
    the screen.
    """
    window.set_stroke(False)


def background(r=None, g=None, b=None, a=255):
    """
    Sets the background color of the window.

    **Notes**

    See :py:meth:`~jygsaw.graphics.color` for how colors are specified.
    """
    window.set_bg_color(color(r, g, b, a))


def clear():
    """
    Deletes all :py:class:`~jygsaw.graphicsobject.GraphicsObject` objects then
    redraws the Canvas.
    """
    window.clear()


def on_draw(user_draw):
    """
    Sets the Canvas draw function which will be run by
    :py:meth:`~jygsaw.graphics.jygsaw_start`.

    :param user_draw: Function to run when drawing.
    """
    window.on_draw = user_draw


def jygsaw_start(delay=0.0):
    """
    Start the main drawing loop.

    Runs the user-defined draw function set by
    :py:meth:`~jygsaw.graphics.on_draw`. Loop if ``delay`` is non-zero.

    :param delay: Amount of delay in seconds before the Canvas redraws itself.
    :type delay: float, optional
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
    Redraws the :py:class:`~jygsaw.graphicswindow.Canvas`.

    :param delay: Amount of delay in seconds before the Canvas redraws itself.
    :type delay: float, optional
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
        if event.getID() == KeyEvent.KEY_PRESSED and window.on_key_pressed:
            window.on_key_pressed()
        if event.getID() == KeyEvent.KEY_RELEASED and window.on_key_released:
            window.on_key_released()
        if event.getID() == KeyEvent.KEY_TYPED and window.on_key_typed:
            window.on_key_typed()


def text(x, y, string, color=None, attribute=PLAIN):
    """
    Draws text to the screen.

    :param x: x-coordinate of text.
    :type x: int
    :param y: y-coordinate of text.
    :type y: int
    :param string: String of characters to display on-screen.
    :type string: str
    :param color: Color of the text. Defaults to the color set by
        :py:meth:`~jygsaw.graphics.fill`.
    :type color: :py:class:`Color`, optional
    :param attribute: Text style (one of ``PLAIN``, ``BOLD``, or ``ITALIC``).
    :type attribute: int, optional
    :rtype: :py:class:`~jygsaw.text.Text`
    """
    newText = Text(int(x), int(y), string, color, attribute)
    window.draw(newText)
    return newText


def font(font):
    """
    Sets the window font.

    :param font: Name of a font installed on the user's system.
    :type font: str
    """
    window.set_font(font)


def text_size(size):
    """
    Sets the text size.

    :param size: Text size in points.
    :type size: int
    """
    window.set_text_size(size)


def get_colors():
    """
    Returns a list of all the available color constants.

    :rtype: list of :py:class:`Color`
    """
    return GraphicsWindow.colors


def color(r, g=None, b=None, a=255):
    """
    Creates a color object.

    :param r: Gray value, R value, or :py:class:`Color` constant.
    :type r: int or :py:class:`Color`
    :param g: G value of RGB color which will be created. ``b`` must also be given. Defaults to :py:class:`None`.
    :type g: int
    :param b: B value of RGB color which will be created. ``g`` must also be given. Defaults to :py:class:`None`.
    :type b: int
    :param a: Optional alpha value of the RBG color which will be created.
    :type a: int
    :rtype: :py:class:`Color`

    **Notes**

    If ``r`` is the only value passed and is a color constant (one of ``BLACK``,
    ``BLUE``, ``CYAN``, ``DARK_GRAY``, ``GRAY``, ``GREEN``, ``LIGHT_GRAY``,
    ``MAGENTA``, ``ORANGE``, ``PINK``, ``RED``, ``WHITE``, ``YELLOW``),
    then that color is simply returned.

    If ``r`` is the only value passed and it's an integer, all three values of
    ``r``, ``g``, ``b`` are set to ``r``.

    If ``r``, ``g``, and ``b`` all have integer values then ``r``, ``g``, ``b``
    will take the corresponding values.
    """
    if g is None or b is None:
        assert r is not None and g is None and b is None, \
            "color takes exactly 1, 3, or 4 parameters"
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
            "color takes exactly 1, 3, or 4 parameters"
        assert isinstance(r, int) and isinstance(
            g, int) and isinstance(b, int), "color takes 3 integers"
        return Color(r, g, b, a)
