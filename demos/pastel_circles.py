from jygsaw.graphics import *
from random import randint

canvas()
background(0, 0, 0)

while True:

	x = randint(0, 400)
	y = randint(0, 400)

	r = randint(128, 255)
	g = randint(128, 255)
	b = randint(128, 255)

	fill(r, g, b)

	circle(x, y, 50)

	redraw(.05)
