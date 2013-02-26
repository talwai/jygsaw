"""
A Group is a convenient way to manage a group of GraphicsObjects.
"""
from graphicsobject import *


class Group():
    def __init__(self, *objects):
        self.group = []
        for o in objects:
            assert isinstance(
                o, GraphicsObject), "%s is not GraphicsObject" % o
            self.group.append(o)

    def __len__(self):
        return len(self.group)

    def remove(self, *objects):
        """Removes all specified objects from the Group."""
        for o in objects:
            self.group.remove(o)

    def append(self, *objects):
        """Appends all specified objects from the Group."""
        for o in objects:
            assert isinstance(
                o, GraphicsObject), "%s is not a GraphicsObject" % o
            self.group.append(o)

    def move(self, deltaX, deltaY):
        """Moves all objects in the Group."""
        for o in self.group:
            o.move(deltaX, deltaY)
