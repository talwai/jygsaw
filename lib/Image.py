from __future__ import with_statement
from GraphicsObject import *
from java.awt import Image
from javax.imageio import *
from java.io import File
from java.net import URL
import urllib2

class Image(GraphicsObject):
    def __init__(self, (x, y), path, width = None, height = None):
        super(Image, self).__init__((x,y))
        
        # Stores a boolean describing whether or not the path given is a
        # url or file path. Throws an exception if it isn't either
        self.url = self.check_valid_url(path)
        
        self.path = path # path can be either a url or a file path
        self.width = width
        self.height = height


    def check_valid_url(self, path):
        '''
        This function checks to see if the path given is a url or a file path. 
        Returns True if it is a url and False if it is a file path. Throws an
        exception if it is neither or if the paths are incorrect.
        '''
        
        request = urllib2.Request(path)
        request.get_method = lambda : 'HEAD'
        try:
            response = urllib2.urlopen(request)
            return True
        except Exception:
            try:
                with open(path) as f: pass
                return False
            except Exception:
                print "Error could not find image"


    def setPath(self, p):
        self.url = self.check_valid_url(path)
        self.path = p
    
    def setWidth(self, w):
        assert w > 0, "Image width must be greater than zero"
        self.width = w
    
    def setHeight(self, h):
        assert h > 0, "Image height must be greater than zero"
        self.Height = h
    
    def getPath(self):
        return self.path
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def _draw(self, g):
        '''
        Depending on what type of path is given this function will call 
        the appropriate methods to create and ImageIo object. If the width
        and height was not set by the user the size of the image will be 
        used as a default.
        '''

        img = None
        if self.url:
            img = ImageIO.read(URL(self.path))
        else:
            img = ImageIO.read(File(self.path))
            
        if self.width == None:
            self.width = img.getWidth()
        if self.height == None:
            self.height = img.getHeight()

        g.drawImage(img, self.coordinates[0], self.coordinates[1], self.width, self.height, g.backgroundColor, None)
