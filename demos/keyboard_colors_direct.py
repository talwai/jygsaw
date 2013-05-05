# keyboard_colors_direct.py
#
# Jygsaw demo - prints colors  from keyboard presses
#
# Attribution: inspired by the keyboardfunction demo in Processing
# from http://processingjs.org/learning/basic/keyboardfunctions/
# written by Casey Reas and Ben Fry.

from jygsaw.graphics import *

MAX_HEIGHT = 40
MIN_HEIGHT = 20
letter_height = MAX_HEIGHT
LETTER_WIDTH = 20

x = -LETTER_WIDTH
y = 0

newletter = False

num_chars = 26
colors = []

canvas(640, 360)
no_stroke()
background(100)

# Set a color for each key
for i in range(num_chars):
    colors.append(Color.getHSBColor(float(i) / float(num_chars), 1, 1))


def key_pressed():
    # If the key is between 'A' (65) and 'z' (122)
    global letter_height
    if ord(last_key_char()) >= ord('A') and ord(last_key_char()) <= ord('z'):
        key_index = -1
        if ord(last_key_char()) <= ord('Z'):
            key_index = ord(last_key_char()) - ord('A')
            letter_height = MAX_HEIGHT
            fill(colors[key_index])
        else:
            key_index = ord(last_key_char()) - ord('a')
            letter_height = MIN_HEIGHT
            fill(colors[key_index])
    else:
        fill(0)
        letter_height = 10

    global newletter
    newletter = True

    # Update the "letter" position
    global x
    global y
    x = x + LETTER_WIDTH

    # Wrap horizontally
    if x > width() - LETTER_WIDTH:
        x = 0
        y = y + MAX_HEIGHT

    # Wrap vertically
    if y > height() - letter_height:
        y = 0  # Reset y to 0

on_key_press(key_pressed)

while True:
    if newletter is True:
        # Draw the 'letter'
        y_pos = 0
        if letter_height == MAX_HEIGHT:
            y_pos = y
            rect(x, y_pos, LETTER_WIDTH, letter_height)
        else:
            y_pos = y + MIN_HEIGHT
            rect(x, y_pos, LETTER_WIDTH, letter_height)
        newletter = False

    refresh(0.05)
