# Basic points and lines demo

from GraphicsWrapper import *

d = 70
p1 = d
p2 = p1 + d
p3 = p2 + d
p4 = p3 + d

canvas(640, 360)
background(0, 0, 0)

# Draw gray box
strokeColor(125)
line(p3, p3, p2, p3)
line(p2, p3, p2, p2)
line(p2, p2, p3, p2)
line(p3, p2, p3, p3)

# Draw white points
strokeColor(white)
point(p1, p1)
ooint(p1, p3)
point(p2, p4)
point(p3, p1)
point(p4, p2)
point(p4, p4)
