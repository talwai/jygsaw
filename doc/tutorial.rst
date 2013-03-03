Tutorial
=========

.. highlight:: python

------------------------------
*Getting started with Jygsaw!*
------------------------------

To get started, first make sure you have properly [installed] the Jygsaw package. If you're having trouble with your installation, check out the [troubleshooting/installation] page.

-----------------------
*Your first program...*
-----------------------
^^^^^^^^^^^^
Basic Shapes
^^^^^^^^^^^^

Open up your editor and start with the import statement::

    from jygsaw import *

Let's set the size of the canvas by inputting a length and width of say, 700 and 400. Since the background is set to a default color gray, let's change it to blue::

    canvas(700,300)
    background(blue)

Let's slap some shapes on the screen. To do this, we'll first need to define a draw function, and then call the callback function onDraw that calls that draw function. The origin (0,0) is located in the top-left corner of the canvas by default::

    def draw():
        circle(350, 150, 50, color=red)
        rect(0,0, 150, 75, color=orange)
        polygon([(450,250),(650,250),(500,300)],color=yellow)
        ellipse(150, 75, 100, 250, color=green)
        regPolygon(550, 85, sides=6, length=80, color=magenta)

    onDraw(draw)


You should now have code like this::

    from jygsaw import *

    canvas(700,300)
    background(blue)

    def draw():
        circle(350, 150, 50, color=red)
        rect(0,0, 150, 75, color=orange)
        polygon([(450,250),(650,250),(500,300)],color=yellow)
        ellipse(150, 75, 100, 250, color=green)
        regPolygon(550, 85, sides=6, length=80, color=magenta)

    onDraw(draw)

That outputs something like this:
    #Can we output the code on the page

Awesome!

^^^^^^^^^^^^^^
Points & Lines
^^^^^^^^^^^^^^

Now let's draw some points and lines::

    from jygsaw import *

    canvas(900,500)
    background(darkGray)

    def draw():
        #width() returns the width of the canvas
        #height() returns the height of the canvas
        lineX = random()*(width()-100) +50
        lineY = random()*(height()-200) +100
        lineColor = choice([lightGray,white,orange, gray])
        line(width()/2,height(),lineX,lineY,color=lineColor)
        point(lineX, lineY -100, color=lineColor)
        loop()

    onDraw(draw)

^^^^^
Text
^^^^^
Let's get text on the screen using keyboard input::

    from jygsaw import *
    canvas(750, 360)
    background(darkGray)
    loop()  # so that draw() loops
    currentLineHeight = 60
    textHeight = 30
    words = ""
    textList = []


    def draw():
        global currentLineHeight, textHeight, words
        clear()

        textSize(textHeight)
        font("Georgia")
        t = text(25, 25, "Type onto the screen:", color=gray)
        font("Arial")
        for (i, h) in textList:
            ti = text(25, h, i, color=white)

        tw = text(25, currentLineHeight, words, color=white)


    def keyPressed():
        global words, textList, currentLineHeight, textHeight
        k = lastKeyChar()
        c = lastKeyCode()
        if (c != 10 and c != 16):  # as long as the key pressed is not a return or shift
            words += k
        elif c == 10:  # else if the key pressed is a return
            newLine = words
            words = ""
            textList.append((newLine, currentLineHeight))
            currentLineHeight += textHeight  # lower the current line by textHeight

    onKeyPress(keyPressed)
    onDraw(draw)

^^^^^^
IMAGES
^^^^^^
Here's how to use images in Jygsaw::

    from jygsaw.graphics import *

    canvas(900, 600)
    background(green)
    offset=25

    def draw():
        image(0,0,"http://s3-ec.buzzfed.com/static/enhanced/terminal05/2012/2/1/16/enhanced-buzz-3821-1328131216-142.jpg", width(), height())

    onDraw(draw)
