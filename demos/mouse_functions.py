# mouse_functions.py
#
# Jygsaw demo - Has a box that can be dragged by the mouse.
#
# Attribution: inspired by the mousefunction demo in Processing
# from http://processingjs.org/learning/basic/mousefunctions/
# written by Casey Reas and Ben Fry

from jygsaw.graphics import *

bx = 0.0
by = 0.0
box_size = 75
over_box = False
locked = False
x_offset = 0.0
y_offset = 0.0


canvas(640, 360)
bx = width() / 2
by = height() / 2


def draw():
    global over_box
    clear()
    background(0)

    # Test if the cursor is over the box
    if (mouse_x() > bx and mouse_x() < bx + box_size and
            mouse_y() > by and mouse_y() < by + box_size):
        over_box = True
        if not locked:
            stroke(255)
            fill(153)
    else:
        stroke(153)
        fill(153)
        over_box = False

    # Draw the box
    rect(bx, by, box_size, box_size)


def mouse_pressed():
    global locked, x_offset, y_offset

    if over_box:
        locked = True
        fill(255, 255, 255)
    else:
        locked = False

    x_offset = mouse_x() - bx
    y_offset = mouse_y() - by


def mouse_dragged():
    global bx, by
    if locked:
        bx = mouse_x() - x_offset
        by = mouse_y() - y_offset


def mouse_released():
    global locked
    locked = False


on_mouse_press(mouse_pressed)
on_mouse_drag(mouse_dragged)
on_mouse_release(mouse_released)
on_draw(draw)
jygsaw_start(1.0 / 30)
