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
        self.circle = circle(20, 20, 15)

        self.polygon = polygon(
            [(250, 250), (250, 370), (360, 340), (360, 250)])
        self.regPolygon = regPolygon(10, 300, 40, 40)

    def test_arc(self):
        self.assertEqual(self.arc._get_color(), color(128, 128, 128))

        fill(0, 255, 0)
        self.arc = arc(300, 100, 123, 33, 34, 33)

        self.assertEqual(self.arc._get_color(), green)

        self.assertEqual(self.arc._get_x(), 300)
        self.assertEqual(self.arc._get_y(), 100)

        self.arc._set_x(130)
        self.assertEqual(self.arc._get_x(), 130)

        self.arc._set_y(170)
        self.assertEqual(self.arc._get_y(), 170)

        c = color(255, 255, 255)

        self.arc._set_color(c)
        self.assertEqual(self.arc._get_color(), c)

        self.arc.moveTo(1500, 1500)
        self.assertEqual(self.arc._get_x(), 1500)
        self.assertEqual(self.arc._get_y(), 1500)

        self.arc.move(-1600, -1600)
        self.assertEqual(self.arc._get_x(), -100)
        self.assertEqual(self.arc._get_y(), -100)

    def test_polygon(self):
        self.assertEqual(self.polygon._get_vertices(),
                         [(250, 250), (250, 370), (360, 340), (360, 250)])
        self.polygon.moveTo(240, 240)
        self.assertEquals(self.polygon._get_vertices(),
                          [(240, 240), (240, 360), (350, 330), (350, 240)])
        self.assertEqual(self.polygon._get_x(), 240)

        self.polygon.move(350, 350)
        self.assertEqual(self.polygon._get_y(), 590)

    def test_circle(self):
        self.assertEqual(self.circle._get_x(), 20)


if (__name__ == '__main__') or (__name__ == 'main'):
    unittest.main()
