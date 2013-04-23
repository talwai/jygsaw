# hello_world.py
#
# Jygsaw demo - prints Hello World
from jygsaw.graphics import *

canvas()

font('Times New Roman')
text_size(32)
fill(red)
t = text(100, 100, 'Hello, world!')
t.font = 'Arial'

text_size(16)
font('Courier')
fill(blue)
text(120, 150, 'World, hello!')
