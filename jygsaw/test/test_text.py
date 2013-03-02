# """This file test_image.py contains unit tests for image.py"""
from __future__ import with_statement

from jygsaw.graphics import *

import unittest2


class TestTextClass(unittest2.TestCase):
    def setUp(self):
        self.c = canvas()
        loop()

        self.string = "Sample string"
        self.text = text(0, 0, self.string)
        
    def test_string_attribute(self):
        self.assertEqual(self.text.s, self.string, msg="Default string in text object not correct")

        self.newString = "New string"
        self.text.s = self.newString
        
        self.assertEqual(self.text.s, self.newString, msg="Was not able to change string in text object")
        
        # pass in a non-string object
        with self.assertRaises(Exception):
            self.text.s = 432

    def test_size_attribute(self):
        self.assertEqual(self.text.size, 12, msg="Default size in text object not correct")

        self.newSize = 20
        self.text.size = self.newSize
        
        self.assertEqual(self.text.size, self.newSize, msg="Was not able to change size in text object correctly")
        
        # pass in an invalid text size
        with self.assertRaises(Exception):
            self.text.size = -100
        
        # check passing in non-int throws exception
        with self.assertRaises(Exception):
            self.text.size = "ads"

    def test_attributes_attribute(self):
        self.assertEqual(self.text.attribute, PLAIN, msg="Default attribute in text object not correct")

        self.newAttribute = BOLD
        self.text.attribute = self.newAttribute
        
        self.assertEqual(self.text.attribute, self.newAttribute, msg="Was not able to change attribute in text object")
        
        # pass in a non-attribute object
        with self.assertRaises(Exception):
            self.text.attribute = 432

    def test_font_attribute(self):
        self.assertEqual(self.text.font, 'Times New Roman', msg="Default font in text object not correct")

        self.newFont = 'Times'
        self.text.font = self.newFont
        
        self.assertEqual(self.text.font, self.newFont, msg="Was not able to change font in text object")
        
        # pass in a non font input
        with self.assertRaises(Exception):
            self.text.font = 432

        with self.assertRaises(Exception):
            self.text.font = 'INVALID TEXT FONT'

if __name__ == '__main__':
    unittest2.main()
