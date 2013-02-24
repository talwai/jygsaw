from jygsaw.graphics import *



canvas(750, 360)
background(darkGray)
loop()
y = 60
textHeight = 30
words=""
textList=[]

def draw():
    global y,textHeight, words
    clear()
    t=text(25, 25, "Type onto the screen:", color=gray, attribute=PLAIN)
    t._set_size(textHeight)
    t._set_font("Georgia")
    for (i,h) in textList:
        ti=text(25, h, i, color=white, attribute=PLAIN)
        ti._set_font("Arial")
        ti._set_size(textHeight)
    tw=text(25, y, words, color=white, attribute=PLAIN)
    tw._set_font("Arial")
    tw._set_size(textHeight)

def keyPressed():
    global words, textList, y, textHeight
    k = lastKeyChar()
    c = lastKeyCode()
    if (c!=10 and c!=16):
        words += k
    elif c==10:
        newLine=words
        words=""
        textList.append((newLine,y))
        y+=textHeight
               

onKeyPress(keyPressed)
onDraw(draw)
