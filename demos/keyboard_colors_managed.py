# keyboard_colors.py
#
# Jygsaw demo - prints colors  from keyboard presses
#
# Attribution: inspired by the keyboardfunction demo in Processing
# from http://processingjs.org/learning/basic/keyboardfunctions/
# written by Casey Reas and Ben Fry.#

from jygsaw.graphics import *

max_height = 40
min_height = 20
letter_height = max_height
letter_width = 20

x = -letter_width
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


def draw():
    global newletter
    if newletter is True:
        # Draw the 'letter'
        y_pos = 0
        if letter_height == max_height:
            y_pos = y
            rect(x, y_pos, letter_width, letter_height)
        else:
            y_pos = y + min_height
            rect(x, y_pos, letter_width, letter_height)
        newletter = False


def keyPressed():
    # If the key is between 'A' (65) and 'z' (122)
    global letter_height
    if ord(last_key_char()) >= ord('A') and ord(last_key_char()) <= ord('z'):
        keyIndex = -1
        if ord(last_key_char()) <= ord('Z'):
            keyIndex = ord(last_key_char()) - ord('A')
            letter_height = max_height
            fill(colors[keyIndex])
        else:
            keyIndex = ord(last_key_char()) - ord('a')
            letter_height = min_height
            fill(colors[keyIndex])
    else:
        fill(0)
        letter_height = 10

    global newletter
    newletter = True

    # Update the "letter" position
    global x
    global y
    x = x + letter_width

    # Wrap horizontally
    if x > width() - letter_width:
        x = 0
        y = y + max_height

    # Wrap vertically
    if y > height() - letter_height:
        y = 0  # Reset y to 0

on_key_press(keyPressed)
on_draw(draw)
jygsaw_start(0.05)
