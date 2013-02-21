from graphics import *
from GraphicsWindow import *
from GraphicsObject import *

import unittest

class TestShapeFunctions(unittest.TestCase):
	
	def setUp(self):
		canvas()
		loop()
		stroke()
		frameRate(60.0)

		self.arc = arc(300,100)
		self.ellipse = ellipse(10,150)

		self.polygon = polygon([(250,250),(250,370),(360,340),(360,250)])
		self.regPolygon = regPolygon(10,300)

	def test_arc(self):
		self.assertEqual(self.arc._get_x(),300)
		self.assertEqual(self.arc._get_y(),100)
		
		self.arc._set_x(130)
		self.assertEqual(self.arc._get_x(),130)

		self.arc._set_y(170)
		self.assertEqual(self.arc._get_y(),170)

		print self.arc._get_color()
	
	def test_ellipse(self):
		self.assertEqual(self.ellipse._get_x(),10)
		self.assertEqual(self.ellipse._get_y(),150)
	
	def test_polygon(self):
		self.assertEqual(self.polygon.vertices,[(250,250),(250,370),(360,340),(360,250)])
	
	def test_regPolygon(self):
		self.assertEqual(self.regPolygon._get_x(),10)
		self.assertEqual(self.regPolygon._get_y(),300)

if (__name__ == '__main__') or (__name__ == 'main'):
	unittest.main()


