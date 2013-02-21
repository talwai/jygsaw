from jygsaw import *

canvas()

#This should already be enabled
#stroke()

rectX = 150
rectY = 30

vertices = [(250, 250), (250, 370), (360, 340), (360, 250)]


background(white)   # hoisted this from the loop

while True:
    clear()

    fill(red)
    stroke(blue)
    # rect(rectX, rectY, filled=True)
    # of course it's filled, I just called fill(red)
    rect(rectX, rectY)

    line(150, 10, 200, 10)
    fill(pink)

    #ellipse(10, 150, filled=True)
    # Ellipse must take four parameters, none default.  Geometry should never
    #  be a default.  But I don't need the filled param.
    ellipse(10, 150, 50, 100)

    #polygon(vertices, filled=False)
    #regPolygon(10, 300, filled=False)
    #arc(300, 100, filled=False)
    #circle(0, 0, filled=False)
    noFill()  # use processing noFill() syntax
    polygon(vertices)
    regPolygon(10, 300)

    # arc and circle should not use default parameters for geometry
    arc(300, 100, 100, 100, 0, 180)
    circle(0, 0, 50)

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

    #text((200, 200), 'Hello, world', 'Times New Roman', 50, black)

    textFont('Times New Roman')
    textSize(50)
    stroke(black)
    text(200, 200, 'Hello, world')

    redraw(.01)
    #sleep(.05)
