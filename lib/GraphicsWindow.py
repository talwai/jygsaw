from java.awt.event import ActionListener, KeyListener, MouseListener
from java.awt.Color import * # so we can just say gray instead of Color.gray
from javax.swing import JFrame, JPanel
from java.lang import Math
from Image import *
from Group import *
from Shape import *
from Text import *


# Buttons, etc
# class Components:


class GraphicsWindow(ActionListener, KeyListener, MouseListener):
    #setters and getters for width and height
    def __init__(self, title, w, h, backgroundColor = white):
        assert w > 0, "GraphicsWindow width must be greater than zero"
        assert h > 0, "GraphicsWindow height must be greater than zero"
        self.objs = [] # List of Jy_Objects
        self.w = w
        self.h = h
        self.frame = JFrame(title,defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
                            size = (self.w, self.h))
        self.frame.contentPane = Canvas(self, self.objs, backgroundColor)
    
    def setVisible(self, isVisible):
        self.frame.visible = isVisible
    
    # this argument takes a variable length number of GraphicsObjects and Group objects
    # using the splat operator, which packages the args into a tuple.
    # We iterate through each element in the tuple,
    # and add it to our self.objs.
    def draw(self, *params):        
        for arg in params:
            if isinstance(arg, GraphicsObject):
                self.objs.append(arg)
            elif isinstance(arg, Group):
                for obj in arg.group:
                    self.objs.append(obj)
            else:
                print "you passed in something that's not a group or graphics object"

    def setDefaultColor(self, c):
        self.frame.contentPane.setDefaultColor(c)

class Canvas(JPanel, ActionListener, KeyListener):
    """ Canvas to draw the action on. Owns the action and key listeners. """
    
    def __init__(self, window, objects, backgroundColor):
        self.objs = objects
        self.window = window
        self.defaultColor = gray
        self.backgroundColor = backgroundColor
    
    def paintComponent(self, g):
        g.background = self.backgroundColor
        g.clearRect(0, 0, self.window.w, self.window.h)
        g.setColor(white) # Set color of rectangle
        
        print 'Canvas # objs', len(self.objs)
        
        for i in range(len(self.objs)):
            if self.objs[i].color == None:
                g.setColor(self.defaultColor)
            else:
                g.setColor(self.objs[i].getColor())
            self.objs[i]._draw(g)
    
    def actionPerformed(self, a):
        pass
    
    def keyReleased(self, e):
        pass
    
    def keyPressed(self, e):
        pass
    
    def setDefaultColor(self, c):
        self.defaultColor = c
