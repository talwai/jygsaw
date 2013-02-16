import sys
import os
sys.path.append(os.path.pardir + "/lib")
from graphicsWrapper import *

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
background(numChars/2)
loop()

# Set a color for each key
for i in range(numChars):
#    colors.append(color(i, numChars, numChars))
    colors.append(red)

def draw():
    global newletter
    if newletter == True:
        # Draw the 'letter'
        y_pos = 0
        fill(red)
        if letterHeight == maxHeight:
            y_pos = y
            rect(x, y_pos, letterWidth, letterHeight, color = blue)
        else:
            y_pos = y + minHeight
            rect(x, y_pos, letterWidth, letterHeight)
            fill(numChars/2)
            rect(x, y_pos - minHeight, letterWidth, letterHeight)
        newletter = False

def keyPressed():
    # If the key is between 'A' (65) and 'z' (122)
    if lastKeyCode() >= ord('A') and lastKeyCode() <= ord('z'):
        keyIndex = -1
        if lastKeyCode() <= ord('Z'):
            keyIndex = lastKeyCode() - ord('A')
            global letterHeight
            letterHeight = maxHeight
            fill(colors[keyIndex])
        else:
            keyIndex = lastKeyCode() - ord('a')
            global letterHeight
            letterheight = minHeight
            fill(colors[keyIndex])
    else:
        fill(0)
        global letterHeight
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
        y = 0 # Reset y to 0
       
onKeyPress(keyPressed)
onDraw(draw)
