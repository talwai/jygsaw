from java.awt.geom import AffineTransform
from java.awt import Color


class GraphicsObject(object):
    """
    The parent class for all drawn objects (shapes, text, images).

    :param x: x-coordinate.
    :type x: int, optional
    :param y: y-coordinate.
    :type y: int, optional
    :param color: Color of the object.
    :type color: :py:class:`Color`, optional
    """

    def __init__(self, x=0, y=0, c=None):
        super(GraphicsObject, self).__init__()
        assert isinstance(x, int), "The x value given is not an integer."
        assert isinstance(y, int), "The x value given is not an integer."
        assert c is None or isinstance(
            c, Color), "The object passed is not a Color object."
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

    x = property(_get_x, _set_x, doc="x-coordinate of object.")

    def _get_y(self):
        """Returns the y coordinate value."""
        return self._y

    def _set_y(self, i):
        """Sets the y coordinate value."""
        assert isinstance(i, int), "The y value given is not an integer."
        self._y = i

    y = property(_get_y, _set_y, doc="y-coordinate of object.")

    def _get_color(self):
        """Returns the color of the GraphicsObject."""
        return self._color

    def _set_color(self, c):
        """Sets the color of the GraphicsObject."""
        assert c is None or isinstance(
            c, Color), "The object passed is not a Color object."
        self._color = c

    color = property(_get_color, _set_color, doc="Color of the object.")

    def move_to(self, x, y):
        """
        Moves object to a new location.

        :param x: New ``x`` coordinate.
        :type x: int
        :param y: New ``y`` coordinate.
        :type y: int
        """
        assert isinstance(x, int), "The x value given is not an integer."
        assert isinstance(y, int), "The y value given is not an integer."
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        """
        Moves object by the specified amount.

        :param delta_x: Amount by which to move x-coordinate.
        :type delta_x: int
        :param delta_y: Amount by which to move y-coordinate.
        :type delta_y: int
        """
        assert isinstance(delta_x, int), "The x value given is not an integer."
        assert isinstance(delta_y, int), "The y value given is not an integer."
        self.move_to(self.x + delta_x, self.y + delta_y)
