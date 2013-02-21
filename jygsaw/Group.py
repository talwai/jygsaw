from GraphicsObject import *


class Group():
    def __init__(self, *objects):
        self.group = []
        for o in objects:
            assert isinstance(
                o, GraphicsObject), "%s is not GraphicsObject" % o
            self.group.append(o)

    # removing and adding objects
    def remove(self, *objects):
        for o in objects:
            self.group.remove(o)

    # append
    def append(self, *objects):
        for o in objects:
            assert isinstance(
                o, GraphicsObject), "%s is not a GraphicsObject" % o
            self.group.append(o)

    # translating
    def move(self, deltaX, deltaY):
        for o in self.group:
            o.move(deltaX, deltaY)

    # rotate all objects on their centers
    def rotateAroundPoint(self, degree):
        for o in self.group:
            o.rotate(degree)
