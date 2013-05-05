"""
Exports GraphicsWindow and Canvas. A Canvas is created and attached to a
GraphicsWindow on window creation. A window holds the drawing canvas.
"""

from __future__ import with_statement
from java.awt.event import ActionListener, KeyListener
from java.awt import Color, Dimension, RenderingHints
from javax.swing import JFrame, JPanel
from javax.swing.event import MouseInputListener
from javax.swing import SwingUtilities
from warnings import warn
from image import *
from group import *
from sets import Set
from shape import *
from text import *
from time import sleep
from Queue import Queue
from java.awt.Color import (BLACK, BLUE, CYAN, DARK_GRAY,
                            GRAY, GREEN, LIGHT_GRAY, MAGENTA,
                            ORANGE, PINK, RED, WHITE, YELLOW)


# the -O switch can't be used with jython, which is used to turn off __debug__
# so we use debug instead
debug = False


class GraphicsWindow(ActionListener, KeyListener, MouseInputListener):
    """
    Creates a :py:class:`~jygsaw.graphicswindow.GraphicsWindow` with a
    :py:class:`~jygsaw.graphicswindow.Canvas` object that can be drawn on.
    Takes a title, window width, and window height.
    An optional background color can be specified.
    """
    colors = [BLACK, BLUE, CYAN, DARK_GRAY, GRAY, GREEN,
              LIGHT_GRAY, MAGENTA, ORANGE, PINK, RED, WHITE, YELLOW]

    def __init__(self, title, w, h, bg_color=WHITE):
        assert w > 0, "GraphicsWindow width must be greater than zero"
        assert h > 0, "GraphicsWindow height must be greater than zero"

        self.objs = []  # List of GraphicsObjects
        self.bg_color = bg_color

        self.frame = JFrame(
            title, defaultCloseOperation=JFrame.EXIT_ON_CLOSE,
            size=(w, h))

        self.frame.setLocationRelativeTo(None)
        self.frame.contentPane = Canvas(self, self.objs, self.bg_color)
        self.frame.contentPane.setPreferredSize(Dimension(w, h))

        self.frame.addMouseListener(self)
        self.frame.addMouseMotionListener(self)
        self.frame.addKeyListener(self)

        # MouseEvent attributes
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_buttons = Set()

        # Mouse callbacks
        self.on_mouse_clicked = None
        self.on_mouse_dragged = None
        self.on_mouse_moved = None
        self.on_mouse_pressed = None
        self.on_mouse_released = None
        self.on_mouse_exited = None
        self.on_mouse_entered = None

        # Key callbacks
        self.on_key_pressed = None
        self.on_key_released = None
        self.on_key_typed = None

        # Key values
        self.last_key_char = None
        self.last_key_code = None

        self.chars_pressed = Set()
        self.codes_pressed = Set()

        # Event queue
        self.event_queue = Queue()
        self.main_running = False

        # not needed, user_draw is called directly from on_draw
        self.on_draw = None

    def set_visible(self, visible):
        """Sets the window to visible."""
        assert isinstance(visible, bool), "Variable is not a boolean."
        self.frame.pack()
        self.frame.visible = visible

    def draw(self, *params):
        """
        Takes any number of :py:class:`~jygsaw.graphicsobject.GraphicsObject`
        or :py:class:`~jygsaw.shape.Shape` objects, or :py:class:`~jygsaw.group.Group`,
        and draws them on the Canvas. If a shape is drawn without specifying a color
        the default color is used. The default stroke option
        (:py:class:`True` or :py:class:`False`) and *stroke_color* is saved in each object.
        """
        for arg in params:
            if isinstance(arg, GraphicsObject) or isinstance(arg, Shape):
                if arg.color is None:
                    arg.color = self.frame.contentPane.default_color
                arg.stroke_color = self.frame.contentPane.stroke_color
                arg.stroke = self.frame.contentPane.stroke
                arg.filled = self.frame.contentPane.filled
                arg.stroke_width = self.frame.contentPane.stroke_width
                if isinstance(arg, Text):
                    arg.font = self.frame.contentPane.font
                    arg.size = self.frame.contentPane.text_size
                self.objs.append(arg)
            elif isinstance(arg, Group):
                for obj in arg.group:
                    if obj.color is None:
                        obj.color = self.frame.contentPane.default_color
                    obj.stroke_color = self.frame.contentPane.stroke_color
                    obj.stroke = self.frame.contentPane.stroke
                    obj.filled = self.frame.contentPane.filled
                    arg.stroke_width = self.frame.contentPane.stroke_width
                    if isinstance(arg, Text):
                        arg.font = self.frame.contentPane.font
                        arg.size = self.frame.contentPane.text_size
                    self.objs.append(obj)
            else:
                raise Exception("Passed in something that's not a Group or GraphicsObject.")

    def set_default_color(self, c):
        """Sets the default color of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self.frame.contentPane.default_color = c

    def set_stroke_color(self, c):
        """Sets the stroke color in the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self.frame.contentPane.stroke_color = c

    def set_stroke(self, b):
        """Turns stroke on or off in the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(b, bool), "Variable given is not a boolean."
        self.frame.contentPane.stroke = b

    def set_stroke_width(self, w):
        """Sets the width of the stroke in the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(w, int), "Variable given is not an integer."
        self.frame.contentPane.stroke_width = w

    def set_filled(self, f):
        """Turns fill on or off in the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(f, bool), "Variable given is not a boolean."
        self.frame.contentPane.filled = f

    def set_bg_color(self, c):
        """Sets the background color of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self.frame.contentPane.background_color = c
        self.background = c

    def set_font(self, f):
        """Sets the font of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        self.frame.contentPane.font = f

    def set_text_size(self, s):
        """Sets the text size of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert s >= 0 and isinstance(
            s, int), "Font size must be greater than or equal to 0"
        self.frame.contentPane.text_size = s

    def get_bg_color(self):
        """Returns the background color of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        return self.background

    def redraw(self, delay=0.0):
        """
        Redraws the :py:class:`~jygsaw.graphicswindow.Canvas`.
        Only returns when done. An optional float can also be used to sleep after redrawing.
        """
        # Use non-blocking redraw because there is no one-to-one relation
        # between calling cavas.repaint() and execution of paintComponent()
        #
        if SwingUtilities.isEventDispatchThread():
            self.frame.contentPane.repaint()
        else:
            self.frame.contentPane.blocking_redraw()
        sleep(delay)

    def clear(self):
        """
        Clears the screen so that only the background is visible.
        Also deletes all :py:class:`~jygsaw.graphicsobject.GraphicsObject` and :py:class:`~jygsaw.shape.Shape` and objects.
        """
        self.objs = []
        self.frame.contentPane.objs = self.objs

    def mouseEntered(self, e):
        """
        Runs when the mouse enters the window.
        Sets the mouse coordinates to the current mouse position.
        Calls a user-provided :py:meth:`mouse_entered` function, if any.
        """
        pos = self.frame.contentPane.getMousePosition()
        if pos:
            self.mouse_x = pos.x
            self.mouse_y = pos.y
        if self.main_running:
            if self.on_mouse_entered:
                self.on_mouse_entered()
        else:
            self.event_queue.put(e)
        if debug:
            print (self.mouse_x, self.mouse_y)

    def mouseClicked(self, e):
        """
        Runs when the mouse is clicked.
        Sets the mouse X and Y coordinates to the current mouse position.
        Calls a user-provided :py:meth:`mouse_clicked` function, if any.
        """
        pos = self.frame.contentPane.getMousePosition()
        if pos:
            self.mouse_x = pos.x
            self.mouse_y = pos.y
        if self.main_running:
            if self.on_mouse_clicked:
                self.on_mouse_clicked()
        else:
            self.event_queue.put(e)

    def mouseExited(self, e):
        """
        Runs when the mouse exits the window.
        Sets the mouse X and Y coordinates to the current mouse position.
        Calls a user-provided :py:meth:`mouse_exited` function, if any.
        """
        pos = self.frame.contentPane.getMousePosition()
        if pos:
            self.mouse_x = pos.x
            self.mouse_y = pos.y
        if self.main_running:
            if self.on_mouse_exited:
                self.on_mouse_exited()
        else:
            self.event_queue.put(e)

    def mousePressed(self, e):
        """
        Runs when the mouse button is pressed.
        Sets the mouse X and Y coordinates to the current mouse position.
        Calls a user-provided :py:meth:`mouse_pressed` function, if any.
        """
        pos = self.frame.contentPane.getMousePosition()
        if pos:
            self.mouse_x = pos.x
            self.mouse_y = pos.y
        self.mouse_buttons.add(e.getButton())
        if self.main_running:
            if self.on_mouse_pressed:
                self.on_mouse_pressed()
        else:
            self.event_queue.put(e)

    def mouseReleased(self, e):
        """
        Runs when the mouse button is released.
        Sets the mouse X and Y coordinates to the current mouse position.
        Calls a user-provided :py:meth:`mouse_released` function, if any.
        """
        pos = self.frame.contentPane.getMousePosition()
        if pos:
            self.mouse_x = pos.x
            self.mouse_y = pos.y
        self.mouse_buttons.remove(e.getButton())
        if self.main_running:
            if self.on_mouse_released:
                self.on_mouse_released()
        else:
            self.event_queue.put(e)

    def mouseMoved(self, e):
        """
        Runs when the mouse is moved.
        Sets the mouse X and Y coordinates to the current mouse position.
        Calls a user-provided :py:meth:`mouse_moved` function, if any.
        """
        pos = self.frame.contentPane.getMousePosition()
        if pos:
            self.mouse_x = pos.x
            self.mouse_y = pos.y
        if self.main_running:
            if self.on_mouse_moved:
                self.on_mouse_moved()
        else:
            self.event_queue.put(e)
        if debug:
            print '(%d, %d)' % (self.mouse_x, self.mouse_y)

    def mouseDragged(self, e):
        """
        Runs when the mouse is dragged.
        Sets the mouse X and Y coordinates to the current mouse position.
        Calls a user-provided :py:meth:`mouseDragged` function, if any.
        """
        pos = self.frame.contentPane.getMousePosition()
        if pos:
            self.mouse_x = pos.x
            self.mouse_y = pos.y
        if self.main_running:
            if self.on_mouse_dragged:
                self.on_mouse_dragged()
        else:
            self.event_queue.put(e)

    def keyTyped(self, e):
        """
        Sets the last key character and code when a key is typed. Calls a
        user-provided :py:meth:`keyTyped` function, if any.
        """
        if debug:
            print e.getKeyCode()

        if self.main_running:
            if self.on_key_typed:
                self.on_key_typed()
        else:
            self.event_queue.put(e)

    def keyPressed(self, e):
        """
        Sets the last key character and code when a key is pressed. Calls a
        user-provided :py:meth:`key_pressed` function, if any.
        """
        self.last_key_code = e.getKeyCode()
        self.last_key_char = e.getKeyChar()
        self.chars_pressed.add(e.getKeyText(e.getKeyCode()).upper())
        self.codes_pressed.add(e.getKeyCode())

        if debug:
            print "Key pressed:"
            print e.getKeyText(e.getKeyCode())
            print e.getKeyCode()

        if self.main_running:
            if self.on_key_pressed:
                self.on_key_pressed()
        else:
            self.event_queue.put(e)

    def keyReleased(self, e):
        """
        Sets the last key character and code when a key is released. Calls a
        user-provided :py:meth:`key_released` function, if any.
        """
        self.chars_pressed.remove(e.getKeyText(e.getKeyCode()).upper())
        self.codes_pressed.remove(e.getKeyCode())

        if debug:
            print "Key released:"
            print e.getKeyText(e.getKeyCode())
            print e.getKeyCode()

        if self.main_running:
            if self.on_key_released:
                self.on_key_released()
        else:
            self.event_queue.put(e)

    def _is_key_pressed(self):
        return bool(self.chars_pressed)

    isKeyPressed = property(_is_key_pressed, ':py:class:`True` if any keys are pressed, else :py:class:`False`.')

    def _get_width(self):
        """Get the width of the canvas."""
        return self.frame.contentPane.width

    width = property(_get_width, 'Width of Canvas in pixels.')

    def _get_height(self):
        """Get the height of the canvas."""
        return self.frame.contentPane.height

    height = property(_get_height, 'Height of Canvas in pixels.')


class Canvas(JPanel):
    """
    Canvas where objects get drawn. The Canvas is automatically created
    and attached to a :py:class:`~jygsaw.graphicswindow.GraphicsWindow` upon creation.
    """
    def __init__(self, window, objects, bg_color):
        self.objs = objects
        self.window = window
        self._default_color = GRAY
        self._background_color = bg_color
        self._stroke_color = BLACK
        self._stroke = False  # sets whether or not strokes are being drawn for shapes
        self._filled = True
        self._font = "Times New Roman"
        self._text_size = 12
        self._stroke_width = 1
        self.redraw_requested = True

    def paintComponent(self, g):
        """
        This function is responsible for drawing on the :py:class:`~jygsaw.graphicswindow.Canvas`. It is passed a
        Java Graphics object that is needed in order to draw all of the
        :py:class:`~jygsaw.graphicsobject.GraphicsObject` objects. Clears the window by
        drawing a clear rectangle over the entire window. The function then runs
        through the entire list of objects and draws them on the :py:class:`~jygsaw.graphicswindow.Canvas`.
        """

        if self.window.main_running and self.window.on_draw:
            self.window.on_draw()

        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                           RenderingHints.VALUE_ANTIALIAS_ON)
        g.background = self.background_color
        g.clearRect(0, 0, self.window.width, self.window.height)

        # Iterates through and draws all of the objects
        for obj in self.window.objs:
            obj._draw(g)

        self.redraw_requested = False

    def blocking_redraw(self):
        """
        Sends a redraw command to the :py:class:`~jygsaw.graphicswindow.Canvas`. Only returns when the redraw
        has been completed.
        """

        # print "blocking redraw called.  redraw requested true"
        self.redraw_requested = True

        while self.redraw_requested:
            self.repaint()
            # print "blocking"
            sleep(.001)

    def _get_default_color(self):
        """Get the default color of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        return self._default_color

    def _set_default_color(self, c):
        """Set the default color of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self._default_color = c

    default_color = property(_get_default_color, _set_default_color,
                             "Default fill color for all the objects.")

    def _get_background_color(self):
        """Get the background color of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        return self._background_color

    def _set_background_color(self, c):
        """Set the background color of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self._background_color = c

    background_color = property(_get_background_color, _set_background_color,
                                "Background color for the window.")

    def _get_stroke_color(self):
        """Returns the stroke_color."""
        return self._stroke_color

    def _set_stroke_color(self, c):
        """Sets the stroke color to *c*."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self._stroke_color = c

    stroke_color = property(
        _get_stroke_color, _set_stroke_color, "Stroke color of the Shape.")

    def _get_stroke(self):
        """Returns whether or not stroke is True or False"""
        return self._stroke

    def _set_stroke(self, b):
        """Sets stroke to the boolean given."""
        assert isinstance(b, bool), "The variable given is not a boolean."
        self._stroke = b

    stroke = property(_get_stroke, _set_stroke,
                      "Boolean describing whether a stroke is being drawn or not.")

    def _get_stroke_width(self):
        """Returns whether or not stroke is :py:class:`True` or :py:class:`False`."""
        return self._stroke_width

    def _set_stroke_width(self, b):
        """Sets stroke to the boolean given."""
        assert isinstance(b, int), "The variable given is not an integer."
        self._stroke_width = b

    stroke_width = property(_get_stroke_width, _set_stroke_width,
                            "Boolean describing whether a stroke is being drawn or not.")

    def _get_filled(self):
        """Returns whether or not stroke is :py:class:`True` or :py:class:`False`."""
        return self._filled

    def _set_filled(self, f):
        assert isinstance(f, bool), "The variable given is not a boolean."
        self._filled = f

    filled = property(_get_filled, _set_filled,
                      "Boolean describing whether a Shape is filled or not.")

    def _get_font(self):
        return self._font

    def _set_font(self, f):
        assert (f in Text._system_fonts), "Font is not available or incorrect."

        self._font = f

    font = property(_get_font, _set_font, "Returns the name of the current font.")

    def _get_text_size(self):
        return self._text_size

    def _set_text_size(self, f):
        assert f > 0 or isinstance(
            f, bool), "Text size must be an integer greater than 0."
        self._text_size = f

    text_size = property(_get_text_size, _set_text_size, "Returns the text size.")
