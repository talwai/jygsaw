from jygsaw.graphics import *
from jygsaw.graphicsobject import *
from jygsaw.graphicswindow import *
import unittest


class TestGroup(unittest.TestCase):
    def setUp(self):
        canvas()
        loop()
        stroke()
        frameRate(60.0)
        self.polygon = polygon([(25, 25), (250, 370), (360, 340), (360, 250)])
        self.regPolygon = regPolygon(10, 300, 5, 20)
        self.circle = circle(350, 150, 50, color=red)
        self.group = Group(self.polygon, self.regPolygon)

    def test_len(self):
        self.assertEqual(len(self.group), 2)

    def test_append(self):
        self.group.append(self.circle)
        self.assertEqual(len(self.group), 3)

    def test_remove(self):
        self.group.remove(self.polygon)
        self.assertEqual(len(self.group), 1)

if (__name__ == '__main__') or (__name__ == 'main'):
    unittest.main()
