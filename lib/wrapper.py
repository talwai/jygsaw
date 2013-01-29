from graphicsLib import *
from time import sleep

window = None



def canvas(width = 400, height = 400, name = "Unclear"):
    global window
    window = GraphicsWindow(name, width, height)
    window.setVisible(True)
    
# how does processing define ellipse params?    
def ellipse(x, y, width, height):
    e = Ellipse((x, y), width, height)
    window.draw(e)
    
def fill(c):
    window.setDefaultColor(pink)

if ( __name__ == '__main__' ) or ( __name__ == 'main') :
    
    canvas()
    fill(pink)
    ellipse(100, 200, 50, 25)

'''
if ( __name__ == '__main__' ) or ( __name__ == 'main' ) :
    
    w = GraphicsWindow('Demo Time', 500, 500)
    w.setDefaultColor(pink)
    e = Ellipse((100, 100), 35, 35)
    r = Rectangle((250, 250), 100, 200, blue)
    w.setDefaultColor(green)
    t = Text((400, 300), "Hello!", "Arial",40)
    sun = Ellipse((115, 110), 75, 75, yellow)
    l = Line ((5,10),(100,150))
    z = Group (r, e, sun)
    z.move(100, 100)
    z.draw(w)
    w.draw(t)
    w.draw(l)
    w.setVisible(True)
'''