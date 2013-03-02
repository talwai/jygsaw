from jygsaw.graphics import *

import unittest


class TestShapeFunctions(unittest.TestCase):

    def setUp(self):
        canvas()
        loop()
        stroke()
        frameRate(60.0)

        self.arc = arc(300, 100, 123, 33, 34, 33)

        self.ellipse = ellipse(10, 150, 40, 40)

        self.polygon = polygon(
            [(250, 250), (250, 370), (360, 340), (360, 250)])
        self.regPolygon = regPolygon(10, 300, 40, 40)

    def test_arc(self):
        self.assertEqual(self.arc._get_color(), color(128, 128, 128))

        fill(0, 255, 0)
        self.arc = arc(300, 100, 123, 33, 34, 33)

        self.assertEqual(self.arc._get_filled(), True)
        self.assertEqual(self.arc._color, green)

        self.assertEqual(self.arc._get_color(), green)

        self.assertEqual(self.arc._get_width(), 123)
        self.assertEqual(self.arc._get_height(), 33)

        self.arc._set_width(130)
        self.assertEqual(self.arc._get_width(), 130)

        self.arc._set_height(170)
        self.assertEqual(self.arc._get_height(), 170)

    def test_polygon(self):
        self.assertEqual(self.polygon._get_vertices(), [(250, 250), (250,
                         370), (360, 340), (360, 250)])

    def test_regpolygon(self):
        self.assertEqual(self.regPolygon.sides,40)
        self.regPolygon.sides = 30

        self.assertEqual(self.regPolygon.sides,30)


        self.regPolygon.sideLength = 20
        self.assertEqual(self.regPolygon.sideLength,20)

if (__name__ == '__main__') or (__name__ == 'main'):
    unittest.main()
