from java.awt import BasicStroke
from java.awt import Color
from java.awt import Polygon as JavaPolygon
from java.awt.geom import Rectangle2D, Ellipse2D, Line2D, Arc2D
from java.lang.Math import PI, cos, sin
from warnings import warn


class Shape():
    """
    Any shape that is drawn on the canvas inherits from Shape. Shape
    stores the width, height, color,, strokeColor and strokeWidth of
    the object. As well a boolean stating whether or not it is filled and
    another boolean that stores whether or not the shape should be drawn
    with a stroke. This class also contains the draw method for all of the shapes.
    """

    def __init__(self, color):
        """
        Constructor for Shape class. This class does not take any parameters
        except for the color. Initially stroke is set to False, strokeColor
        is black and strokeWidth is set to 1. strokeColor and stroke are
        later set by the draw method in graphicsWindow.
        """

        self._color = color
        self._filled = True
        self._stroke = False
        self._strokeColor = Color.black
        self._strokeWidth = 1

    def _get_color(self):
        """Returns the color of the GraphicsObject."""
        return self._color

    def _set_color(self, c):
        """Sets the color of the GraphicsObject."""
        assert c == None or isinstance(c, Color), "The object passed is not a Color object."
        self._color = c

    color = property(_get_color, _set_color, doc="Color of the object.")

    def _get_filled(self):
        """Returns the boolean value of filled"""
        return self._filled

    def _set_filled(self, f):
        """Sets the value of filled"""
        assert isinstance(f, bool), "Filled must be set to a Boolean"
        self._filled = f

    filled = property(_get_filled, _set_filled,
        "Boolean describing whether the shaped is filled or not.")

    def _get_stroke(self):
        return self._stroke

    def _set_stroke(self, s):
        assert isinstance(s, bool), "Stroke must be set to a Boolean"
        self._stroke = s

    stroke = property(_get_stroke, _set_stroke,
        "Boolean describing whether the shape has a stroke or not.")

    def _get_strokeColor(self):
        return self._strokeColor

    def _set_strokeColor(self, c):
        assert c == None or isinstance(c, Color), "The object passed is not a Color object."
        self._strokeColor = c

    strokeColor = property(_get_strokeColor, _set_strokeColor,
        "Color of the stroke.")

    def _get_strokeWidth(self):
        return self._strokeWidth

    def _set_strokeWidth(self, w):
        assert isinstance(w, int), "strokeWidth must be a integer."
        self._strokeWidth = w

    strokeWidth = property(_get_strokeWidth, _set_strokeWidth,
        "Width of the stroke")

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
            # Throw a warning!
            warn('Shape filled and stroke are both set to false.')


class Rectangle(Rectangle2D.Float, Shape):

    """
    Inherits from Rectangle2D.Float and Shape. Its arguments are
    x, y, width, height and optionally color. A rectangle is drawn
    on the screen with its top-left corner at the x, y coordinate.
    """

    def __init__(self, x, y, width, height, color=None):
        super(Rectangle, self).__init__(x, y, width, height, color=color)


class Ellipse(Ellipse2D.Float, Shape):

    """
    Inherits from Ellipse2D.Float and Shape. The x, y coordinates
    represent top left hand corner of the bounding rectangle, and
    width and height define the bounding rectangle's width and
    height, respectively.
    """

    def __init__(self, x, y, width, height, color=None):
        super(Ellipse, self).__init__(x, y, width, height, color=color)


class Circle(Ellipse2D.Float, Shape):

    """
    Circle inherits from Ellipse2D and Shape. The x, y coordinates of a Circle
    represent its center, instead of the upper left corner of
    the bounding box, and it takes a radius as well.
    """

    # This NEEDS to be more carefully looked at. I tried to overwrite
    # getters and setters for the x and y values, but they currently do not
    # update the x and y values of the super class which means that if
    # the x and y values are updated the shape won't be drawn in the correct
    # place . Mostly because of namespace issues. I have not devised
    # a solution yet. --Carla

    def __init__(self, x, y, radius, color=None):
        assert radius > 0, "Circle radius must be greater than zero"
        super(Circle, self).__init__(x - radius, y - radius, radius * 2, radius * 2, color=color)
        self._radius = radius

    def _get_radius(self):
        return self._radius

    def _set_radius(self, r):
        assert isinstance(r, int) and r > 0, "Circle radius must be greater than zero and an integer."
        self._radius = r
        self.width = r * 2

    radius = property(_get_radius, _set_radius, "Radius of the Circle.")

    def _get_x(self):
        return self.x + self.radius

    def _set_x(self, x):
        self.x = x - self.radius

    x = property(_get_x, _set_x, "X coordinate of the Circle.")

    def _get_y(self):
        return self.y + self.radius

    def _set_y(self, y):
        self.y = y - self.radius

    y = property(_get_y, _set_y, "Y coordinate of the Circle.")

    def moveTo(self, x, y):
        self.move(x - self.x, y - self.y)
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.translate(deltaX, deltaY)

class Line(Line2D.Float, Shape):

    """
    Inherits from Shape. Its arguments are the start x, y, the
    end x, y and a color. A line is drawn on the screen from the
    start point to the end point.
    """

    def __init__(self, startX, startY, endX, endY, color=None):
        super(Line, self).__init__(startX, startY, endX, endY, color=color)

    def moveTo(self, x, y):
        self.move(x - self.x, y - self.y)
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.translate(deltaX, deltaY)

class Point(Line):

    """
    Inherits from Line. Its arguments are x, y coordinates and
    color. The draw method from line is used; a line is drawn that
    starts and ends at the same point.
    """

    # (x, y) - coordinate of point
    # draws a line with the same start and end point
    def __init__(self, x, y, color=None):
        super(Point, self).__init__(x, y, x, y, color)



class Arc(Arc2D.Float, Shape):

    """
    Based in polar coordinate convention, with 0 degrees pointing 3 o'clock
    positive degree values are in the counter-clockwise direction; negative in clockwise
    startAngle is where the arc begins; arc is extended for arcAngle degrees
    x, y - upper left corner of the arc's rectangle to be filled
    width and height are the width and height of the arc to be filled
    """

    def __init__(self, x, y, width, height, startAngle, arcAngle, color=None):
        super(Arc, self).__init__(x, y, width, height, startAngle, arcAngle, Arc2D.OPEN, color=color)

    def moveTo(self, x, y):
        self.move(x - self.x, y - self.y)
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.translate(deltaX, deltaY)

class Polygon(JavaPolygon, Shape):

    """
    Inherits from the Polygon class in java and Shape. Given
    a list of vertices, the points are connected in order to
    create a polygon.
    """

    def __init__(self, vertices, color=None):
        assert len(vertices) > 0, "Number of vertices must be greater than 0 "
        (xValues, yValues) = zip(*vertices)
        super(Polygon, self).__init__(xValues, yValues, len(vertices), color=color)
        self._vertices = vertices

    def _get_vertices(self):
        return self._vertices

    def _set_vertices(self, v):
        assert v >= 1, "Number of sides must be greater than or equal to 0 "
        self._vertices = v

    vertices = property(_get_vertices, _set_vertices, "List of vertices, where the vertices are tuples of two integers.")

    def moveTo(self, x, y):
        self.move(x - self.vertices[0][0], y - self.vertices[0][1])
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.vertices = [(x + deltaX, y + deltaY) for x,y in self.vertices]
        self.translate(deltaX, deltaY)


class RegPolygon(JavaPolygon, Shape):

    """
    Inherits from the Polygon class in java and Shape. Given an x, y
    coordinate, number of sides, length of the sides and a color a
    regular polygon is drawn on the window. The class generates a list of
    vertices, where the first vertex is the given x, y coordinate and the
    rest are calculated using the number of sides and the length
    of each of the sides.
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
        super(RegPolygon, self).__init__(xValues, yValues, len(self.vertices), color=color)

    def _get_vertices(self):
        return self._vertices

    def _set_vertices(self, v):
        assert v > 0, "Number of vertices must be greater than 0"
        self._vertices = v

    vertices = property(_get_vertices, _set_vertices, "List of vertices, where the vertices are tuples of two integers.")

    def _get_sides(self):
        return self._sides

    def _set_sides(self, s):
        assert s >= 3, "Number of sides must be greater than or equal to 3"
        self._sides = s
        self.sideAngle = (2 * PI) / self._sides

    sides = property(_get_sides, _set_sides, "An integer setting the number of sides. ")

    def _set_sideLength(self):
        return self._sideLength

    def _get_sideLength(self, l):
        assert l > 0, "Length of sides must be greater than 0"
        self._sideLength = l
        self.radius = self._sideLength * sin(.5 * (PI - self.sideAngle)) / \
            sin(self.sideAngle)

    sideLength = property(_set_sideLength, _get_sideLength, "Length of each side.")

    def moveTo(self, x, y):
        self.move(x - self.vertices[0][0], y - self.vertices[0][1])
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.vertices = [(x + deltaX, y + deltaY) for x,y in self.vertices]
        self.translate(deltaX, deltaY)

