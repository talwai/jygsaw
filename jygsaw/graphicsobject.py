from java.awt.geom import AffineTransform
from java.awt import Color


class GraphicsObject(object):
    """
    Anything drawn on the canvas is a child of GraphicsObject.
    This class stores the location of the object (x, y) and
    has methods to rotate, flip, translate and move the object.
    The basic move method has been created rotate, scale, and flip are
    still in the process of being created.
    """

    def __init__(self, x=0, y=0, c=None):
        super(GraphicsObject, self).__init__()
        assert isinstance(x, int), "The x value given is not an integer."
        assert isinstance(y, int), "The x value given is not an integer."
        assert c == None or isinstance(c, Color), "The object pass is not a Color object."
        self._x = x
        self._y = y
        self._color = c
        self.transform = AffineTransform()

    def _get_x(self):
        """Returns the x coordinate value."""
        return self._x

    def _set_x(self, i):
        """Sets the x coordinate value."""
        assert isinstance(i, int), "The x value given is not an integer."
        self._x = i

    x = property(_get_x, _set_x, doc="x coordinate of object.")

    def _get_y(self):
        """Returns the y coordinate value."""
        return self._y

    def _set_y(self, i):
        """Sets the y coordinate value."""
        assert isinstance(i, int), "The y value given is not an integer."
        self._y = i

    y = property(_get_y, _set_y, doc="y coordinate of object.")

    def _get_color(self):
        """Returns the color of the GraphicsObject."""
        return self._color

    def _set_color(self, c):
        """Sets the color of the GraphicsObject."""
        assert c == None or isinstance(c, Color), "The object pass is not a Color object."
        self._color = c

    color = property(_get_color, _set_color, doc="Color of the object.")

    def moveTo(self, x, y):
        """The object is moved to the given coordinates."""
        assert isinstance(x, int), "The x value given is not an integer."
        assert isinstance(y, int), "The y value given is not an integer."
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """The object moves by deltaX and deltaY in the x and y direction, respectively."""
        assert isinstance(deltaX, int), "The x value given is not an integer."
        assert isinstance(deltaY, int), "The y value given is not an integer."
        self.moveTo(self.x + deltaX, self.y + deltaY)
