from GraphicsObject import *
from java.awt.Graphics import fillRect, fillOval
from java.awt.Graphics2D import * # Hopefully, refine this later.
from java.lang.Math import PI, cos, sin
from java.awt import Color

# Set stroke for all of the shapes that could possible use it


class Shape(GraphicsObject):
    def __init__(self, (x, y), width, height, color=None, filled=True):
        super(Shape, self).__init__((x, y), color)
        self.width = width
        self.height = height
        self.filled = filled
        self.stroke = False
        self.strokeColor = None

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getFilled(self):
        return self.filled

    def setStroke(self, s):
        self.stroke = s

    def setStrokeColor(self, c):
        self.strokeColor = c

    def setWidth(self, w):
        assert w > 0, "Shape width must be greater than zero"
        self.width = w

    def setHeight(self, h):
        assert h > 0, "Shape height must be greater than zero"
        self.height = h

    def setFilled(self, f):
        self.filled = f

    def _draw(self, g):
        self._draw_shape(g)
        if self.stroke:
            self._draw_stroke(g)

class Ellipse(Shape):
    # (x,y) - center of Ellipse
    def __init__(self, (x, y), width, height, color=None, filled=True):
        assert width > 0, "Ellipse width must be greater than zero"
        assert height > 0, "Ellipse height must be greater than zero"
        super(Ellipse, self).__init__((x, y), width, height, color, filled)

    def scale(self):
        pass

    def _draw_stroke(self, g):
        g.setColor(self.strokeColor)
        g.drawOval(self.coordinates[0],
            self.coordinates[1],
            self.width,
            self.height)

    def _draw_shape(self, g):
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
    # (x,y) - center of Circle
    def __init__(self, (x, y), radius, color=None, filled=True):
        assert radius > 0, "Circle radius must be greater than zero"
        super(Circle, self).__init__((x - radius, y - radius), radius * 2, radius * 2, color, filled)
        self.radius = radius

    def setRadius(self, r):
        assert r > 0, "Circle radius must be greater than zero"
        self.radius = r

    def getRadius(self):
        return self.radius

    def scale(self, scale):
        self.radius = self.radius * scale


class Rectangle(Shape):
    # (x,y) - top-left vertex of Rectangle
    def __init__(self, (x, y), width, height, color=None, filled=True):
        assert width > 0, "Rectangle width must be greater than zero"
        assert height > 0, "Rectangle height must be greater than zero"
        super(Rectangle, self).__init__((x, y), width, height, color, filled)

    def _draw_shape(self, g):
        if self.filled:
            g.fillRect(self.coordinates[0], self.coordinates[1],
                       self.width, self.height)
        else:
            g.drawRect(self.coordinates[0], self.coordinates[1],
                       self.width, self.height)

    def _draw_stroke(self, g):
        g.fillRect(self.coordinates[0], self.coordinates[1],
            self.width, self.height)

class Line(Shape):
    # (startX, startY) - coordinate of line's starting point
    # (endX, endY) - coordinate of line's ending point
    def __init__(self, (startX, startY), (endX, endY), color=None):
        super(Line, self).__init__((startX, startY), 0, 0, color, True)
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY

    def _draw(self, g):
        g.drawLine(self.startX, self.startY, self.endX, self.endY)

class Point(Line):
    # (x, y) - coordinate of point
    # draws a line with the same start and end point
    def __init__(self, (x, y), color=None):
        super(Point, self).__init__((x, y), (x, y), color)
        self.x = x
        self.y = y

class Arc(Shape):
    # based in polar coordinate convention, with 0 degrees pointing 3 o'clock
    # positive degree values are in the counter-clockwise direction; negative in clockwise
    # startAngle is where the arc begins; arc is extended for arcAngle degrees
    # (x,y) - upper left corner of the arc's rectangle to be filled
    # width and height are the width and height of the arc to be filled
    def __init__(self, (x, y), width, height, startAngle, arcAngle, color=None):

        assert width > 0, "Arc width must be greater than zero"
        assert height > 0, "Arc height must be greater than zero"
        super(Arc, self).__init__((x, y), width, height, color)
        self.startAngle = startAngle
        self.arcAngle = arcAngle

    def _draw(self, g):
        g.fillArc(self.coordinates[0], self.coordinates[1],
                  self.width, self.height, self.startAngle, self.arcAngle)


class Polygon(Shape):
    def __init__(self, vertices, color=None, filled=True):
        super(Polygon, self).__init__(vertices[0], 0, 0, color, filled)
        self.vertices = vertices

    def _draw_shape(self, g):
        (xValues, yValues) = zip(*self.vertices)
        if self.filled:
            g.fillPolygon(xValues, yValues, len(self.vertices))
        else:
            g.drawPolygon(xValues, yValues, len(self.vertices))

    def _draw_stroke(self, g):
        (xValues, yValues) = zip(*self.vertices)
        g.drawPolygon(xValues, yValues, len(self.vertices))

class RegPolygon(Shape):
    def __init__(self, (x, y), sides, length, color=None, filled=True):
        super(RegPolygon, self).__init__((x, y), 0, 0, color, True)
        self.x = x
        self.y = y
        self.vertices = []
        self.sides = sides
        self.sideLength = length
        self.sideAngle = (2 * PI) / self.sides
        self.radius = self.sideLength * sin(.5 * (PI - self.sideAngle)) / \
            sin(self.sideAngle)
        for i in range(self.sides):
            self.vertices.append((int(round(x + self.radius * cos(
                self.sideAngle * i))), int(round(y + self.radius * sin(self.sideAngle * i)))))
        print "Vertices:", self.vertices

    def _draw_shape(self, g):
        (xValues, yValues) = zip(*self.vertices)
        if self.filled:
            g.fillPolygon(xValues, yValues, self.sides)
        else:
            g.drawPolygon(xValues, yValues, self.sides)

    def _draw_stroke(self, g):
        (xValues, yValues) = zip(*self.vertices)
        g.drawPolygon(xValues, yValues, self.sides)
