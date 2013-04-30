# typewriter.py
#
# Jygsaw demo - Implements a typewriter with Jygsaw
#
# Attribution: inspiRED by the words demo in Processing
# from http://processingjs.org/learning/basic/words/
# written by Casey Reas and Ben Fry

from jygsaw.graphics import *

canvas(750, 360)
background(DARK_GRAY)
LINE_HEIGHT = 60
TEXT_HEIGHT = 30
words = ""
text_list = []


def key_pressed():
    global words, text_list, LINE_HEIGHT, TEXT_HEIGHT
    k = last_key_char()
    c = last_key_code()
    if (c != 10 and c != 16):  # as long as the key pressed is not a return or shift
        words += k
    elif c == 10:  # else if the key pressed is a return
        new_line = words
        words = ""
        text_list.append((new_line, LINE_HEIGHT))
        LINE_HEIGHT += TEXT_HEIGHT  # lower the current line by TEXT_HEIGHT

on_key_press(key_pressed)


while True:
    clear()

    t = text(25, 25, "Type onto the screen:", color=GRAY, attribute=PLAIN)
    t.size = TEXT_HEIGHT
    t.font = "Georgia"

    for (i, h) in text_list:
        ti = text(25, h, i, color=WHITE, attribute=PLAIN)
        ti.font = "Arial"
        ti.size = TEXT_HEIGHT

    tw = text(25, LINE_HEIGHT, words, color=WHITE, attribute=PLAIN)
    tw.font = "Arial"
    tw.size = TEXT_HEIGHT
    refresh(0.01)
