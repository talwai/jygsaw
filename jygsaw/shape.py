from graphicsobject import *
from java.awt.Graphics import fillRect, fillOval
from java.awt.Graphics2D import *  # Hopefully, refine this later.
from java.lang.Math import PI, cos, sin
from java.awt import Color
from warnings import warn


class Shape(GraphicsObject):
    """
    Shape inherits from GraphicsObject. Any shape that is drawn on the
    canvas inherits from Shape. Shape stores the width and height of the
    object. As well a boolean stating whether or not it is filled and
    another boolean that stores whether or not the shape should be drawn
    with a stroke. The stroke color for the Shape is also stored in this
    class.
    """

    def __init__(self, x, y, width, height, color=None):
        """
        Constructor for Shape class. Coordinates and color are passed
        to the super class. Coodinates, width and height are required
        parameters in order to create the object. If no color is passed
        the default color is the default color of the window. Initially
        stroke is set to False and strokeColor is None. strokeColor and
        stroke are later set by the draw method in window.
        """

        super(Shape, self).__init__(x, y, color)
        self._width = width
        self._height = height
        self._filled = True
        self._stroke = False
        self._strokeColor = None

    def _get_width(self):
        """Returns the value of width."""
        return self._width

    def _set_width(self, w):
        """Sets the value of width as long as the value is greater than zero."""
        assert w > 0, "Shape width must be greater than zero"
        self._width = w

    width = property(_get_width, _set_width,
        "Integer describing the width of the Shape.")

    def _get_height(self):
        """Return the value of height"""
        return self._height

    def _set_height(self, h):
        """Sets the value of height as long as the value is greater than zero"""
        assert h > 0, "Shape height must be greater than zero"
        self._height = h

    height = property(_get_height, _set_height,
        "Integer describing the height of the Shape")

    def _get_filled(self):
        """Returns the boolean value of filled"""
        return self._filled

    def _set_filled(self, f):
        """Sets the value of filled"""
        self._filled = f

    filled = property(_get_filled, _set_filled,
        "Boolean describing whether the shaped is filled or not.")

    def _get_stroke(self):
        return self._stroke

    def _set_stroke(self, s):
        self._stroke = s

    stroke = property(_get_stroke, _set_stroke,
        "Boolean describing whether the shape has a stroke or not.")

    def _get_strokeColor(self):
        return self._strokeColor

    def _set_strokeColor(self, c):
        self._strokeColor = c

    strokeColor = property(_get_strokeColor, _set_strokeColor,
        "Color of the stroke.")

    def _draw(self, g):
        """
        Hidden draw method for all Shape objects. Each shape that inherits from
        Shape needs to have its own _draw method or two methods: _draw_fill()
        and _draw_stroke(). If the class that inherits from Shape just has a
        _draw method that method will be used to draw the object. This is the
        case for shapes that don't need a stroke. If a shape has a fill,
        it will be drawn using _draw_fill(). If it does have a stroke, then
        the shape outline is drawn using _draw_stroke(). If stroke and filled
        are false, then a warning is thrown.
        """

        if self.filled:
            g.setColor(self.color)
            self._draw_fill(g)
        if self.stroke:
            g.setColor(self.strokeColor)
            self._draw_stroke(g)
        if not self.filled and not self.stroke:
            # Throw a warning!
            warn('Shape filled and stroke are both set to false')


class Ellipse(Shape):
    """
    Inherits from Shape. The (x,y) coordinates represent top left hand corner
    of the bounding rectangle, and width and height define the bounding
    rectangle's width and height, respectively.
    """
    def __init__(self, x, y, width, height, color=None):
        assert width > 0, "Ellipse width must be greater than zero"
        assert height > 0, "Ellipse height must be greater than zero"
        super(Ellipse, self).__init__(x, y, width, height, color)

    def _draw_stroke(self, g):
        g.drawOval(self.x, self.y, self.width, self.height)

    def _draw_fill(self, g):
        g.fillOval(self.x, self.y, self.width, self.height)


class Circle(Shape):
    """
    Circle inherits from Shape. The (x, y) coordinates of a Circle
    represent its center, instead of the upper left corner of
    the bounding box, and it takes a radius as well.
    """

    # (x,y) - center of Circle
    def __init__(self, x, y, radius, color=None):
        assert radius > 0, "Circle radius must be greater than zero"
        super(Circle, self).__init__(x, y, radius * 2, radius * 2, color)
        self._radius = radius

    def _draw_stroke(self, g):
        g.drawOval(self.x - self.radius, self.y - self.radius,
                   self.radius * 2, self.radius * 2)

    def _draw_fill(self, g):
        g.fillOval(self.x - self.radius, self.y - self.radius,
                   self.radius * 2, self.radius * 2)

    def _get_radius(self):
        return self._radius

    def _set_radius(self, r):
        assert r > 0, "Circle radius must be greater than zero"
        self._radius = r

    radius = property(_get_radius, _set_radius, "Radius of the Circle.")


class Rectangle(Shape):
    # (x,y) - top-left vertex of Rectangle
    def __init__(self, x, y, width, height, color=None):
        assert width > 0, "Rectangle width must be greater than zero"
        assert height > 0, "Rectangle height must be greater than zero"
        super(Rectangle, self).__init__(x, y, width, height, color)

    def _draw_fill(self, g):
        g.fillRect(self.x, self.y, self.width, self.height)

    def _draw_stroke(self, g):
        g.drawRect(self.x, self.y, self.width, self.height)


class Line(Shape):

    """
    Inherits from Shape. Its arguments are the start (x, y), the
    end (x, y) and a color. A line is drawn on the screen from the
    start point to the end point.
    """

    def __init__(self, (startX, startY), (endX, endY), color=None):
        super(Line, self).__init__(startX, startY, 0, 0, color)
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY

    def _draw(self, g):
        g.setColor(self.color)
        g.drawLine(self.startX, self.startY, self.endX, self.endY)


class Point(Line):

    """
    Inherits from Line. Its arguments are an (x, y) coordinate and
    color. The draw method from line is used; a line is drawn that
    starts and ends at the same point.
    """
    # (x, y) - coordinate of point
    # draws a line with the same start and end point
    def __init__(self, x, y, color=None):
        super(Point, self).__init__((x, y), (x, y), color)
        self.x = x
        self.y = y


class Arc(Shape):
    """
    Based in polar coordinate convention, with 0 degrees pointing 3 o'clock
    positive degree values are in the counter-clockwise direction; negative in clockwise
    startAngle is where the arc begins; arc is extended for arcAngle degrees
    (x,y) - upper left corner of the arc's rectangle to be filled
    width and height are the width and height of the arc to be filled
    """

    def __init__(self, x, y, width, height, startAngle, arcAngle, color=None):

        assert width > 0, "Arc width must be greater than zero"
        assert height > 0, "Arc height must be greater than zero"
        super(Arc, self).__init__(x, y, width, height, color)
        self.startAngle = startAngle
        self.arcAngle = arcAngle

    def _draw_fill(self, g):
        g.fillArc(self.x, self.y, self.width, self.height,
                  self.startAngle, self.arcAngle)

    def _draw_stroke(self, g):
        g.drawArc(self.x, self.y, self.width, self.height,
                  self.startAngle, self.arcAngle)


class Polygon(Shape):

    """
    Inherits from Shape. Given a list of vertices, the points are connected
    in order to create a polygon.
    """

    def __init__(self, vertices, color=None):
        super(Polygon, self).__init__(
            vertices[0][0], vertices[0][1], 0, 0, color)
        assert len(vertices) > 0, "Number of vertices must be greater than 0 "
        self._vertices = vertices

    def _get_vertices(self):
        return self._vertices

    def _set_vertices(self, v):
        assert v >= 1, "Number of sides must be greater than or equal to 0 "
        self._vertices = v

    vertices = property(_get_vertices, _set_vertices, "List of vertices, where the vertices are tuples of two integers.")

    def _draw_fill(self, g):
        (xValues, yValues) = zip(*self.vertices)
        g.fillPolygon(xValues, yValues, len(self.vertices))

    def _draw_stroke(self, g):
        (xValues, yValues) = zip(*self.vertices)
        g.drawPolygon(xValues, yValues, len(self.vertices))

    def moveTo(self, x, y):
        self.move(x - self.x, y - self.y)

    def move(self, deltaX, deltaY):
        assert isinstance(deltaX, int), "The x value given is not an integer."
        assert isinstance(deltaY, int), "The y value given is not an integer."
        self.vertices = [(x + deltaX, y + deltaY) for x, y in self.vertices]


class RegPolygon(Shape):
    """
    Inherits from Shape. Given an (x, y) coordinate, number of sides, length of
    the sides and a color a regular polygon is drawn on the window. The class
    generates a list of vertices, where the first vertex is the given (x, y)
    coordinate and the rest are calculated using the number of sides and the length
    of each of the sides.
    """

    def __init__(self, x, y, sides, length, color=None):
        super(RegPolygon, self).__init__(x, y, 0, 0, color)
        assert sides >= 0, "Number of sides must be greater than or equal to 0 "
        assert length > 0, "Length of sides must be greater than 0 "

        self._vertices = []
        self._sides = sides
        self._sideLength = length
        self.sideAngle = (2 * PI) / self.sides
        self.radius = self.sideLength * sin(.5 * (PI - self.sideAngle)) / \
            sin(self.sideAngle)
        for i in range(self.sides):
            self.vertices.append((int(round(x + self.radius * cos(
                self.sideAngle * i))), int(round(y + self.radius * sin(self.sideAngle * i)))))

    def _get_vertices(self):
        return self._vertices

    def _set_vertices(self, v):
        assert v > 0, "Number of vertices must be greater that 0"
        self._vertices = v

    vertices = property(_get_vertices, _set_vertices, "List of vertices, where the vertices are tuples of two integers.")

    def _get_sides(self):
        return self._sides

    def _set_sides(self, s):
        assert sides >= 0, "Number of sides must be greater than or equal to 0 "
        self._sides = s
        self.sideAngle = (2 * PI) / self._sides

    sides = property(_get_sides, _set_sides, "An integer setting the number of sides. ")

    def _set_sideLength(self):
        return self._sideLength

    def _get_sideLength(self, l):
        assert l > 0, "Length of sides must be greater than 0"
        self._sideLength = l
        self.radius = self._sideLength * sin(.5 * (PI - self._sideAngle)) / \
            sin(self.sideAngle)

    sideLength = property(_set_sideLength, _get_sideLength, "Length of each side.")

    def _draw_fill(self, g):
        (xValues, yValues) = zip(*self.vertices)
        g.fillPolygon(xValues, yValues, self.sides)

    def _draw_stroke(self, g):
        (xValues, yValues) = zip(*self.vertices)
        g.drawPolygon(xValues, yValues, self.sides)

    def move(self, deltaX, deltaY):
        self.vertices = [(x + deltaX, y + deltaY) for x, y in self.vertices]
