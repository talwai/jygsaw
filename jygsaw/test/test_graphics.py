"""
TestShapeColors.py contains end-to-end tests for setting stroke and fill
booleans and colors for all shapes.
"""

from __future__ import with_statement

from jygsaw.graphics import *

import unittest
import warnings


# http://stackoverflow.com/questions/3892218/
# how-to-test-with-pythons-unittest-that-a-warning-has-been-
# thrown/3892413#3892413

# class WarningTestMixin(object):
#     'A test which checks if the specified warning was raised'

#     def assertWarns(self, warning, callable, *args, **kwds):
#         with warnings.catch_warnings(record=True) as warning_list:
#             warnings.simplefilter('always')

#             result = callable(*args, **kwds)

# self.assertTrue(any(item.category == warning for item in warning_list))

class BaseShapeClassTests(object):
    def create_shape(self):
        pass

    def setUp(self):
        self.c = canvas()
        loop()

    def test_fill(self):
        fill(green)
        self.shape = self.create_shape()
        self.assertEqual(self.c.frame.contentPane.defaultColor, green)
        self.assertEqual(
            self.shape.color, self.c.frame.contentPane.defaultColor)

    def test_noFill(self):
        noFill()
        stroke()
        self.shape = self.create_shape()
        self.assertEqual(self.shape.filled, False)
        self.assertEqual(self.c.frame.contentPane.filled, False)

    def test_stroke(self):
        stroke(red)
        self.shape = self.create_shape()
        self.assertEqual(self.shape.stroke, self.c.frame.contentPane.stroke)
        self.assertEqual(self.shape.stroke, True)
        self.assertEqual(self.shape.strokeColor, red)

    def test_noStroke(self):
        fill()
        noStroke()
        self.shape = self.create_shape()
        self.assertEqual(self.shape.stroke, False)
        self.assertEqual(self.shape.stroke, self.c.frame.contentPane.stroke)


#     def test_noStrokeAndnoFill_RaiseWarning(self):
#         noStroke()
#         noFill()
#         self.assertRaises(Warning, self.create_shape)

class TestPoint(BaseShapeClassTests, unittest.TestCase):
    def create_shape(self):
        return point(100, 100)


class TestLine(BaseShapeClassTests, unittest.TestCase):
    def create_shape(self):
        return line(0, 0, 100, 100)


class TestRect(BaseShapeClassTests, unittest.TestCase):
    def create_shape(self):
        return rect(10, 10, 30, 30)


class TestCircle(BaseShapeClassTests, unittest.TestCase):
    def create_shape(self):
        return circle(20, 20, 30)


class TestEllipse(BaseShapeClassTests, unittest.TestCase):
    def create_shape(self):
        return ellipse(20, 20, 30, 30)


class TestPolygon(BaseShapeClassTests, unittest.TestCase):
    def create_shape(self):
        return polygon([(18, 18), (18, 360), (81, 360)])


class TestRegPolygon(BaseShapeClassTests, unittest.TestCase):
    def create_shape(self):
        return regPolygon(10, 10, 5, 20)


class TestArc(BaseShapeClassTests, unittest.TestCase):
    def create_shape(self):
        return arc(20, 20, 30, 30, 0, 90)



###### This does not inherit from tthe BaseShapeClass class!!!
class TestBackground(unittest.TestCase):
    # this fails. why?
    def test_background(self):
        background(blue)
        self.c = canvas()
        self.assertEqual(self.c.frame.contentPane.backgroundColor, blue)

if __name__ == '__main__':
    unittest.main()
