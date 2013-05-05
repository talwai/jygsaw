# loop_direct.py
#
# Jygsaw demo - Loops and draws a moving line.
#
# Attribution: Inspired by the loop demo in Processing
# from http://processingjs.org/learning/basic/keyboardfunctions/
# written by Casey Reas and Ben Fry.

from jygsaw.graphics import *

y = 100

canvas(640, 360)      # Size should be the first statement
stroke(255)           # Set stroke color to WHITE
running = False

y = int(height() * 0.5)


def mouse_pressed():
    global running
    running = True

on_mouse_press(mouse_pressed)

background(BLACK)
line(0, y, width(), y)

while True:
    clear()
    line(0, y, width(), y)

    if running:
        line(0, y, width(), y)

        y = y - 1
        if (y < 0):
            y = height()

    refresh(0.05)
