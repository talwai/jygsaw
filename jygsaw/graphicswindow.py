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
from image import *
from group import *
from sets import Set
from shape import *
from text import *
from time import sleep
from Queue import Queue
# These unused imports are for the user
from java.awt.Color import black, blue, cyan, darkGray, gray, green, lightGray, magenta, orange, pink, red, white, yellow


# the -O switch can't be used with jython, which is used to turn off __debug__
# so we use debug instead
debug = False


class GraphicsWindow(ActionListener, KeyListener, MouseInputListener):
    """
    Creates a :py:class:`~jygsaw.graphicswindow.GraphicsWindow` with a :py:class:`~jygsaw.graphicswindow.Canvas`
    object that can be drawn on. Takes a title, window width, and window height.
    An optional background color can be specified.
    """
    def __init__(self, title, w, h, backgroundColor=white):
        assert w > 0, "GraphicsWindow width must be greater than zero"
        assert h > 0, "GraphicsWindow height must be greater than zero"

        self.objs = []  # List of GraphicsObjects
        self.backgroundColor = backgroundColor

        self.frame = JFrame(
            title, defaultCloseOperation=JFrame.EXIT_ON_CLOSE,
            size=(w, h))

        self.frame.setLocationRelativeTo(None)
        self.frame.contentPane = Canvas(self, self.objs, self.backgroundColor)
        self.frame.contentPane.setPreferredSize(Dimension(w, h))

        self.frame.addMouseListener(self)
        self.frame.addMouseMotionListener(self)
        self.frame.addKeyListener(self)

        # MouseEvent attributes
        self.mouseEventType = 0
        self.mouseX = 0
        self.mouseY = 0

        # Mouse callbacks
        self.onMouseClicked = None
        self.onMouseDragged = None
        self.onMouseMoved = None
        self.onMousePressed = None
        self.onMouseReleased = None
        self.onMouseDragged = None
        self.onMouseExited = None
        self.onMouseEntered = None

        # KeyEvent booleans keyPressed, keyTyped
        self.keyEventType = 0
        self.keyP = False
        self.keyT = False

        # Key callbacks
        self.onKeyPressed = None
        self.onKeyReleased = None
        self.onKeyTyped = None

        # Key values
        self.lastKeyChar = None
        self.lastKeyCode = None

        self.charsPressed = Set()

        # Event queue
        self.eventQueue = Queue()

        self.mainRunning = False

        # not needed, user_draw is /called directly from onDraw
        self.onDraw = None

    def setVisible(self, isVisible):
        """Sets the window to visible."""
        assert isinstance(isVisible, bool), "Variable is not a boolean."
        self.frame.pack()
        self.frame.visible = isVisible

    def draw(self, *params):
        """
        Takes any number of :py:class:`~jygsaw.graphicsobject.GraphicsObject`
        or :py:class:`~jygsaw.shape.Shape` objects, or :py:class:`~jygsaw.group.Group`,
        and draws them on the Canvas. If a shape is drawn without specifying a color
        the default color is used. The default stroke option
        (:py:class:`True` or :py:class:`False`) and *strokeColor* is saved in each object.
        """
        for arg in params:
            if isinstance(arg, GraphicsObject) or isinstance(arg, Shape):
                if arg.color is None:
                    arg.color = self.frame.contentPane.defaultColor
                arg.strokeColor = self.frame.contentPane.strokeColor
                arg.stroke = self.frame.contentPane.stroke
                arg.filled = self.frame.contentPane.filled
                arg.strokeWidth = self.frame.contentPane.strokeWidth
                if isinstance(arg, Text):
                    arg.font = self.frame.contentPane.font
                    arg.size = self.frame.contentPane.textSize
                self.objs.append(arg)
            elif isinstance(arg, Group):
                for obj in arg.group:
                    if obj.color is None:
                        obj.color = self.frame.contentPane.defaultColor
                    obj.strokeColor = self.frame.contentPane.strokeColor
                    obj.stroke = self.frame.contentPane.stroke
                    obj.filled = self.frame.contentPane.filled
                    arg.strokeWidth = self.frame.contentPane.strokeWidth
                    if isinstance(arg, Text):
                        arg.font = self.frame.contentPane.font
                        arg.size = self.frame.contentPane.textSize
                    self.objs.append(obj)
            else:
                raise Exception("Passed in something that's not a Group or GraphicsObject.")

    def setDefaultColor(self, c):
        """Sets the default color of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self.frame.contentPane.defaultColor = c

    def setStrokeColor(self, c):
        """Sets the stroke color in the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self.frame.contentPane.strokeColor = c

    def setStroke(self, b):
        """Turns stroke on or off in the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(b, bool), "Variable given is not a boolean."
        self.frame.contentPane.stroke = b

    def setStrokeWidth(self, w):
        """Sets the width of the stroke in the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(w, int), "Variable given is not an integer."
        self.frame.contentPane.strokeWidth = w

    def setFilled(self, f):
        """Turns fill on or off in the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(f, bool), "Variable given is not a boolean."
        self.frame.contentPane.filled = f

    def setBackgroundColor(self, c):
        """Sets the background color of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self.frame.contentPane.backgroundColor = c
        self.background = c

    def setFont(self, f):
        """Sets the font of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        self.frame.contentPane.font = f

    def setTextSize(self, s):
        """Sets the text size of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert s >= 0 and isinstance(
            s, int), "Font size must be greater than or equal to 0"
        self.frame.contentPane.textSize = s

    def getBackgroundColor(self):
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
        Calls a user-provided :py:meth:`mouseEntered` function, if any.
        """
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.mainRunning:
            if self.onMouseEntered:
                self.onMouseEntered()
        else:
            self.eventQueue.put(e)
        if debug:
            print (self.mouseX, self.mouseY)

    def mouseClicked(self, e):
        """
        Runs when the mouse is clicked.
        Sets the mouse X and Y coordinates to the current mouse position.
        Calls a user-provided :py:meth:`mouseClicked` function, if any.
        """
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.mainRunning:
            if self.onMouseClicked:
                self.onMouseClicked()
        else:
            self.eventQueue.put(e)

    def mouseExited(self, e):
        """
        Runs when the mouse exits the window.
        Sets the mouse X and Y coordinates to the current mouse position.
        Calls a user-provided :py:meth:`mouseExited` function, if any.
        """
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.mainRunning:
            if self.onMouseExited:
                self.onMouseExited()
        else:
            self.eventQueue.put(e)

    def mousePressed(self, e):
        """
        Runs when the mouse button is pressed.
        Sets the mouse X and Y coordinates to the current mouse position.
        Calls a user-provided :py:meth:`mousePressed` function, if any.
        """
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.mainRunning:
            if self.onMousePressed:
                self.onMousePressed()
        else:
            self.eventQueue.put(e)

    def mouseReleased(self, e):
        """
        Runs when the mouse button is released.
        Sets the mouse X and Y coordinates to the current mouse position.
        Calls a user-provided :py:meth:`mouseReleased` function, if any.
        """
        self.mouseEventType = e.getID()
        if self.mainRunning:
            if self.onMouseReleased:
                self.onMouseReleased()
        else:
            self.eventQueue.put(e)

    def mouseMoved(self, e):
        """
        Runs when the mouse is moved.
        Sets the mouse X and Y coordinates to the current mouse position.
        Calls a user-provided :py:meth:`mouseMoved` function, if any.
        """
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.mainRunning:
            if self.onMouseMoved:
                self.onMouseMoved()
        else:
            self.eventQueue.put(e)
        if debug:
            print '(%d, %d)' % (self.mouseX, self.mouseY)

    def mouseDragged(self, e):
        """
        Runs when the mouse is dragged.
        Sets the mouse X and Y coordinates to the current mouse position.
        Calls a user-provided :py:meth:`mouseDragged` function, if any.
        """
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.mainRunning:
            if self.onMouseDragged:
                self.onMouseDragged()
        else:
            self.eventQueue.put(e)

    def keyTyped(self, e):
        """
        Sets the last key character and code when a key is typed. Calls a
        user-provided :py:meth:`keyTyped` function, if any.
        """
        self.keyEventType = e.getID()

        if debug:
            print e.getKeyCode()

        if self.mainRunning:
            if self.onKeyTyped:
                self.onKeyTyped()
        else:
            self.eventQueue.put(e)

    def keyPressed(self, e):
        """
        Sets the last key character and code when a key is pressed. Calls a
        user-provided :py:meth:`keyPressed` function, if any.
        """
        self.keyEventType = e.getID()
        self.lastKeyCode = e.getKeyCode()
        self.lastKeyChar = e.getKeyChar()
        self.charsPressed.add(e.getKeyText(e.getKeyCode()).upper())

        if debug:
            print "Key pressed:"
            print e.getKeyText(e.getKeyCode())
            print e.getKeyCode()

        if self.mainRunning:
            if self.onKeyPressed:
                self.onKeyPressed()
        else:
            self.eventQueue.put(e)

    def keyReleased(self, e):
        """
        Sets the last key character and code when a key is released. Calls a
        user-provided :py:meth:`keyReleased` function, if any.
        """
        self.keyEventType = e.getID()
        self.charsPressed.remove(e.getKeyText(e.getKeyCode()).upper())

        if debug:
            print "Key released:"
            print e.getKeyText(e.getKeyCode())
            print e.getKeyCode()

        if self.mainRunning:
            if self.onKeyReleased:
                self.onKeyReleased()
        else:
            self.eventQueue.put(e)

    def _is_key_pressed(self):
        return bool(self.charsPressed)

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
    def __init__(self, window, objects, backgroundColor):
        self.objs = objects
        self.window = window
        self._defaultColor = gray
        self._backgroundColor = backgroundColor
        self._strokeColor = black
        self._stroke = False  # sets whether or not strokes are being drawn for shapes
        self._filled = True
        self._font = "Times New Roman"
        self._textSize = 12
        self._strokeWidth = 1

        self.redraw_requested = True

        # Installed fonts

    def paintComponent(self, g):
        """
        This function is responsible for drawing on the :py:class:`~jygsaw.graphicswindow.Canvas`. It is passed a
        Java Graphics object that is needed in order to draw all of the
        :py:class:`~jygsaw.graphicsobject.GraphicsObject` objects. Clears the window by
        drawing a clear rectangle over the entire window. The function then runs
        through the entire list of objects and draws them on the :py:class:`~jygsaw.graphicswindow.Canvas`.
        """

        if self.window.mainRunning and self.window.onDraw:
            self.window.onDraw()

        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                           RenderingHints.VALUE_ANTIALIAS_ON)
        g.background = self.backgroundColor
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

    def _get_defaultColor(self):
        """Get the default color of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        return self._defaultColor

    def _set_defaultColor(self, c):
        """Set the default color of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self._defaultColor = c

    defaultColor = property(_get_defaultColor, _set_defaultColor,
                            "Default fill color for all the objects.")

    def _get_backgroundColor(self):
        """Get the background color of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        return self._backgroundColor

    def _set_backgroundColor(self, c):
        """Set the background color of the :py:class:`~jygsaw.graphicswindow.Canvas`."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self._backgroundColor = c

    backgroundColor = property(_get_backgroundColor, _set_backgroundColor,
                               "Background color for the window.")

    def _get_strokeColor(self):
        """Returns the strokeColor."""
        return self._strokeColor

    def _set_strokeColor(self, c):
        """Sets the stroke color to *c*."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self._strokeColor = c

    strokeColor = property(
        _get_strokeColor, _set_strokeColor, "Stroke color of the Shape.")

    def _get_stroke(self):
        """Returns whether or not stroke is True or False"""
        return self._stroke

    def _set_stroke(self, b):
        """Sets stroke to the boolean given."""
        assert isinstance(b, bool), "The variable given is not a boolean."
        self._stroke = b

    stroke = property(_get_stroke, _set_stroke,
                      "Boolean describing whether a stroke is being drawn or not.")

    def _get_strokeWidth(self):
        """Returns whether or not stroke is :py:class:`True` or :py:class:`False`."""
        return self._strokeWidth

    def _set_strokeWidth(self, b):
        """Sets stroke to the boolean given."""
        assert isinstance(b, int), "The variable given is not an integer."
        self._strokeWidth = b

    strokeWidth = property(_get_strokeWidth, _set_strokeWidth,
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
        assert (f in Text._systemFonts), "Font is not available or incorrect."

        self._font = f

    font = property(_get_font, _set_font, "Returns the name of the current font.")

    def _get_textSize(self):
        return self._textSize

    def _set_textSize(self, f):
        assert f > 0 or isinstance(
            f, bool), "Text size must be an integer greater than 0."
        self._textSize = f

    textSize = property(_get_textSize, _set_textSize, "Returns the text size.")
