from java.awt.event import ActionListener
from java.awt.event import KeyListener
from java.awt.event import MouseListener
from java.awt.Color import * # so we can just say gray instead of Color.gray
from java.awt import Font, Toolkit
from java.awt.Font import *
from javax.swing import JFrame, JPanel
from java.awt.Graphics import fillRect, fillOval, setFont
from java.awt import Image
from javax.imageio import *
from java.net import URL
from java.lang import String
from java.lang import Math

# Filename: GraphicsLib.py
from java.awt.geom import AffineTransform

class GraphicsWindow(ActionListener, KeyListener, MouseListener):
    
    def __init__(self, title, width, height, backgroundColor = white):
        assert width >0, "GraphicsWindow width must be greater than zero"
        assert height >0, "GraphicsWindow height must be greater than zero"
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

class GraphicsObject(object):
    """
        Anything drawn on the canvas is a child of GraphicsObject.
        This class stores the location of the object (x, y) and
        has methods to rotate, flip, translate and move the object.        
    """
    
    def __init__(self, (x, y) = (0, 0), color = None):
        super(GraphicsObject, self).__init__()
        self.coordinates = (x, y) # (x,y) tuple of object's position
        self.color = color
        self.transform = AffineTransform()

    # Use degrees, not radians
    def rotate(self, degrees):
        pass
    
    def moveTo(self, x, y):
        self.coordinates = (x, y)
    #redraw?
    
    def move(self, deltaX, deltaY):
        self.moveTo(self.coordinates[0] + deltaX, self.coordinates[1] + deltaY)
    
    # Flip object on horizontal axis (mirror image)
    def flipX(self):
#        self.transform.scale(1.0, -1.0)
        (x, y) = self.coordinates
        self.coordinates = (x, -1.0 * y)

    
    # Flip object on vertical axis
    def flipY(self):
        pass
    
    def scale(self):
        pass
    
    def getColor(self):
        return self.color
    
    def getCoordinates(self):
        return self.coordinates
    
    def getX(self):
        return  self.coordinates[0]
    
    def getY(self):
        return  self.coordinates[1]
    
    def setColor(self, c):
        self.color = c
    
    def setCoordinates(self, (x, y)):
        self.coordinates = (x, y)
    
    def setX(self, x):
        self.coordinates[0] = x
    
    def setY(self, y):
        self.coordinates[1] = y


class Text(GraphicsObject):
    def __init__(self, (x, y), s, font, size, attribute = PLAIN, color = None):
        assert size >0, "Text size must be greater than zero"
        super(Text, self).__init__((x, y), color)
        self.s = s
        self.font = font # Font, however it's defined in Java...
        self.size = size
        self.attribute = attribute #bold, italic, underline
    
    def getString(self):
        return self.s
    
    def getSize(self):
        return self.size
    
    def getAttribute(self):
        return self.attribute
    
    def getFont(self):
        return self.font
    
    def setString (self, s):
        self.s = s
    
    def setSize(self, s):
        self.size = s
    
    def setAttribute(self, a):
        self.attribute = a
    
    def setFont(self, f):
        self.font = f
    
    def _draw(self, g):
        g.setFont(Font(self.font, self.attribute, self.size))
        g.drawString(self.s, self.coordinates[0], self.coordinates[1])

class Image(GraphicsObject):
    def __init__(self, (x, y), url, width, height):
        assert width >0, "Image width must be greater than zero"
        assert height >0, "Image height must be greater than zero"
        super(Image, self).__init__((x,y))

        self.url = url
        self.imageURL = url
        self.width = width
        self.height = height
    
    def setUrl(self, u):
        self.url = u
    
    def setWidth(self, w):
        assert w >0, "Image width must be greater than zero"
        self.width = w
    
    def setHeight(self, h):
        assert h >0, "Image height must be greater than zero"
        self.Height = h
    
    def getUrl(self):
        return self.url
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def _draw(self, g):
        img = ImageIO.read(URL(String(self.url)))
        g.drawImage(img, self.coordinates[0], self.coordinates[1], None)
        w = img.getWidth(null);
        h = img.getHeight(null);

class Shape(GraphicsObject):
    def __init__(self, (x, y), width, height, color = None, filled = True):
        super(Shape, self).__init__((x, y), color)
        self.width = width
        self.height = height
        self.filled = filled
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getFilled(self):
        return self.filled
    
    def setWidth(self, w):
        assert w >0, "Shape width must be greater than zero"
        self.width = w
    
    def setHeight(self, h):
        assert h >0, "Shape height must be greater than zero"
        self.height = h
    
    def setFilled(self, f):
        self.filled = f


class Ellipse(Shape):
    def __init__(self, (x, y), width, height, color = None, filled = True):
        assert width >0, "Ellipse width must be greater than zero"
        assert height >0, "Ellipse height must be greater than zero"
        super(Ellipse, self).__init__((x, y), width, height, color, filled)
    
    def scale(self):
        pass

    
    def _draw(self, g):
        if self.filled:
            g.fillOval(self.coordinates[0],
                       self.coordinates[1],
                       self.width,
                       self.height)
        else:
            g.drawOval(self.coordinates[0],
                       self.coordinates[1],
                       self.width,
                       self.height)
    
    def rotate(self, degrees):
        math.radians(degrees)

class Circle(Ellipse):
    def __init__(self, (x, y), radius, color = None, filled = True):
        assert radius >0, "Circle radius must be greater than zero"
        super(Circle, self).__init__((x, y), color = self.color, filled = self.filled)
        self.radius = radius
    
    def setRadius(self, r):
        assert r >0, "Circle radius must be greater than zero"
        self.radius = r
    
    def getRadius(self):
        return self.radius
    
    def scale(self, scale):
        self.radius = self.radius * scale
    
    def _draw(self, g):
        x = x + self.radius
        y = y + self.radius
        if self.filled:
            g.fillOval(x, y, self.radius*2, self.radius*2)
        else:
            g.drawOval(x, y, self.radius*2, self.radius*2)

class Rectangle(Shape):
    def __init__(self, (x, y), width, height, color = None, filled = True):
        assert width >0, "Rectangle width must be greater than zero"
        assert height >0, "Rectangle height must be greater than zero"
        super(Rectangle, self).__init__((x, y), width, height, color, filled)
    
    def _draw(self, g):
        if self.filled:
            g.fillRect(self.coordinates[0], self.coordinates[1],
                       self.width, self.height)
        else:
            g.drawRect(self.coordinates[0], self.coordinates[1],
                       self.width, self.height)

class Line(Shape):
    def __init__(self, (startX, startY), (endX, endY), color = None):
        super(Line, self).__init__((startX, startY), None, None, color, None)
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
    
    def _draw(self, g):
        g.drawLine(self.startX, self.startY, self.endX, self.endY)

class Point(Line):
    def __init__(self, (x, y), color = None):
        super(self, (x, y), None, color)
        self.x = x
        self.y = y
    
    def _draw(self, g):
        g.drawLine(self.x, self.y, self.x, self.y)

class Arc(Shape):
    def __init__(self, (x, y), width, height, startAngle, arcAngle, color =  None):
        # Why does arc have width and height?
        assert width >0, "Arc width must be greater than zero"
        assert height >0, "Arc height must be greater than zero"
        super(Arc, self).__init__((x, y), width, height, color = self.color)
        self.startAngle = startAngle
        self.arcAngle = arcAngle
    
    def _draw(self, g):
        g.fillArc(self.coordinates[0], self.coordinates[1],
                  self.weigth, self.height, self.startAngle, self.arcAngle)


class Polygon(Shape):
    def __init__(self, vertices, color = None, filled = True):
        super(Polygon, self).__init__(self, color = self.color, filled = True)
        self.vertices = vertices
    
    def _draw(self, g):
        (xValues, yValues) = zip(*vertices)
        if self.filled:
            g.fillPolygon(xValues, yValues, vertices.length)
        else:
            g.drawPolygon(xValues, yValues, vertices.length)

## Parking lot: class RegPolygon(Polygon):

class Group():
    def __init__(self, *objects):
        self.group = []
        for o in objects:
            assert isinstance(o, GraphicsObject), "%s is not GraphicsObject" % o
            self.group.append(o)
    
    # removing and adding objects
    def remove(self, *objects):
        for o in objects:
            self.group.remove(o)
    
    # append
    def append(self, *objects):
        for o in objects:
            assert isinstance(o, GraphicsObject), "%s is not a GraphicsObject" % o
            self.group.append(o)
    
    # translating
    def move(self, deltaX, deltaY):
        for o in self.group:
            o.move(deltaX, deltaY)
    
    # rotate all objects on their centers
    def rotateAroundPoint(self, degree):
        for o in self.group:
            o.rotate(degree)
    

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
    z.draw(w)
    w.draw(t)
    w.draw(image)
    w.setVisible(True)




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

