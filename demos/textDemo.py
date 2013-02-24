from jygsaw.graphics import *



canvas(750, 360)
background(white)
loop()
y = 60
textHeight = 30
words=""
textList=[]

def draw():
    global y,textHeight, words
    clear()
    text((25, 25), "Type onto the screen:", "Georgia", 25, color=lightGray, attribute=PLAIN)
    for (i,h) in textList:
        text((25, h), i, "Arial", textHeight, color=white, attribute=PLAIN)
    text((25, y), words, "Arial", textHeight, color=white, attribute=PLAIN)
    

def keyPressed():
    global words, textList, y, textHeight
    # If the key is between 'A' (65) and 'z' (122)
    k = lastKeyChar()
    c = lastKeyCode()
    if (c!=10 and c!=16):
        print k
        print c
        words += k
    elif c==10:
        newLine=words
        words=""
        textList.append((newLine,y))
        y+=textHeight
               

onKeyPress(keyPressed)
onDraw(draw)
