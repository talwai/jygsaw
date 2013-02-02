# Filename: GraphicsLib.py

from java.awt.event import ActionListener, KeyListener, MouseListener
from java.awt.Color import * # so we can just say gray instead of Color.gray
from javax.swing import JFrame, JPanel
from java.lang import Math
from Image import *
from Group import *
from Shape import *
from Text import *

class GraphicsWindow(ActionListener, KeyListener, MouseListener):
    
    def __init__(self, title, width, height, backgroundColor = white):
        assert width > 0, "GraphicsWindow width must be greater than zero"
        assert height > 0, "GraphicsWindow height must be greater than zero"
        self.objs = [] # List of Jy_Objects
        self.width = width
        self.height = height
        self.frame = JFrame(title,defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
                            size = (self.width, self.height))
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
        g.clearRect(0, 0, self.window.width, self.window.height)
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


# Buttons, etc
# class Components:


## Parking lot: class RegPolygon(Polygon):

if ( __name__ == '__main__' ) or ( __name__ == 'main' ) :
    w = GraphicsWindow('Demo Time', 500, 500, black)
    w.setDefaultColor(pink)
    e = Ellipse((100, 100), 35, 35, filled=False)
    r = Rectangle((250, 250), 100, 200, blue)
    w.setDefaultColor(green)
    t = Text((400, 300), "Hello!", "Arial", 40)
    sun = Ellipse((115, 110), 75, 75, yellow)
    l = Line ((5,10),(100,150))
    image = Image((20, 20), "puppy.jpg", 400, 400)
    z = Group (r, e, sun)
    z.move(100, 100)
    #    z.draw(w)
    w.draw(t)
    w.draw(image)
    w.setVisible(True)

    #this is a sample url image that we can use for testing things
    #http://cdn.cutestpaw.com/wp-content/uploads/2011/11/Handsome-l.jpg




# TODO
# implement group.draw() in window class
#
# demo of shape responding to mouse/key events

#End of GraphicsLib.py

#use graphics2d, antialiasing
#animation style:
# 1) cs1lib, 
# 2) while loop


# instance variables should be functions
# i.e. mouseX() instead of mouseX

# setStrokeColor() instead of setStroke()

# all graphics library are non thread-safe
# look up event dispatch thread for swing
# invoke later

# avoiding two threads
# 1) wrap things in invokelater()

