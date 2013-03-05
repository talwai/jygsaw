"""
Provides methods and attributes for a text object which
will be drawn on a GraphicsWindow.

Exports Text.
"""

from graphicsobject import *
from java.awt import Font
from java.awt.Font import *
from java.awt.Graphics import setFont



class Text(GraphicsObject):
    """
    Text draws a string on the window. Its arguments are x and y coordinates which
    represent the upper left-hand corner of where the string should begin, a String
    that represents the words to be drawn on the window, a color and an attribute.
    Attributes can be PLAIN, BOLD or ITALIC, by default the attribute is PLAIN.
    """
    attributes = [PLAIN, BOLD, ITALIC]

    def __init__(self, x, y, s, color=None, attribute=PLAIN):
        super(Text, self).__init__(x, y, color)
        assert attribute in self.attributes, "Attribute must be PLAIN, BOLD or ITALIC"
        self._s = s
        self._font = 'Times New Roman'  # Font, however it's defined in Java...
        self._size = 12
        self._attribute = attribute  # PLAIN, BOLD, ITALIC

    def _get_string(self):
        return self._s

    def _set_string(self, s):
        assert isinstance(s, str), "The varible passed is not a string."
        self._s = s

    s = property(
        _get_string, _set_string, "String that is to be drawn on the window.")

    def _get_size(self):
        return self._size

    def _set_size(self, s):
        assert isinstance(s, int) and s > 0, "Text size must be greater than zero."
        self._size = s

    size = property(_get_size, _set_size, "Size of the text.")

    def _get_attribute(self):
        return self._attribute

    def _set_attribute(self, a):
        assert a in self.attributes, "Attribute must be PLAIN, BOLD or ITALIC"
        self._attribute = a

    attribute = property(_get_attribute, _set_attribute,
                         "Attribute of the text (PLAIN, BOLD, ITALIC)")

    def _get_font(self):
        return self._font

    def _set_font(self, f):
        assert isinstance(f, str), "The varible passed is not a string."
        self._font = f

    font = property(_get_font, _set_font,
                    "Font that strings are being drawn in, ex. \'TIMES NEW ROMAN\'")

    def _draw(self, g):
        g.setColor(self.color)
        g.setFont(Font(self.font, self.attribute, self.size))
        g.drawString(self.s, self.x, self.y)
