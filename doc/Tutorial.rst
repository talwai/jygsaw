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



You should now have something that looks like this::

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

Awesome! Now let's draw some points and lines.

^^^^^^^^^^^^^^
Points & Lines
^^^^^^^^^^^^^^


Here is another demo::

    from jygsaw import *

    canvas(900,500)
    background(darkGray)

    #   def point(x, y, color=None):

    def draw():
        lineX = random()*800 +50
        lineY = random()*300 +125
        lineColor = choice([lightGray,white,orange, gray])
        line(width()/2,height(),lineX,lineY,color=lineColor)
        point(lineX, lineY -100, color=lineColor)
        loop()

    onDraw(draw)

