# Filename: graphicsLib.py
from GraphicsWindow import *
from time import sleep

## Parking lot: class RegPolygon(Polygon):

if (__name__ == '__main__') or (__name__ == 'main'):
    w = GraphicsWindow('Demo Time', 1000, 1000, black)
    w.setDefaultColor(pink)
    w.setStrokeColor(green)
    w.setStroke(True)

    e = Ellipse(400, 400, 300, 300, filled=True)
    w.draw(e)

    w.setStrokeColor(red)
    r = Ellipse(250, 250, 100, 200, blue)

    w.setDefaultColor(green)
    t = Text((400, 300), "Hello!", "Arial", 40)
    sun = Ellipse((115, 110), 75, 75, yellow)
    l = Line((5, 10), (100, 150))
    w.draw(l)
    p = Point((900, 9), black)
    w.draw(p)
    # image = Image((20, 20), "puppy.jpg")
    q = Polygon([(100, 100), (150, 250), (200, 300)], blue)
    p = RegPolygon((200, 200), 5, 50)
    z = Group(q, p, r, e, sun)

    image2 = Image(
        100, 400, "http://cdn.cutestpaw.com/wp-content/uploads/2011/11/Handsome-l.jpg")
    z = Group(r, e, sun)
    z.move(100, 100)
    w.draw(z)
    w.draw(t)
    # w.draw(image)

    w.draw(image2)
    w.setVisible(True)
    w.setBackgroundColor(white)

    # this is a sample url image that we can use for testing things
    # http://cdn.cutestpaw.com/wp-content/uploads/2011/11/Handsome-l.jpg


# End of GraphicsLib.py


# TODO
# implement group.draw() in window class
#
# demo of shape responding to mouse/key events


# use graphics2d, antialiasing
# animation style:
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
