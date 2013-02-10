from java.awt.event import ActionListener, KeyListener, MouseListener
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

# Buttons, etc
# class Components:

class GraphicsWindow(ActionListener, KeyListener, MouseInputListener):
    # setters and getters for width and height
    def __init__(self, title, w, h, backgroundColor=white):
        assert w > 0, "GraphicsWindow width must be greater than zero"
        assert h > 0, "GraphicsWindow height must be greater than zero"
        self.objs = []  # List of Jy_Objects
        self.w = w
        self.h = h
        self.backgroundColor = backgroundColor

        self.frame = JFrame(title, defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
                            size = (self.w, self.h))

        self.frame.contentPane = Canvas(self, self.objs, self.backgroundColor)
        self.frame.addMouseListener(self)
        self.frame.addMouseMotionListener(self)
        self.frame.addKeyListener(self)

        # MouseEvent booleans
        self.mouseX = 0
        self.mouseY = 0
        self.mouseP = False
        self.mouseC = False
        self.mouseD = False

        # Mouse callbacks
        self.onMouseClicked = None
        self.onMouseDragged = None
        self.onMouseMoved = None
        self.onMousePressed = None
        self.onMouseReleased = None

        # KeyEvent booleans keyPressed, keyTyped
        self.keyP = False
        self.keyT = False

        # Key callbacks
        self.onKeyPressed = None
        self.onKeyReleased = None
        self.onKeyTyped = None

    def setVisible(self, isVisible):
        self.frame.visible = isVisible

    # this argument takes a variable length number of GraphicsObjects and Group objects
    # using the splat operator, which packages the args into a tuple.
    # We iterate through each element in the tuple,
    # and add it to our self.objs.
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
                print "you passed in something that's not a group or graphics object"

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

    def clear(self):
        self.objs = []
        self.frame.contentPane.objs = self.objs
        self.redraw()


    # We put these mouse location methods in the window class in case we implement multiple panels
    # MouseListener methods
    def mouseEntered(self, e):
        self.mouseX = e.getXOnScreen()
        self.mouseY = e.getYOnScreen()
        if debug:
            print self.mouseX
            print self.mouseY

    def mouseX(self):
        return self.mouseX

    def mouseY(self):
        return self.mouseY

    def mouseClicked(self, e):
        self.mouseC = True
        if self.onMouseClicked:
            self.onMouseClicked()

    def mouseExited(self, e):
        pass

    def mousePressed(self, e):
        self.mouseP = True
        if self.onMousePressed:
            self.onMousePressed()

    def mouseReleased(self, e):
        self.mouseP = False
        self.mouseC = False
        self.mouseD = False
        if self.onMouseReleased:
            self.onMouseReleased()

    def mouseMoved(self, e):
        self.mouseX = e.getXOnScreen()
        self.mouseY = e.getYOnScreen()
        if self.onMouseMoved:
            self.onMouseMoved()
        if debug:
            print self.mouseX
            print self.mouseY

    def mouseDragged(self, e):
        self.mouseD = True

    #KeyListener methods
    def keyTyped (self,e):
        if self.onMouseDragged:
            self.onMouseDragged()

    # KeyListener methods
    def keyTyped(self, e):
        self.keyT = True
        if debug:
            print e.getKeyChar()
        if self.onKeyTyped:
            self.onKeyTyped()

    def keyPressed(self, e):
        self.keyP = True
        if self.onKeyPressed:
            self.onKeyPressed()
        if debug:
            print e.getKeyChar()

    def keyReleased(self, e):
        self.keyT = False
        self.keyP = False
        if self.onKeyReleased:
            self.onKeyReleased()

class Canvas(JPanel):
    """ Canvas to draw the action on. Owns the action and key listeners. """

    def __init__(self, window, objects, backgroundColor):
        self.objs = objects
        self.window = window
        self.defaultColor = gray
        self.backgroundColor = backgroundColor
        self.strokeColor = black
        self.stroke = False
    
    def paintComponent(self, g):
        g.background = self.backgroundColor
        g.clearRect(0, 0, self.window.w, self.window.h)
        g.setColor(white)  # Set color of rectangle

        print 'Canvas # objs', len(self.objs)

        for i in range(len(self.objs)):
            g.setColor(self.objs[i].getColor())
            self.objs[i]._draw(g)

    def setDefaultColor(self, c):
        self.defaultColor = c

    def setBackgroundColor(self, c):
        self.backgroundColor = c

    def setStrokeColor(self, c):
        self.strokeColor = c

    def setStroke(self, b):
        self.stroke = b

