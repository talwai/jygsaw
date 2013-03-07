"""
Exports GraphicsWindow and Canvas. A Canvas is created and attached to a
GraphicsWindow on window creation. A window holds the drawing canvas.
"""

from __future__ import with_statement
from java.awt.event import ActionListener, KeyListener, MouseListener, MouseEvent, KeyEvent, ActionEvent
from java.awt import Color, Dimension, RenderingHints
from java.awt.Color import black, blue, cyan, darkGray, gray, green, lightGray, magenta, orange, pink, red, white, yellow
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

# the -O switch can't be used with jython, which is used to turn off __debug__
# so we use debug instead
debug = 0


class GraphicsWindow(ActionListener, KeyListener, MouseInputListener):
    """
    Creates a GraphicsWindow with a Canvas object that can be drawn on.
    Takes a title, window width, and window height. An optional background
    color can be specified.
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
        self.codesPressed = Set()

        # Event queue
        self.eventQueue = Queue()

        self.mainRunning = False

        # not needed, user_draw is called directly from onDraw
        self.onDraw = None

    def setVisible(self, isVisible):
        """Sets the window to visible."""
        assert isinstance(isVisible, bool), "Variable is not a boolean."
        self.frame.pack()
        self.frame.visible = isVisible

    def draw(self, *params):
        """
        Takes a variable number of GraphicsObjects, or Groups of
        GraphicsObjects, and draws them on the window. If a shape is drawn
        without specifiying a color the default color is used. The default
        stroke option (True or False) and stokeColor is saved in each object.
        """
        for arg in params:
            if isinstance(arg, GraphicsObject):
                if arg.color == None:
                    arg.color = self.frame.contentPane.defaultColor
                arg.strokeColor = self.frame.contentPane.strokeColor
                arg.stroke = self.frame.contentPane.stroke
                arg.filled = self.frame.contentPane.filled
                if isinstance(arg, Text):
                    arg.font = self.frame.contentPane.font
                    arg.size = self.frame.contentPane.textSize
                self.objs.append(arg)
            elif isinstance(arg, Group):
                for obj in arg.group:
                    if obj.color == None:
                        obj.color = self.frame.contentPane.defaultColor
                    obj.strokeColor = self.frame.contentPane.strokeColor
                    obj.stroke = self.frame.contentPane.stroke
                    obj.filled = self.frame.contentPane.filled
                    if isinstance(arg, Text):
                        arg.font = self.frame.contentPane.font
                        arg.size = self.frame.contentPane.textSize
                    self.objs.append(obj)
            else:
                print "Passed in something that's not a group or graphics object"

    def setDefaultColor(self, c):
        """Sets the default color of the Canvas."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self.frame.contentPane.defaultColor = c

    def setStrokeColor(self, c):
        """Sets the stroke color in the Canvas."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self.frame.contentPane.strokeColor = c

    def setStroke(self, b):
        """Turns stroke on or off in the Canvas."""
        assert isinstance(b, bool), "Variable given is not a boolean."
        self.frame.contentPane.stroke = b

    def setFilled(self, f):
        """Turns fill on or off in the Canvas."""
        assert isinstance(f, bool), "Variable given is not a boolean."
        self.frame.contentPane.filled = f

    def setBackgroundColor(self, c):
        """Sets the background color of the Canvas."""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self.frame.contentPane.backgroundColor = c
        self.background = c

    def setFont(self, f):
        """Sets the font of the Canvas."""

        self.frame.contentPane.font = f

    def setTextSize(self, s):
        """Sets the text size of the Canvas."""
        assert s >= 0 and isinstance(s, int), "Font size must be greater than or equal to 0"
        self.frame.contentPane.textSize = s

    def getBackgroundColor(self):
        """Returns the background color of the Canvas."""
        return self.background

    def redraw(self, delay=0.0):
        """
        Redraws the Canvas; only returns when done. An optional float
        can also be used to sleep after redrawing.
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
        """Clears the screen by removing all shapes from the window."""
        self.objs = []
        self.frame.contentPane.objs = self.objs

    def mouseEntered(self, e):
        """
        Sets the mouse X and Y coordinates when the mouse enters the window.
        Calls a user mouse entered function, if any.
        """
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.onMouseEntered:
            self.onMouseEntered()
        if debug:
            print '(%d, %d)' % (self.mouseX, self.mouseY)

    def mouseClicked(self, e):
        """
        Sets the mouse X and Y coordinates when the mouse is clicked. Calls
        a user mouse clicked function, if any.
        """
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.onMouseClicked:
            self.onMouseClicked()

    def mouseExited(self, e):
        """
        Sets the mouse X and Y coordinates when the mouse exits the screen.
        Calls a user mouse exited function, if any.
        """
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.onMouseExited:
            self.onMouseExited()

    def mousePressed(self, e):
        """
        Sets the mouse X and Y coordiantes when the mouse is pressed.
        Calls a user mouse pressed function, if any.
        """
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.onMousePressed:
            self.onMousePressed()

    def mouseReleased(self, e):
        """
        Sets the mouse X and Y coordinates when the mouse is released.
        Calls a user mouse released function, if any.
        """
        self.mouseEventType = e.getID()
        if self.onMouseReleased:
            self.onMouseReleased()

    def mouseMoved(self, e):
        """
        Sets the mouse X and Y coordinates when the mouse is moved.
        Calls a user mouse moved function, if any.
        """
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.onMouseMoved:
            self.onMouseMoved()
        if debug:
            print '(%d, %d)' % (self.mouseX, self.mouseY)

    def mouseDragged(self, e):
        """
        Sets the mouse X and Y coordinates when the mouse is dragged.
        Calls a user mouse dragged function, if any.
        """
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.onMouseDragged:
            self.onMouseDragged()

    def keyTyped(self, e):
        """
        Sets the last key character and code when a key is typed. Calls a
        user key typed function, if any.
        """
        self.keyEventType = e.getID()
        if debug:
            print e.getKeyChar()
        if self.onKeyTyped:
            self.lastKeyChar = e.getKeyChar()
            self.lastKeyCode = e.getKeyCode()
            self.onKeyTyped()

    def keyPressed(self, e):
        """
        Sets the last key character and code when a key is pressed. Calls a
        user key pressed function, if any.
        """
        self.keyEventType = e.getID()
        self.lastKeyChar = e.getKeyChar()
        self.lastKeyCode = e.getKeyCode()
        self.charsPressed.add(self.lastKeyChar)
        self.codesPressed.add(self.lastKeyCode)

        if debug:
            print e.getKeyChar()
        if self.onKeyPressed:
            self.onKeyPressed()

    def keyReleased(self, e):
        """
        Sets the last key character and code when a key is released. Calls a
        user key released function, if any.
        """
        self.keyEventType = e.getID()
        self.lastKeyChar = e.getKeyChar()
        self.lastKeyCode = e.getKeyCode()
        self.charsPressed.remove(self.lastKeyChar)
        self.codesPressed.remove(self.lastKeyCode)

        if self.onKeyReleased:
            self.onKeyReleased()

    def _is_key_pressed(self):
        return bool(self.charsPressed)

    isKeyPressed = property(_is_key_pressed, 'Width of canvas')

    def _get_width(self):
        """Get the width of the canvas"""
        return self.frame.contentPane.width

    width = property(_get_width, 'Width of canvas')

    def _get_height(self):
        """Get the height of the canvas"""
        return self.frame.contentPane.height

    height = property(_get_height, 'Height of canvas')


class Canvas(JPanel):
    """
    Canvas where objects get drawn. The Canvas is automatically created
    and attached to a window upon window creation.
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

        self.redraw_requested = True

    def paintComponent(self, g):
        """
        This function is responsible for drawing on the canvas. It is passed a
        Java Graphics object that is needed in order to draw all of the
        GraphicsObjects. Clears the window by drawing a clear rectangle over
        the entire window. The function then runs through the entire list of
        objects and draws them on the Canvas.
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
        Sends a redraw command to the Canvas. Only returns when the redraw
        has been completed.
        """

        #print "blocking redraw called.  redraw requested true"
        self.redraw_requested = True

        while self.redraw_requested:
            self.repaint()
            #print "blocking"
            sleep(.001)

    def _get_defaultColor(self):
        """Get the default color of the Canvas"""
        return self._defaultColor

    def _set_defaultColor(self, c):
        """Set the default color of the Canvas"""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self._defaultColor = c

    defaultColor = property(_get_defaultColor, _set_defaultColor,
                            "Default fill color for all the objects")

    def _get_backgroundColor(self):
        """Get the background color of the Canvas"""
        return self._backgroundColor

    def _set_backgroundColor(self, c):
        """Set the background color of the Canvas"""
        assert isinstance(c, Color), "The object passed is not a Color object."
        self._backgroundColor = c

    backgroundColor = property(_get_backgroundColor, _set_backgroundColor,
                               "Background Color for the window.")

    def _get_strokeColor(self):
        """Returns the strokeColor"""
        return self._strokeColor

    def _set_strokeColor(self, c):
        """Sets the strokeColor with the color passed as an argument."""
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

    def _get_filled(self):
        """Returns whether or not stroke is True of False"""
        return self._filled

    def _set_filled(self, f):
        assert isinstance(f, bool), "The variable given is not a boolean"
        self._filled = f

    filled = property(_get_filled, _set_filled,
                      "Boolean describing whether a Shape is filled or not.")

    def _get_font(self):
        return self._font

    def _set_font(self, f):
        self._font = f

    font = property(_get_font, _set_font)

    def _get_textSize(self):
        return self._textSize

    def _set_textSize(self, f):
        assert f > 0 or isinstance(f, bool), "Text size must be an integer greater than 0."
        self._textSize = f

    textSize = property(_get_textSize, _set_textSize)
