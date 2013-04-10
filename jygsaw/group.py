"""
A Group is a convenient way to manage a group of GraphicsObjects.
"""
from graphicsobject import *
from shape import Shape


class Group():

    """
    A Group object  will hold a list of shapes, text, images and other objects, that are grouped together for convenience.
    """


    def __init__(self, *objects):
        """Create a Group object, containing a variable number of objects."""
        self.group = []
        for o in objects:
            assert (isinstance(o, Shape) or isinstance(o,
                    GraphicsObject)), "%s is not Shape " % o
            self.group.append(o)

    def __len__(self):
        return len(self.group)

    def remove(self, *objects):
        """Removes all specified objects from the :py:class:`~jygsaw.group.Group` """
        for o in objects:
            self.group.remove(o)

    def append(self, *objects):
        """Appends all specified objects to the :py:class:`~jygsaw.group.Group` ."""
        for o in objects:
            assert (isinstance(o, Shape) or isinstance(o,
                    GraphicsObject)), "%s is not Shape" % o
            self.group.append(o)

    def move(self, deltaX, deltaY):
        """Moves all objects in the :py:class:`~jygsaw.group.Group` by calling :py:meth:`jygsaw.graphics.move` on each element within it. """
        for o in self.group:
            o.move(deltaX, deltaY)
