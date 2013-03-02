# """This file test_image.py contains unit tests for image.py"""
from __future__ import with_statement

from jygsaw.graphics import *

import unittest2


class TestImage(unittest2.TestCase):
    def setUp(self):
        self.invalid_path = "./invalid_test_puppy.jpg"
        self.valid_path = "./puppy_for_test_image.jpg"
        self.invalid_url = "http://invalidurl.zzzzzzz/comics/steroids.png"
        self.valid_url = "http://imgs.xkcd.com/comics/steroids.png"

        self.c = canvas()
        self.i = image(200, 200, self.valid_path)

    def test_check_valid_url(self):
        self.assertFalse(self.i.check_valid_url(self.valid_path), msg="Valid File path should return false")

        # Invalid path should thrown an exception
        with self.assertRaises(Exception):
            self.i.check_valid_url(self.invalid_path)

        self.assertTrue(self.i.check_valid_url(self.valid_url), msg="valid URL should return True")

        # Invalid url should throw exception
        with self.assertRaises(Exception):
            self.i.check_valid_url(self.invalid_url)



    def test_path_attribute(self):
        self.assertEqual(self.i.path, self.valid_path, msg="Attribute path is set incorrectly")

        self.i.path = self.invalid_path
        self.assertEqual(self.i.path, self.invalid_path, msg="Was not able to set path instance variable");

    def test_width_attribute(self):
        self.assertEqual(self.i.width, None, "Attribute width should be none")

        self.i.width = 100
        self.assertEqual(self.i.width, 100, msg="Was not able to set attribute width")

        # check invalid inputs throw error
        with self.assertRaises(Exception):
            self.i.width = -100
        
        # check passing in non-int throws exception
        with self.assertRaises(Exception):
            sef.i.witdth = "ads"

    def test_height_attribute(self):
        self.assertEqual(self.i.height, None, msg="Attribute height should be none")

        self.i.height = 200
        self.assertEqual(self.i.height, 200, "was not able to set i.height")

        # check invalid inputs throws exception
        with self.assertRaises(Exception):
            self.i.height = -200

        # check passing in non-int throws exception
        with self.assertRaises(Exception):
            self.i.height = "ads"




if __name__ == '__main__':
    unittest2.main()
