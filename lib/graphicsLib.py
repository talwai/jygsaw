# Filename: graphicsLib.py

from GraphicsWindow import *

## Parking lot: class RegPolygon(Polygon):

if ( __name__ == '__main__' ) or ( __name__ == 'main' ) :
    w = GraphicsWindow('Demo Time', 500, 500, black)
    w.setDefaultColor(pink)
    e = Ellipse((100, 100), 35, 35, filled=False)
    r = Rectangle((250, 250), 100, 200, blue)
    w.setDefaultColor(green)
    t = Text((400, 300), "Hello!", "Arial", 40)
    sun = Ellipse((115, 110), 75, 75, yellow)
    l = Line ((5,10),(100,150))
    image = Image((20, 20), "puppy.jpg")
    q = Polygon ([(100,100),(150,250),(200,300)],blue)
    p = RegPolygon((200,200),5,50)
    z = Group (q,p)
    #z.move(100, 100)
    #    z.draw(w)
    w.draw(z)
    #w.draw(t)
    #w.draw(image)
    w.setVisible(True)

    #this is a sample url image that we can use for testing things
    #http://cdn.cutestpaw.com/wp-content/uploads/2011/11/Handsome-l.jpg




# TODO
# implement group.draw() in window class
#
# demo of shape responding to mouse/key events

#End of GraphicsLib.py

#use graphics2d, antialiasing
#animation style:
# 1) cs1lib, 
# 2) while loop


# instance variables should be functions
# i.e. mouseX() instead of mouseX

# setStrokeColor() instead of setStroke()

# all graphics library are non thread-safe
# look up event dispatch thread for swing
# invoke later

# avoiding two threads
# 1) wrap things in invokelater()

