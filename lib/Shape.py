from GraphicsObject import *
from java.awt.Graphics import fillRect, fillOval
from java.awt.Graphics2D import *  # Hopefully, refine this later.
from java.lang.Math import PI, cos, sin
from java.awt import Color


class Shape(GraphicsObject):
    """
    Shape inherits from GraphicsObject. Any shape that is drawn on the
    canvas inherits from Shape. Shape stores the width and height of the
    object. As well a boolean stating whether or not it is filled and
    another boolean that stores whether or not the shape should be drawn
    with a stroke. The stroke color for the Shape is also stored in this
    class.
    """

    def __init__(self, (x, y), width, height, color=None, filled=True):
        """
        Constructor for Shape class. Coordinates and color are passed
        to the super class. Coodinates, width and height are required
        parameters in order to create the object. If no color is passed
        the default color is the default color of the window. Initially
        stroke is set to False and strokeColor is None. strokeColor and
        stroke are later set by the draw method in window.
        """

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
        """
        Hidden draw method for all Shape objects. Each shape that inherits from
        Shape needs to have its own _draw method or two methods: _draw_shape()
        and _draw_stroke(). If the class that inherits from Shape just has a
        _draw method that method will be used to draw the object. This is the
        case for shapes that don't need a stroke. If a shape doesn't have a stroke
        it will be drawn using _draw_shape(). If it does have a stroke after
        the filled circle is _draw_stroke() will draw an unfilled circle over
        it creating a stroke.
        """
        g.setColor(self.color)
        self._draw_shape(g)
        if self.filled and self.stroke:
            g.setColor(self.strokeColor)
            self._draw_stroke(g)


class Ellipse(Shape):
    """
    Inherits from Shape. The (x,y) coordinates represent top left hand corner
    of the bounding rectangle.
    """
    def __init__(self, (x, y), width, height, color=None, filled=True):
        assert width > 0, "Ellipse width must be greater than zero"
        assert height > 0, "Ellipse height must be greater than zero"
        super(Ellipse, self).__init__((x, y), width, height, color, filled)

    def _draw_stroke(self, g):
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

    def scale(self):
        pass

    def rotate(self, degrees):
        pass
        # math.radians(degrees)


class Circle(Ellipse):
    """
    Circle inherits its draw methods from Ellipse. The (x, y) coordinates of a Circle represent its center.
    """

    # (x,y) - center of Circle
    def __init__(self, (x, y), radius, color=None, filled=True):
        assert radius > 0, "Circle radius must be greater than zero"
        super(Circle, self).__init__(
            (x - radius, y - radius), radius * 2, radius * 2, color, filled)
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
        g.drawRect(self.coordinates[0], self.coordinates[1],
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

    def _draw_shape(self, g):
        if self.filled:
            g.fillArc(self.coordinates[0], self.coordinates[1],
                      self.width, self.height, self.startAngle, self.arcAngle)
        else:
            g.drawArc(self.coordinates[0], self.coordinates[1],
                      self.width, self.height, self.startAngle, self.arcAngle)

    def _draw_stroke(self, g):
        g.drawArc(self.coordinates[0], self.coordinates[1],
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

    def _draw_shape(self, g):
        (xValues, yValues) = zip(*self.vertices)
        if self.filled:
            g.fillPolygon(xValues, yValues, self.sides)
        else:
            g.drawPolygon(xValues, yValues, self.sides)

    def _draw_stroke(self, g):
        (xValues, yValues) = zip(*self.vertices)
        g.drawPolygon(xValues, yValues, self.sides)
