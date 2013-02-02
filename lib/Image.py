from java.awt import Image
from javax.imageio import *
from java.net import URL
from java.io import File
from GraphicsObject import *

class Image(GraphicsObject):
    def __init__(self, (x, y), url, width, height):
        assert width > 0, "Image width must be greater than zero"
        assert height > 0, "Image height must be greater than zero"
        super(Image, self).__init__((x,y))

        self.url = url
        self.width = width
        self.height = height
    
    def setUrl(self, u):
        self.url = u
    
    def setWidth(self, w):
        assert w > 0, "Image width must be greater than zero"
        self.width = w
    
    def setHeight(self, h):
        assert h > 0, "Image height must be greater than zero"
        self.Height = h
    
    def getUrl(self):
        return self.url
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def _draw(self, g):
        #Need to check whether it is a file or a url -- Carla will work on this later
        img = ImageIO.read(File(self.url))
        #File(self.url)
        #URL(self.url)
        g.drawImage(img, self.coordinates[0], self.coordinates[1], None)
        w = img.getWidth(None);
        h = img.getHeight(None);