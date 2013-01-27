# Basic shapes demo

from GraphicsWrapper import *

openCanvas(640, 360)
setBackground(0)
noStroke()

setFill(204)
drawTriangle(18, 18, 18, 360, 81, 360)

setFill(102)
drawRect(81, 81, 63, 63)

setFill(204)
drawPolygon(189, 18, 216, 18, 216, 360, 144, 360)

setFill(255)
drawEllipse(252, 144, 72, 72)

setFill(204)
drawTriangle(288, 18, 351, 360, 288, 360)

setFill(255)
drawArc(479, 300, 280, 280, 180, 360)
