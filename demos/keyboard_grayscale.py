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
no_stroke()
background(0)
rect_width = width() / 4


def draw():
    pass


def keypressed():
    key_index = -1
    if last_key_code() >= ord('A') and last_key_code() <= ord('Z'):
        key_index = last_key_code() - ord('A')
    elif last_key_code() >= ord('a') and last_key_code() <= ord('z'):
        key_index = last_key_code() - ord('a')

    if key_index == -1:
        # If it's not a letter key, clear the screen
        clear()
    else:
        # It's a letter key, fill a rectangle
        fill(int(random() * 255))
        x = int(float(key_index) / 26.0 * float(width() - rect_width))
        rect(x, 0, rect_width, height())

on_key_press(keypressed)
on_draw(draw)
jygsaw_start(0.05)
