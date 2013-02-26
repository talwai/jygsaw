from jygsaw.graphics import *


canvas()
stroke()

rectX = 150
rectY = 30

while True:
    clear()
    vertices = [(250, 250), (250, 370), (360, 340), (360, 250)]

    fill(red)
    stroke(blue)
    rect(rectX, rectY, 100, 100)
    line(150, 10, 200, 10)
    fill(pink)
    ellipse(10, 150, 100, 100)

    polygon(vertices)
    regPolygon(10, 300, 5, 20)
    arc(300, 100, 100, 100, 0, 170)
    circle(0, 0, 100)

    background(white)
    w = width()
    h = height()

    if rectX >= w:
        directionX = -1
    elif rectX < -10:
        directionX = 1

    rectX = rectX + directionX

    if rectY >= h:
        directionY = -1
    elif rectY < -10:
        directionY = 1

    rectY = rectY + directionY

    text((200, 200), 'Hello, world', 'Times New Roman', 50, black)

    redraw(.01)
