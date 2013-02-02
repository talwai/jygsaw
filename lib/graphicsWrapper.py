from GraphicsLibrary import *

class GraphicsWrapper():
    window = GraphicsWindow('Empty', 100, 100)
    FillColor = Color.none
    mouseX, mouseY
    toLoop = False

    def canvas(width = 400, height = 400, window_title = ' '):
        global window
        window = GraphicsWindow(window_title, width, height)
        window.setVisible(True)

    def width():
        return window.width

    def height():
        return window.height

    def line((x1, y1), (x2, y2), color=None):
        global FillColor
        if color == None:
            color = FillColor
        new_line = Line(self, (x1, y1), (x2, y2))
        window.draw(new_line)
		return new_line

    def rect((x, y), rectWidth, rectHeight, color=None, filled=True, stroke=False):
        global FillColor
        if color == None:
            color = FillColor
        new_rect = Rectangle(self, (x, y), rectWidth, rectHeight, color, true)
        window.draw(new_rect)
		return new_rect

    def circle((x, y), radius, color=None, filled=True, stroke=False):
        global FillColor
        if color == None:
            color = FillColor
        new_circle = Circle(self, (x, y), radius, FillColor, filled, stroke)
        window.draw(new_circle)
		return new_circle

    def ellipse((x, y), width, height, color=None, filled=True, stroke=False):
        global FillColor
        if color == None:
            color = FillColor
        new_ellipse = Ellipse(self, (x, y), width, height, color, filled)
        window.draw(new_ellipse)
		return new_ellipse

    def polygon (vertices, width, height, color = None, filled = True, stroke = False):
		if color == None:
			color = global FillColor
		new_polygon = Polygon (self, vertices, color, filled, stroke)
		return new_polygon
	
	def arc((x, y), width = 100, height = 100, startAngle = 0, endAngle = 180, color = None, filled = True, stroke = False):
        global FillColor
        if color == None:
            color = FillColor
        new_arc = Arc((x,y), width, height, startAngle, (endAngle - startAngle), color)
        window.draw(new_arc)
        return new_arc

# It would be nice to have the option to not specify the width
# and height. Is there a way to get the default width/height of image?
    def drawImage((x, y), imagePath, width, height):
        global window
        img = Image((x, y), imagePath, width, height)
        window.draw(img)

    def fill(color):
        window.setDefaultColor(color)

    def setBackground(r, g, b):
        global window
        window.contentPane.background = (r, g, b)

    def draw():
        for img in window.objs:
            img._draw(window)


	def mousePressed():
		# Perform some magic
		drawRect((x, y), mouseX, mouseY)

drawFunction(draw)
mousePressedFunction(mousePressed)
