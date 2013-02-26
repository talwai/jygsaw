# """This file test_image.py contains unit tests for image.py"""
from __future__ import with_statement

from jygsaw.graphics import *
 
import unittest

class TestImage(unittest.TestCase):
    def setUp(self):
        self.invalid_path = "./invalid_test_puppy.jpg"
        self.valid_path = "./test_puppy.jpg"
        self.invalid_url = "http://invalidurl.zzzzzzz/comics/steroids.png"
        self.valid_url = "http://imgs.xkcd.com/comics/steroids.png"

        self.c = canvas()
        self.i = image(200, 200, self.valid_path)

    def test_check_valid_url_validPathReturnsFalse(self):
        self.assertFalse(self.i.check_valid_url(self.valid_path))

    def test_check_valid_url_invalidPathReturnsFalseThrowsException(self):
        self.assertRaises(Exception, self.i.check_valid_url(self.valid_path))
        self.assertFalse(self.i.check_valid_url(self.valid_path))
        
    def test_check_valid_url_validURLReturnsTrue(self):
        self.assertTrue(self.i.check_valid_url(self.valid_url))

    def test_check_valid_url_invalidURLReturnsTrueThrowsException(self):
        self.assertRaises(Exception, self.i.check_valid_url(self.invalid_url))
        self.assertFalse(self.i.check_valid_url(self.invalid_url))


    def test_get_path_returnsPath(self):
        self.assertEqual(self.i.path, self.valid_path)

    def test_set_path_setsPathReturnsNewPath(self):
        self.i.path = self.invalid_path
        self.assertEqual(self.i.path, self.invalid_path)
        
    def test_get_width_returnsPath(self):
        self.assertEqual(self.i.width, None)
            
    def test_set_width_setsWidthReturnsNewWidth(self):
        self.i.width = 100
        self.assertEqual(self.i.width, 100)
        
    def test_get_height_returnsHeight(self):
        self.assertEqual(self.i.height, None)

    def test_set_height_setsHeightReturnsNewPath(self):
        self.i.height = 200
        self.assertEqual(self.i.height, 200)

#     def test_draw(self):
#         pass

if __name__ == '__main__':
    pass
    unittest.main()
