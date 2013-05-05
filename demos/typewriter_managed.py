# typewriter_managed.py
#
# Jygsaw demo - Implements a typewriter with Jygsaw
#
# Attribution: inspired by the words demo in Processing
# from http://processingjs.org/learning/basic/words/
# written by Casey Reas and Ben Fry

from jygsaw.graphics import *

canvas(750, 360)
background(DARK_GRAY)
line_height = 60
TEXT_HEIGHT = 30
words = ""
text_list = []


def draw():
    global line_height, TEXT_HEIGHT, words
    clear()

    font("Georgia")
    t = text(25, 25, "Type onto the screen:", color=GRAY)

    font("Arial")
    for (i, h) in text_list:
        text(25, h, i, color=WHITE)

    text(25, line_height, words, color=WHITE)

def keypressed():
    global words, text_list, line_height, TEXT_HEIGHT
    k = last_key_char()
    c = last_key_code()
    if (c != 10 and c != 16):  # as long as the key pressed is not a return or shift
        words += k
    elif c == 10:  # else if the key pressed is a return
        new_line = words
        words = ""
        text_list.append((new_line, line_height))
        line_height += TEXT_HEIGHT  # lower the current line by TEXT_HEIGHT

on_key_press(keypressed)
on_draw(draw)

text_size(TEXT_HEIGHT)

jygsaw_start(0.01)
