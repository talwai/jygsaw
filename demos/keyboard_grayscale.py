# keyboard_grayscale.py
#
# Jygsaw demo - prints columns of gray  from keyboard presses
# 
# Attribution: inspired by the keyboard demo in Processing 
# from http://processingjs.org/learning/basic/keyboard/
# written by Casey Reas and Ben Fry.

from jygsaw.graphics import *
from random import random

canvas(640, 360)
noStroke()
background(0)
rectWidth = width() / 4


def draw():
    # Keep draw to continue looping while waiting for keys.
    # I don't know why this is necessary, but doesn't work without it.
    # Processing also has it in - JL
    pass


def keyPressed():
    keyIndex = -1
    if lastKeyCode() >= ord('A') and lastKeyCode() <= ord('Z'):
        keyIndex = lastKeyCode() - ord('A')
    elif lastKeyCode() >= ord('a') and lastKeyCode() <= ord('z'):
        keyIndex = lastKeyCode() - ord('a')

    if keyIndex == -1:
        # If it's not a letter key, clear the screen
        clear()
    else:
        # It's a letter key, fill a rectangle
        fill(int(random() * 255))
        x = int(float(keyIndex) / 26.0 * float(width() - rectWidth))
        rect(x, 0, rectWidth, height())

onKeyPress(keyPressed)
onDraw(draw)
jygsawMain(0.05)
