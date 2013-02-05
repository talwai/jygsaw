from GraphicsObject import *
from java.awt import Font
from java.awt.Font import *
from java.awt.Graphics import setFont



class Text(GraphicsObject):
    def __init__(self, (x, y), s, font, size, attribute = PLAIN, color = None):
        assert size > 0, "Text size must be greater than zero"
        super(Text, self).__init__((x, y), color)
        self.s = s
        self.font = font # Font, however it's defined in Java...
        self.size = size
        self.attribute = attribute #bold, italic, underline
    
    def getString(self):
        return self.s
    
    def getSize(self):
        return self.size
    
    def getAttribute(self):
        return self.attribute
    
    def getFont(self):
        return self.font
    
    def setString (self, s):
        self.s = s
    
    def setSize(self, s):
        self.size = s
    
    def setAttribute(self, a):
        self.attribute = a
    
    def setFont(self, f):
        self.font = f
    
    def _draw(self, g):
        g.setFont(Font(self.font, self.attribute, self.size))
        g.drawString(self.s, self.coordinates[0], self.coordinates[1])

