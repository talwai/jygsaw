# keyboard_grayscale_direct.py
#
# Jygsaw demo - prints columns of GRAY  from keyboard presses
#
# Attribution: inspired by the keyboard demo in Processing
# from http://processingjs.org/learning/basic/keyboard/
# written by Casey Reas and Ben Fry.

from jygsaw.graphics import *
from random import random

canvas(640, 360)
no_stroke()
background(0)
RECT_WIDTH = width() / 4


def key_pressed():
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
        x = int(float(key_index) / 26.0 * float(width() - RECT_WIDTH))
        rect(x, 0, RECT_WIDTH, height())

on_key_press(key_pressed)

while True:
    refresh(0.05)
