from jygsaw.graphics import *



canvas(750, 360)
background(white)
loop()
words = ""
letterWidth = 20
y = 60
tH = 30

def draw():
    clear()
    text((25, 25), "Type onto the screen:", "Georgia", 25, color=lightGray, attribute=PLAIN)
    text((25, y), words, "Arial", tH, color=black, attribute=PLAIN)

   
def keyPressed():
    global words, y, tH
    # If the key is between 'A' (65) and 'z' (122)
    k = lastKeyChar()
    c = lastKeyCode()
    if (c!=10 and c!=16):
        print k
        print c
        words += k
    elif c==10:
        y+=tH
        words=""


onKeyPress(keyPressed)
onDraw(draw)
