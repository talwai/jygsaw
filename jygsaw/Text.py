from GraphicsObject import *
from java.awt import Font
from java.awt.Font import *
from java.awt.Graphics import setFont


class Text(GraphicsObject):

    def __init__(self, x, y, s, font, size, attribute=PLAIN, color=None):
        assert size > 0, "Text size must be greater than zero"
        super(Text, self).__init__(x, y, color)
        self._s = s
        self._font = font  # Font, however it's defined in Java...
        self._size = size
        self.attribute = attribute  # bold, italic, underline

    def _get_string(self):
        return self._s

    def _set_string(self, s):
        self._s = s

    s = property(_get_string, _set_string)

    def _get_size(self):
        return self._size

    def _set_size(self, s):
        assert _size > 0, "Text size must be greater than zero"
        self._size = s

    size = property(_get_size, _set_size)

    def _get_attribute(self):
        return self._attribute

    def _set_attribute(self, a):
        self._attribute = a

    attribute = property(_get_attribute, _set_attribute)

    def _get_font(self):
        return self._font

    def _set_font(self, f):
        self._font = f

    font = property(_get_font, _set_font)

    def _draw(self, g):
        g.setColor(self.color)
        g.setFont(Font(self.font, self.attribute, self.size))
        g.drawString(self.s, self.x, self.y)
