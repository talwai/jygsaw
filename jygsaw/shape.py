from java.awt import BasicStroke
from java.awt import Color
from java.awt import Polygon as JavaPolygon
from java.awt.geom import Rectangle2D, Ellipse2D, Line2D, Arc2D
from java.lang.Math import PI, cos, sin
from warnings import warn


class Shape():

    """
    Any shape that is drawn on the canvas inherits from Shape. Shape
    stores the width, height, color, strokeColor, and strokeWidth of
    the object. As well a boolean stating whether or not it is filled and
    another boolean that stores whether or not the shape should be drawn
    with a stroke. This class also contains the draw method for all of the
    shapes.

    Constructor for :py:class:`~jygsaw.shape.Shape` classs does not take
    any parameters except for the color. Initially stroke is set to False,
    strokeColor is black, and strokeWidth is set to 1. StrokeColor and stroke
    are later set by the draw method in graphicsWindow.

    """

    def __init__(self, color):
        self._color = color
        self._filled = True
        self._stroke = False
        self._strokeColor = Color.black
        self._strokeWidth = 1

    def _get_color(self):
        """Returns the color of the :py:class:`~jygsaw.shape.Shape` """
        return self._color

    def _set_color(self, c):
        """Sets the color of the :py:class:`~jygsaw.shape.Shape` """
        assert c is None or isinstance(
            c, Color), "The object passed is not a Color object."
        self._color = c

    color = property(_get_color, _set_color, doc="Color of the shape.")

    def _get_filled(self):
        """Returns the boolean value of filled"""
        return self._filled

    def _set_filled(self, f):
        """Sets the boolean value of filled"""
        assert isinstance(f, bool), "Filled must be set to a Boolean"
        self._filled = f

    filled = property(_get_filled, _set_filled,
                      "Boolean describing if the shape is filled.")

    def _get_stroke(self):
        return self._stroke

    def _set_stroke(self, s):
        assert isinstance(s, bool), "Stroke must be set to a Boolean"
        self._stroke = s

    stroke = property(_get_stroke, _set_stroke,
                      "Boolean describing if the shape has a stroke.")

    def _get_strokeColor(self):
        return self._strokeColor

    def _set_strokeColor(self, c):
        assert c is None or isinstance(
            c, Color), "The object passed is not a Color object."
        self._strokeColor = c

    strokeColor = property(_get_strokeColor, _set_strokeColor,
                           "Color of the stroke.")

    def _get_strokeWidth(self):
        return self._strokeWidth

    def _set_strokeWidth(self, w):
        assert isinstance(w, int), "strokeWidth must be an integer."
        self._strokeWidth = w

    strokeWidth = property(_get_strokeWidth, _set_strokeWidth,
                           "Width of the stroke.")

    def _draw(self, g):
        if self.filled:
            g.setColor(self.color)
            g.fill(self)
        else:
            g.setColor(self.color)
            g.draw(self)
        if self.stroke:
            g.setPaint(self.strokeColor)
            g.setStroke(BasicStroke(self.strokeWidth))
            g.draw(self)

        if not self.filled and not self.stroke:
            warn('Shape filled and stroke are both set to false.')


class Rectangle(Rectangle2D.Float, Shape):

    """
    The Rectangle class describes a rectangle defined by its top left corner,
    width, and height. Rectangle inherits from Rectangle2D.Float and 
    :py:class:`~jygsaw.shape.Shape` .

    Creates a Rectangle where x and y describe the top left coordinate of
    the rectangle. Width and height set the width and height, respectively,
    of the rectangle. An optional color can also be given.

    """

    def __init__(self, x, y, width, height, color=None):
        super(Rectangle, self).__init__(x, y, width, height, color=color)

    def moveTo(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY


class Ellipse(Ellipse2D.Float, Shape):

    """
    The Ellipse class describes an ellipse that is defined by a bounding
    rectangle. Inherits from Ellipse2D.Float and
    :py:class:`~jygsaw.shape.Shape` .

    Creates an :py:class:`~jygsaw.shape.Ellipse` where x and y represent the
    top left hand corner of the counding rectangle. Width and height define
    the bounding rectangle's width and height, respectively. An optional color
    can also be passed.

    """

    def __init__(self, x, y, width, height, color=None):
        super(Ellipse, self).__init__(x, y, width, height, color=color)

    def moveTo(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY


class Circle(Ellipse2D.Float, Shape):

    """
    The Circle class describes a circle that is defined by its center point
    and radius. It inherits from Ellipse2D and
    :py:class:`~jygsaw.shape.Shape` .

    Creates a circle that is centered at (x, y) with a given radius. An
    optional color can also be passed.

    """

    def __init__(self, x, y, radius, color=None):
        assert radius > 0, "Circle radius must be greater than zero."
        super(Circle, self).__init__(x - radius, y - radius, radius * 2, radius * 2, color=color)
        self._radius = radius

    def _get_radius(self):
        return self._radius

    def _set_radius(self, r):
        assert isinstance(
            r, int) and r > 0, "Circle radius must be greater than zero and an integer."
        self._radius = r
        self.width = r * 2

    radius = property(_get_radius, _set_radius, "Radius of the circle.")

    def _get_x(self):
        return self.getX() + self.radius

    def _set_x(self, x):
        self.setFrame(x - self.radius, self.getY(), self.width, self.height)

    x = property(_get_x, _set_x, "X coordinate of the circle.")

    def _get_y(self):
        return self.getY() + self.radius

    def _set_y(self, y):
        self.setFrame(self.getX(), y - self.radius, self.width, self.height)

    y = property(_get_y, _set_y, "Y coordinate of the circle.")

    def moveTo(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY


class Line(Line2D.Float, Shape):

    """
    The Line class describes a line that is defined by a start point and
    an end point. It inherits from Line2D and :py:class:`~jygsaw.shape.Shape` .

    Creates a line that starts at startX and startY, and ends at endX
    and endY. An optional color can also be given.

    """

    def __init__(self, startX, startY, endX, endY, color=None):
        super(Line, self).__init__(startX, startY, endX, endY, color=color)

    def moveTo(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY


class Point(Line):

    """
    The Point class describes a point that is defined by an x and y coordinate.
    It inherits from :py:class:`~jygsaw.shape.Line` ; the start and end
    coordinates are the same.

    Creates a point at x, y with an optional color.
    """

    def __init__(self, x, y, color=None):
        super(Point, self).__init__(x, y, x, y, color)


class Arc(Arc2D.Float, Shape):

    """
    The Arc class describes an arc. According to polar coordinate convention,
    0 degrees points and 3 o'clock, positive degree values are in the counter-
    clockwise direction, and negative degree values are in the clockwise
    direction. The arc is defined by a bounding rectangle, start angle,
    and arc angle. The bounding rectangle is defined by its top left corner,
    width, and height. Inherits from Arc2D and :py:class:`~jygsaw.shape.Shape`.
    startAngle is where the arc begins; arc is extended for arcAngle degrees
    x, y - upper left corner of the arc's rectangle to be filled
    width and height are the width and height of the arc to be filled

    Creates an arc within a bounding rectangle defined by upper left
    corner at x, y with given width and height. The arc begins at
    startAngle and extends for arcAngle degrees. An optional color can
    also be given.

    """

    def __init__(self, x, y, width, height, startAngle, arcAngle, color=None):
        super(Arc, self).__init__(x, y, width, height, startAngle,
                                  arcAngle, Arc2D.OPEN, color=color)

    def moveTo(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY


class Polygon(JavaPolygon, Shape):

    """
    The Polygon class describes a polygon defined by a list of points. Inherits
    from Java's Polygon class and :py:class:`~jygsaw.shape.Shape` .

    Creates a polygon defined by a list of vertices as (x, y). Sequential
    vertices are connected via line segments. The polygon is closed by
    connecting the first and last vertices.

    """

    def __init__(self, vertices, color=None):
        assert len(vertices) > 0, "Number of vertices must be greater than 0 "
        (xValues, yValues) = zip(*vertices)
        super(Polygon, self).__init__(xValues, yValues, len(
            vertices), color=color)
        self._vertices = vertices

    def _get_vertices(self):
        return self._vertices

    def _set_vertices(self, v):
        assert v >= 1, "Number of sides must be greater than or equal to 0 "
        self._vertices = v

    vertices = property(_get_vertices, _set_vertices,
                        "List of vertices, where the vertices are tuples of two integers.")

    def moveTo(self, x, y):
        self.move(x - self.vertices[0][0], y - self.vertices[0][1])
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.vertices = [(x + deltaX, y + deltaY) for x, y in self.vertices]
        self.translate(deltaX, deltaY)


class RegPolygon(JavaPolygon, Shape):

    """
    The RegPolygon class describes a regular polygon defined by a start
    vertex, the number of sides, and side length. It inherits from Java's
    Polygon class and Shape.

    Inherits from the :py:class:`~jygsaw.shape.Polygon`  class in java and :py:class:`~jygsaw.shape.Shape`. Given an x, y
    coordinate, number of sides, length of the sides and a color a
    regular polygon is drawn on the window. The class generates a list of
    vertices, where the first vertex is the given x, y coordinate and the
    rest are calculated using the number of sides and the length
    of each of the sides.

    Creates a regular polygon where the first vertex is x and y. It is
    also defined by the number of sides and length. An optional color
    can also be given.

    """

    def __init__(self, x, y, sides, length, color=None):
        assert sides >= 3, "Number of sides must be greater than or equal to 3"
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

        (xValues, yValues) = zip(*self.vertices)
        super(RegPolygon, self).__init__(
            xValues, yValues, len(self.vertices), color=color)

    def _get_vertices(self):
        return self._vertices

    def _set_vertices(self, v):
        assert v > 0, "Number of vertices must be greater than 0"
        self._vertices = v

    vertices = property(_get_vertices, _set_vertices,
                        "List of vertices, where the vertices are tuples of two integers.")

    def _get_sides(self):
        return self._sides

    def _set_sides(self, s):
        assert s >= 3, "Number of sides must be greater than or equal to 3."
        self._sides = s
        self.sideAngle = (2 * PI) / self._sides

    sides = property(
        _get_sides, _set_sides, "An integer setting the number of sides. ")

    def _set_sideLength(self):
        return self._sideLength

    def _get_sideLength(self, l):
        assert l > 0, "Length of sides must be greater than 0"
        self._sideLength = l
        self.radius = self._sideLength * sin(.5 * (PI - self.sideAngle)) / \
            sin(self.sideAngle)

    sideLength = property(
        _set_sideLength, _get_sideLength, "Length of each side.")

    def moveTo(self, x, y):
        self.move(x - self.vertices[0][0], y - self.vertices[0][1])
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.vertices = [(x + deltaX, y + deltaY) for x, y in self.vertices]
        self.translate(deltaX, deltaY)
