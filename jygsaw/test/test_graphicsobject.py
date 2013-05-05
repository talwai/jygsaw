from jygsaw.graphics import *
import unittest


class TestShapeFunctions(unittest.TestCase):

    def setUp(self):
        canvas()
        stroke()
        frame_rate(60.0)

        self.arc = arc(300, 100, 123, 33, 34, 33)
        self.ellipse = ellipse(10, 150, 40, 40)
        self.circle = circle(20, 20, 15)

        self.polygon = polygon(
            [(250, 250), (250, 370), (360, 340), (360, 250)])
        self.reg_polygon = reg_polygon(10, 300, 40, 40)

    def test_arc(self):
        self.assertEqual(self.arc.color, color(128, 128, 128))

        fill(0, 255, 0)
        self.arc = arc(300, 100, 123, 33, 34, 33)

        self.assertEqual(self.arc.color, GREEN)

        self.assertEqual(self.arc.x, 300)
        self.assertEqual(self.arc.y, 100)

        self.arc.x = 130
        self.assertEqual(self.arc.x, 130)

        self.arc.y = 170
        self.assertEqual(self.arc.y, 170)

        c = color(255, 255, 255)

        self.circle.move_to(1500, 1500)

        self.arc._set_color(c)
        self.assertEqual(self.arc.color, c)

        self.arc.move_to(1500, 1500)
        self.assertEqual(self.arc.x, 1500)
        self.assertEqual(self.arc.y, 1500)

        self.arc.move(-1600, -1600)
        self.assertEqual(self.arc.x, -100)
        self.assertEqual(self.arc.y, -100)

    def test_polygon(self):
        self.assertEqual(self.polygon._get_vertices(),
                         [(250, 250), (250, 370), (360, 340), (360, 250)])
        self.polygon.move_to(240, 240)
        self.assertEquals(self.polygon._get_vertices(),
                          [(240, 240), (240, 360), (350, 330), (350, 240)])
        self.assertEqual(self.polygon.x, 240)

        self.polygon.move(350, 350)
        self.assertEqual(self.polygon.y, 240)

    def test_circle(self):
        self.assertEqual(self.circle.x, 20)
        self.assertEqual(self.circle.y, 20)

        self.circle.x = 40
        self.circle.y = 40

        self.assertEqual(self.circle.x, 40)
        self.assertEqual(self.circle.y, 40)

if (__name__ == '__main__') or (__name__ == 'main'):
    unittest.main()
