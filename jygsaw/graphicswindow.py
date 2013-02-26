from __future__ import with_statement
from java.awt.event import ActionListener, KeyListener, MouseListener, MouseEvent, KeyEvent, ActionEvent
from java.awt import Dimension, RenderingHints
from java.awt.Color import *  # so we can just say gray instead of Color.gray
from javax.swing import JFrame, JPanel
from javax.swing.event import MouseInputListener
from image import *
from group import *
from shape import *
from text import *
from time import sleep

# the -O switch can't be used with jython, which is used to turn off __debug__
# so we use debug instead
debug = 0


class GraphicsWindow(ActionListener, KeyListener, MouseInputListener):
    """
    Creates a GraphicsWindow with a Canvas object that can be drawn on.
    Also takes callback functions for Mouse and Key input.

    """
    def __init__(self, title, w, h, backgroundColor=white):

        assert w > 0, "GraphicsWindow width must be greater than zero"
        assert h > 0, "GraphicsWindow height must be greater than zero"

        self.objs = []  # List of GraphicsObjects
        self.backgroundColor = backgroundColor

        self.frame = JFrame(
            title, defaultCloseOperation=JFrame.EXIT_ON_CLOSE,
            size=(w, h))

        self.frame.contentPane = Canvas(self, self.objs, self.backgroundColor)
        self.frame.contentPane.setPreferredSize(Dimension(w, h))

        # print self.frame.contentPane.isDoubleBuffered()

        self.frame.contentPane.setDoubleBuffered(False)

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

        self.user_draw_fn = None

    def setVisible(self, isVisible):
        self.frame.pack()
        self.frame.visible = isVisible

    """
    Takes a variable number of GraphicsObjects, or Groups of GraphicsObjects,
    and draws them on the window. If a shape is drawn without specifiying
    a color the default color is used. The default stroke option (True or False)
    and stokeColor is saved in each object.
    """
    def draw(self, *params):
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
        """Sets the default color of the Canvas"""
        self.frame.contentPane.defaultColor = c

    def setStrokeColor(self, c):
        """Sets the stroke color in the Canvas"""
        self.frame.contentPane.strokeColor = c

    def setStroke(self, b):
        self.frame.contentPane.stroke = b

    def setFilled(self, f):
        self.frame.contentPane.filled = f

    def setBackgroundColor(self, c):
        self.frame.contentPane.backgroundColor = c
        self.background = c

    def setFont(self, f):
        self.frame.contentPane.font = f

    def setTextSize(self, s):
        assert s >= 0, "Font size must be greater than or equal to 0"
        self.frame.contentPane.textSize = s

    def getBackgroundColor(self):
        return self.background

    def redraw(self, delay=0.0):
        self.frame.contentPane.blocking_redraw()
        sleep(delay)

    """
    In order to clear the screen, all of the objects are removed
    from the objects list and then the screen is redrawn.
    """
    def clear(self):
        self.objs = []
        self.frame.contentPane.objs = self.objs

    """ These methods implemented Swing's MouseInputListener interface. """

    def mouseEntered(self, e):
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if debug:
            print '(%d, %d)' % (self.mouseX, self.mouseY)

    def mouseClicked(self, e):
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.onMouseClicked:
            self.onMouseClicked()

    def mouseExited(self, e):
        self.mouseEventType = e.getID()

    def mousePressed(self, e):
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.onMousePressed:
            self.onMousePressed()

    def mouseReleased(self, e):
        self.mouseEventType = e.getID()
        if self.onMouseReleased:
            self.onMouseReleased()

    def mouseMoved(self, e):
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.onMouseMoved:
            self.onMouseMoved()
        if debug:
            print '(%d, %d)' % (self.mouseX, self.mouseY)

    def mouseDragged(self, e):
        self.mouseEventType = e.getID()
        self.mouseX = e.getX()
        self.mouseY = e.getY() - 25
        if self.onMouseDragged:
            self.onMouseDragged()

    """
    These methods implement Swing's KeyListener inteface.
    """
    def keyTyped(self, e):
        self.keyEventType = e.getID()
        if debug:
            print e.getKeyChar()
        if self.onKeyTyped:
            self.lastKeyChar = e.getKeyChar()
            self.lastKeyCode = e.getKeyCode()
            self.onKeyTyped()

    def keyPressed(self, e):
        self.keyEventType = e.getID()
        if debug:
            print e.getKeyChar()
        if self.onKeyPressed:
            self.lastKeyChar = e.getKeyChar()
            self.lastKeyCode = e.getKeyCode()
            self.onKeyPressed()

    def keyReleased(self, e):
        self.keyEventType = e.getID()
        if self.onKeyReleased:
            self.lastKeyChar = e.getKeyChar()
            self.lastKeyCode = e.getKeyCode()
            self.onKeyReleased()

    def _get_width(self):
        """Get the width of the canvas"""
        return self.frame.contentPane.width

    width = property(_get_width, 'Width of canvas')

    def _get_height(self):
        """Get the height of the canvas"""
        return self.frame.contentPane.height

    height = property(_get_height, 'Height of canvas')


class Canvas(JPanel):
    """ Canvas to draw the action on. Owns the action and key listeners. """

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
        This fuction is responsible for drawing on the canvas. It is passed a
        java graphics object that is needed in order to draw all of the GraphicsObjects.
        Clears the window by drawing a clear rectangle over the entire window.
        The function then runs through the entire list of objs and draws all of them
        on the screen.
        """
        # Run the user-defined draw function if it exists
        if self.window.user_draw_fn:
            self.window.user_draw_fn()

        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                           RenderingHints.VALUE_ANTIALIAS_ON)
        g.background = self.backgroundColor
        g.clearRect(0, 0, self.window.width, self.window.height)
        g.setColor(white)  # Set color of rectangle

        # Iterates through and draws all of the objects
        for obj in self.window.objs:
            obj._draw(g)

        self.redraw_requested = False

    def blocking_redraw(self):

        self.redraw_requested = True
        self.repaint()
        while self.redraw_requested:
            sleep(.001)

    def _get_defaultColor(self):
        """Get the default color of the Canvas"""
        return self._defaultColor

    def _set_defaultColor(self, c):
        """Set the default color of the Canvas"""
        self._defaultColor = c

    defaultColor = property(_get_defaultColor, _set_defaultColor,
                            "Default fill color for all the objects")

    def _get_backgroundColor(self):
        """Get the background color of the Canvas"""
        return self._backgroundColor

    def _set_backgroundColor(self, c):
        """Set the background color of the Canvas"""
        self._backgroundColor = c

    backgroundColor = property(_get_backgroundColor, _set_backgroundColor,
                               "Background Color for the window.")

    def _get_strokeColor(self):
        """Returns the strokeColor"""
        return self._strokeColor

    def _set_strokeColor(self, c):
        """Sets the strokeColor with the color passed as an argument"""
        self._strokeColor = c

    strokeColor = property(
        _get_strokeColor, _set_strokeColor, "Stroke color of the Shape.")

    def _get_stroke(self):
        """Returns whether or not stroke is True or False"""
        return self._stroke

    def _set_stroke(self, b):
        """Sets stroke to the boolean given"""
        self._stroke = b

    stroke = property(_get_stroke, _set_stroke,
                      "Boolean describing whether a stroke is being drawn or not.")

    def _get_filled(self):
        """Returns whether or not stoke is True of False"""
        return self._filled

    def _set_filled(self, f):
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
        self._textSize = f

    textSize = property(_get_textSize, _set_textSize)