# keyboard_colors.py
#
# Jygsaw demo - prints colors  from keyboard presses
#
# Attribution: inspired by the keyboardfunction demo in Processing
# from http://processingjs.org/learning/basic/keyboardfunctions/
# written by Casey Reas and Ben Fry.#

from jygsaw.graphics import *

maxHeight = 40
minHeight = 20
letterHeight = maxHeight
letterWidth = 20

x = -letterWidth
y = 0

newletter = False

numChars = 26
colors = []

canvas(640, 360)
noStroke()
background(100)

# Set a color for each key
for i in range(numChars):
    colors.append(Color.getHSBColor(float(i) / float(numChars), 1, 1))


def draw():
    global newletter
    if newletter is True:
        # Draw the 'letter'
        y_pos = 0
        if letterHeight == maxHeight:
            y_pos = y
            rect(x, y_pos, letterWidth, letterHeight)
        else:
            y_pos = y + minHeight
            rect(x, y_pos, letterWidth, letterHeight)
        newletter = False


def keyPressed():
    # If the key is between 'A' (65) and 'z' (122)
    global letterHeight
    if ord(lastKeyChar()) >= ord('A') and ord(lastKeyChar()) <= ord('z'):
        keyIndex = -1
        if ord(lastKeyChar()) <= ord('Z'):
            keyIndex = ord(lastKeyChar()) - ord('A')
            letterHeight = maxHeight
            fill(colors[keyIndex])
        else:
            keyIndex = ord(lastKeyChar()) - ord('a')
            letterHeight = minHeight
            fill(colors[keyIndex])
    else:
        fill(0)
        letterHeight = 10

    global newletter
    newletter = True

    # Update the "letter" position
    global x
    global y
    x = x + letterWidth

    # Wrap horizontally
    if x > width() - letterWidth:
        x = 0
        y = y + maxHeight

    # Wrap vertically
    if y > height() - letterHeight:
        y = 0  # Reset y to 0

onKeyPress(keyPressed)
onDraw(draw)
jygsawMain(0.05)
