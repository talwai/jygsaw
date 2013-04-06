"""
TestShapeColors.py contains end-to-end tests for setting stroke and fill
booleans and colors for all shapes.
"""

from __future__ import with_statement

from jygsaw.graphics import *

import unittest2
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

    def test_fill(self):
        fill(green)
        self.shape = self.create_shape()
        self.assertEqual(self.c.frame.contentPane.defaultColor, green,
                         msg="Changed fill color not reflected in Window")
        self.assertEqual(
            self.shape.color, self.c.frame.contentPane.defaultColor, msg="Changed fill color not reflected in shape")

        # pass in non valid inputs
        with self.assertRaises(Exception):
            fill("fdasdfsa")

    def test_noFill(self):
        noFill()
        stroke()
        self.shape = self.create_shape()
        self.assertEqual(
            self.shape.filled, False, msg="Shape's fill bool not correct")
        self.assertEqual(self.c.frame.contentPane.filled, False,
                         msg="Windows fill bool not set correctly")

    def test_stroke(self):
        stroke(red)
        self.shape = self.create_shape()
        self.assertEqual(self.shape.stroke, self.c.frame.contentPane.stroke,
                         msg="New shape's stroke color  doesn't match have stroke color of window")
        self.assertEqual(self.shape.stroke, True,
                         msg="New shape doesn't have stroke turned on")
        self.assertEqual(self.shape.strokeColor, red,
                         msg="New shape doesn't have right stroke color")

        # pass in non valid inputs
        with self.assertRaises(Exception):
            stroke("FDsafdsa")

    def test_noStroke(self):
        fill()
        noStroke()
        self.shape = self.create_shape()
        self.assertFalse(
            self.shape.stroke, msg="new shape doesn't have stroke turned off")
        self.assertFalse(
            self.shape.stroke, msg="Window doesn't have stroke turned off")

#     def test_noStrokeAndnoFill_RaiseWarning(self):
#          noStroke()
#          noFill()
#          self.assertRaises(UserWarning, self.create_shape)


class TestPoint(BaseShapeClassTests, unittest2.TestCase):
    def create_shape(self):
        return point(100, 100)


class TestLine(BaseShapeClassTests, unittest2.TestCase):
    def create_shape(self):
        return line(0, 0, 100, 100)


class TestRect(BaseShapeClassTests, unittest2.TestCase):
    def create_shape(self):
        return rect(10, 10, 30, 30)


class TestCircle(BaseShapeClassTests, unittest2.TestCase):
    def create_shape(self):
        return circle(20, 20, 30)


class TestEllipse(BaseShapeClassTests, unittest2.TestCase):
    def create_shape(self):
        return ellipse(20, 20, 30, 30)


class TestPolygon(BaseShapeClassTests, unittest2.TestCase):
    def create_shape(self):
        return polygon([(18, 18), (18, 360), (81, 360)])


class TestRegPolygon(BaseShapeClassTests, unittest2.TestCase):
    def create_shape(self):
        return regPolygon(10, 10, 5, 20)


class TestArc(BaseShapeClassTests, unittest2.TestCase):
    def create_shape(self):
        return arc(20, 20, 30, 30, 0, 90)


###### This does not inherit from tthe BaseShapeClass class!!!
class TestBackground(unittest2.TestCase):
    # this fails. why?
    def test_background(self):
        self.c = canvas()
        background(blue)
        self.assertEqual(self.c.frame.contentPane.backgroundColor, blue)

        # pass in non valid inputs
        with self.assertRaises(Exception):
            background("Fdsafdas")

if __name__ == '__main__':
    unittest2.main()
