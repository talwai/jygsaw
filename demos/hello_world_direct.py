# hello_world_direct.py
#
# Jygsaw demo - prints Hello World
from jygsaw.graphics import *

canvas()

font('Times New Roman')
text_size(32)
fill(RED)
t = text(100, 100, 'Hello, world!')
t.font = 'Arial'

text_size(16)
font('Courier New')
fill(BLUE)
text(120, 150, 'World, hello!')
