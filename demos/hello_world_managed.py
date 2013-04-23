# hello_world_managed.py
#
# Jygsaw demo - prints Hello World
from jygsaw.graphics import *
from time import sleep

canvas()

def write():
    font('Times New Roman')
    textSize(32)
    fill(red)
    t = text(100, 100, 'Hello, world!')
    t.font = 'Arial'
    
    textSize(16)
    font('Courier')
    fill(blue)
    text(120, 150, 'World, hello!')

onDraw(write)
jygsawMain(0)
