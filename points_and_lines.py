# Basic points and lines demo

from GraphicsWrapper import *

d = 70
p1 = d
p2 = p1 + d
p3 = p2 + d
p4 = p3 + d

openCanvas(640, 360)
setBackground(0, 0, 0)

# Draw gray box
setStroke(125)
drawLine(p3, p3, p2, p3)
drawLine(p2, p3, p2, p2)
drawLine(p2, p2, p3, p2)
drawLine(p3, p2, p3, p3)

# Draw white points
setStroke(white)
drawPoint(p1, p1)
drawPoint(p1, p3)
drawPoint(p2, p4)
drawPoint(p3, p1)
drawPoint(p4, p2)
drawPoint(p4, p4)
