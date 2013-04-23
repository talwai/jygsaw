"""
Provides methods and attributes for an Image objectto be
drawn on a GraphicsWindow.

Exports Image.
"""

from __future__ import with_statement
from graphicsobject import *
from javax.imageio import *
from java.io import File
from java.net import URL
import urllib2


class Image(GraphicsObject):

    """
    Displays an image on the window at the given x and y values. The x and y
    coordinates represent the upper left hand corner of where the image should
    be drawn on the window. The user can specify a path that is either to an
    image in their machine or an html link. The class itself differentiates
    between the two. The user can specify the width and height of the image.
    If none is provided, the width and height of the actual image is used.
    """

    def __init__(self, x, y, path, width=None, height=None):
        super(Image, self).__init__(x, y)
        assert (isinstance(width, int) and width >
                0) or width == None, "Image width must be greater than zero"
        assert (isinstance(height, int) and height >
                0) or width == None, "Image width must be greater than zero"
        assert isinstance(x, int), "Coordinates must be an int."
        assert isinstance(y, int), "Coordinates must be an int."

        # Stores a boolean describing whether or not the path given is a
        # url or file path. Throws an exception if it isn't either
        self.url = self.check_valid_url(path)
        self._path = path  # path can be either a url or a file path
        self._width = width
        self._height = height

    def check_valid_url(self, path):
        """
        This function checks to see if the path given is a url or a file path.
        Returns True if it is a url and False if it is a file path. Throws an
        exception if it is neither or if the paths are incorrect.
        """

        request = urllib2.Request(path)
        request.get_method = lambda: 'HEAD'
        try:
            response = urllib2.urlopen(request)
            return True
        except Exception:
            try:
                with open(path) as f:
                    pass
                return False
            except Exception:
                raise Exception("Could not find image")

    def _get_path(self):
        return self._path

    def _set_path(self, p):
        self.url = self.check_valid_url(p)
        self._path = p

    path = property(_get_path, _set_path,
                    "A String that describes where the image is located. Can either be a url or a file path.")

    def _get_width(self):
        return self._width

    def _set_width(self, w):
        assert isinstance(
            w, int) and w > 0, "Image width must be greater than zero"
        self._width = w

    width = property(_get_width, _set_width, "Width of the image in pixels.")

    def _get_height(self):
        return self._height

    def _set_height(self, h):
        assert isinstance(
            h, int) and h > 0, "Image height must be greater than zero"
        self._height = h

    height = property(
        _get_height, _set_height, "Height of the image in pixels.")

    def _draw(self, g):
        """
        Depending on what type of path is given this function will call
        the appropriate methods to create an ImageIO object. If the user did
        not set the width and height, the size of the image will be used as a
        default.
        """

        img = None
        if self.url:
            img = ImageIO.read(URL(self.path))
        else:
            img = ImageIO.read(File(self.path))

        if self.width == None:
            self.width = img.getWidth()
        if self.height == None:
            self.height = img.getHeight()

        g.drawImage(img, self.x, self.y,
                    self.width, self.height, g.background_color, None)
