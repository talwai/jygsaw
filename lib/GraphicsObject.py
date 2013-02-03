from java.awt.geom import AffineTransform

class GraphicsObject(object):
    """
        Anything drawn on the canvas is a child of GraphicsObject.
        This class stores the location of the object (x, y) and
        has methods to rotate, flip, translate and move the object.        
    """
    
    def __init__(self, (x, y) = (0, 0), color = None):
        super(GraphicsObject, self).__init__()
        self.coordinates = (x, y) # (x,y) tuple of object's position
        self.color = color
        self.transform = AffineTransform()

    # Use degrees, not radians
    def rotate(self, degrees):
        pass
    
    def moveTo(self, x, y):
        self.coordinates = (x, y)
    #redraw?
    
    def move(self, deltaX, deltaY):
        self.moveTo(self.coordinates[0] + deltaX, self.coordinates[1] + deltaY)
    
    # Flip object on horizontal axis (mirror image)
    def flipX(self):
#self.transform.scale(1.0, -1.0)
        (x, y) = self.coordinates
        self.coordinates = (x, -1.0 * y)

    
    # Flip object on vertical axis
    def flipY(self):
        pass
    
    def scale(self):
        pass
    
    def getColor(self):
        return self.color
    
    def getCoordinates(self):
        return self.coordinates
    
    def getX(self):
        return  self.coordinates[0]
    
    def getY(self):
        return  self.coordinates[1]
    
    def setColor(self, c):
        self.color = c
    
    def setCoordinates(self, (x, y)):
        self.coordinates = (x, y)
    
    def setX(self, x):
        self.coordinates[0] = x
    
    def setY(self, y):
        self.coordinates[1] = y
