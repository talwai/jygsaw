from jygsaw.graphics import *
import unittest


class TestShapeFunctions(unittest.TestCase):

    def setUp(self):
        canvas()
        stroke()
        frame_rate(60.0)

        self.arc = arc(300, 100, 123, 33, 34, 33)

        self.ellipse = ellipse(10, 150, 40, 40)

        self.polygon = polygon(
            [(250, 250), (250, 370), (360, 340), (360, 250)])
        self.reg_polygon = reg_polygon(10, 300, 40, 40)

    def test_arc(self):
        self.assertEqual(self.arc._get_color(), color(128, 128, 128))

        fill(0, 255, 0)
        self.arc = arc(300, 100, 123, 33, 34, 33)

        self.assertEqual(self.arc._get_filled(), True)
        self.assertEqual(self.arc._color, GREEN)

        self.assertEqual(self.arc._get_color(), GREEN)

        self.assertEqual(self.arc.width, 123)
        self.assertEqual(self.arc.height, 33)

        self.arc.width = 130
        self.assertEqual(self.arc.width, 130)

        self.arc.height = 170
        self.assertEqual(self.arc.height, 170)

    def test_polygon(self):
        self.assertEqual(self.polygon._get_vertices(), [(250, 250), (250,
                         370), (360, 340), (360, 250)])

    def test_regpolygon(self):
        self.assertEqual(self.reg_polygon.sides, 40)
        self.reg_polygon.sides = 30

        self.assertEqual(self.reg_polygon.sides, 30)

        self.assertEqual(self.reg_polygon.side_length, 40)

        self.reg_polygon.side_length = 20
        self.assertEqual(self.reg_polygon.side_length, 20)


if (__name__ == '__main__') or (__name__ == 'main'):
    unittest.main()
