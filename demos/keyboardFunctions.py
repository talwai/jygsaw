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
background(0.5)
loop()

# Set a color for each key
for i in range(numChars):
    colors.append(Color.getHSBColor(float(i) / float(numChars), 1, 1))


def draw():
    global newletter
    if newletter == True:
        # Draw the 'letter'
        print 'letterHeight', letterHeight
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
        print 'key', lastKeyChar(), keyIndex, ord(lastKeyChar())
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
