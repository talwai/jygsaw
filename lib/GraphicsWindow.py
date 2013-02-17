from java.awt.event import ActionListener, KeyListener, MouseListener, MouseEvent, KeyEvent, ActionEvent
from java.awt import Dimension
from java.awt.Color import *  # so we can just say gray instead of Color.gray
from javax.swing import JFrame, JPanel
from javax.swing.event import MouseInputListener
from java.lang import Math
from Image import *
from Group import *
from Shape import *
from Text import *

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
        self.w = w
        self.h = h
        self.backgroundColor = backgroundColor

        self.frame = JFrame(
            title, defaultCloseOperation=JFrame.EXIT_ON_CLOSE,
            size=(self.w, self.h))

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
                self.objs.append(arg)
            elif isinstance(arg, Group):
                for obj in arg.group:
                    if obj.color == None:
                        obj.color = self.frame.contentPane.defaultColor
                    obj.strokeColor = self.frame.contentPane.strokeColor
                    obj.stroke = self.frame.contentPane.stroke
                    self.objs.append(obj)
            else:
                print "Passed in something that's not a group or graphics object"

    def setDefaultColor(self, c):
        self.frame.contentPane.setDefaultColor(c)

    def setStrokeColor(self, c):
        self.frame.contentPane.setStrokeColor(c)

    def setStroke(self, b):
        self.frame.contentPane.setStroke(b)

    def setBackgroundColor(self, c):
        self.frame.contentPane.setBackgroundColor(c)
        self.background = c

    def getBackgroundColor(self):
        return self.background

    def redraw(self):
        self.frame.contentPane.repaint()

    """
    In order to clear the screen, all of the objects are removed
    from the objects list and then the screen is redrawn.
    """
    def clear(self):
        self.objs = []
        self.frame.contentPane.objs = self.objs
        self.redraw()

    """
    These methods implemented Swing's MouseInputListener interface.    """

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


class Canvas(JPanel):
    """ Canvas to draw the action on. Owns the action and key listeners. """

    def __init__(self, window, objects, backgroundColor):
        self.objs = objects
        self.window = window
        self.defaultColor = gray
        self.backgroundColor = backgroundColor
        self.strokeColor = black
        self.stroke = False  # sets whether or not strokes are being drawn for shapes

    """
    This fuction is responsible for drawing on the canvas. It is passed a
    java graphics object that is needed in order to draw all of the GraphicsObjects.
    Clears the window by drawing a clear rectangle over the entire window.
    The function then runs through the entire list of objs and draws all of them
    on the screen.
    """

    def paintComponent(self, g):
        g.background = self.backgroundColor
        g.clearRect(0, 0, self.window.w, self.window.h)
        g.setColor(white)  # Set color of rectangle

        for o in self.objs:
            g.setColor(o.getColor())
            o._draw(g)

    def setDefaultColor(self, c):
        self.defaultColor = c

    def setBackgroundColor(self, c):
        self.backgroundColor = c

    def setStrokeColor(self, c):
        self.strokeColor = c

    def setStroke(self, b):
        self.stroke = b
