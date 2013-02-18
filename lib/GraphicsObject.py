from java.awt.geom import AffineTransform


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
        self._x = x
        self._y = y
        self._color = c
        self.transform = AffineTransform()

    def _get_x(self):
        """Returns the x coordinate value."""
        return self._x

    def _set_x(self, i):
        """Sets the x coordinate value."""
        self._x = i

    x = property(_get_x, _set_x, doc="x coordinate")

    def _get_y(self):
        """Returns the y coordinate value."""
        return self._y

    def _set_y(self, i):
        """Sets the y coordinate value."""
        self._y = i

    y = property(_get_y, _set_y, doc="y coordinate")

    def _get_color(self):
        """Returns the color object"""
        return self._color

    def _set_color(self, c):
        """Sets the color object"""
        self._color = c

    color = property(_get_color, _set_color, doc="color of object")

    def moveTo(self, x, y):
        """ The object is moved to the given coordinates. """
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """ The object's change in x and y are added to its coordinates """
        self.moveTo(self.x + deltaX, self.y + deltaY)

    # Use degrees, not radians
    def rotate(self, degrees):
        pass

    # Flip object on horizontal axis (mirror image)
    def flipX(self):
        # self.transform.scale(1.0, -1.0)
        # (x, y) = self.coordinates
        # self.coordinates = (x, -1.0 * y)
        pass

    # Flip object on vertical axis
    def flipY(self):
        pass

    def scale(self):
        pass
