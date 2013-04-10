from jygsaw.graphics import *
from jygsaw.graphicsobject import *
from jygsaw.graphicswindow import *
import unittest


class TestGroup(unittest.TestCase):
    def setUp(self):
        canvas()
        stroke()
        frameRate(60.0)
        self.polygon = polygon([(25, 25), (250, 370), (360, 340), (360, 250)])
        self.regPolygon = regPolygon(10, 300, 5, 20)
        self.circle = circle(350, 150, 50, color=red)
        self.triangle = triangle(10, 10, 5, 5, 6, 1)
        self.triangle_b = triangle(10, 10, 5, 5, 6, 1)
        self.group = Group(self.polygon, self.regPolygon, self.triangle)

    def test_len(self):
        self.assertEqual(len(self.group), 3,
                         msg="len should return size of the group.")

    def test_append(self):
        self.group.append(self.circle)

        self.assertEqual(len(self.group), 4,
                         msg="append should add an object to the group.")

    def test_remove(self):
        self.group.remove(self.polygon)
        self.assertEqual(len(self.group), 2,
                         msg="remove should remove an object from the group.")
        self.assertRaises(ValueError, self.group.remove, self.polygon)

    # def test_move(self):
    #     self.group.append(self.circle)
    #     self.group.remove(self.regPolygon)
    #     #self.group.remove(self.regPolygon)

    #     self.group.move(1, 1)
    #     self.assertEqual(self.polygon.vertices,
    #                      [(26, 26), (251, 371), (361, 341), (361, 251)],
    #                      msg="polygon should move by (+1,+1).")
    #     self.assertEqual(self.circle.x, 351,
    #                      msg="circle should move by (+1,+1).")
    #     self.assertEqual(self.circle.y, 151,
    #                      msg="circle should move by (+1,+1).")

if (__name__ == '__main__') or (__name__ == 'main'):
    unittest.main()
