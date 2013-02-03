from GraphicsObject import *
from java.awt.Graphics import fillRect, fillOval

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
        assert w > 0, "Shape width must be greater than zero"
        self.width = w
    
    def setHeight(self, h):
        assert h > 0, "Shape height must be greater than zero"
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
        assert width > 0, "Rectangle width must be greater than zero"
        assert height > 0, "Rectangle height must be greater than zero"
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
        assert width > 0, "Arc width must be greater than zero"
        assert height > 0, "Arc height must be greater than zero"
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
