from jygsaw.graphics import *
import random

# Snake for Jygsay by David Lam

# Keys for controlling game
keys = {"start": " ",  # space bar
        "left": "j",   # j
        "up": "i",     # i
        "down": "k",   # k
        "right": "l"   # l
        }

direction = {"left": (-1, 0),  # j
             "up": (0, -1),    # i
             "down": (0, 1),   # k
             "right": (1, 0)   # l
             }

# Sizes of things
CANVAS_SIZE = 500
BLOCK_SIZE = 25
MAX_BLOCK = CANVAS_SIZE / BLOCK_SIZE

# Nap time
DELAY = 0.2
# colors of objects
BACKGROUND_COLOR = gray
SNAKE_COLOR = yellow
FOOD_COLOR = green

# state variables
FOOD_EXISTS = False
GROW = False
FOOD_ROW = 10
FOOD_COL = 10

START = 1
PLAY = 2
LOST = 3

state = START

DIR = direction["right"]

# snake represented by two parallel arrays
# to move, pop tail of the snake, and add
# to the head of the snake.
SNAKE_ROW = None
SNAKE_COL = None


# move snake
def move_snake():
    global SNAKE_ROW, SNAKE_COL, FOOD_EXISTS, FOOD_COL, FOOD_ROW, DIR

    (row_delta, col_delta) = DIR
    new_col = SNAKE_COL[0] + col_delta
    new_row = SNAKE_ROW[0] + row_delta

    # move in the right direction
    # add head to the list
    SNAKE_ROW.insert(0, new_row)
    SNAKE_COL.insert(0, new_col)

    snake = zip(SNAKE_COL, SNAKE_ROW)

    # did snake eat food?
    if (FOOD_COL, FOOD_ROW) not in snake:
        SNAKE_ROW.pop()
        SNAKE_COL.pop()
    else:
        FOOD_EXISTS = False

    # draw snake
    for i in xrange(0, len(SNAKE_ROW)):
        rect(SNAKE_ROW[i] * BLOCK_SIZE, SNAKE_COL[i] * BLOCK_SIZE,
             BLOCK_SIZE, BLOCK_SIZE, color=SNAKE_COLOR)


# generate random location of food pellet not
# occupied by snake
def generate_food_pellet():
    global FOOD_COL, FOOD_ROW

    while True:
        FOOD_COL = random.randint(0, MAX_BLOCK - 1)
        FOOD_ROW = random.randint(0, MAX_BLOCK - 1)

        snake = zip(SNAKE_COL, SNAKE_ROW)

        if (FOOD_COL, FOOD_ROW) not in snake:
            break


# detect for self-collisions
def check_self_collisions():
    snake = zip(SNAKE_COL, SNAKE_ROW)
    return (len(snake) != len(set(snake)))


# detect collisions into wall
def check_wall_collisions():
    row = sorted(SNAKE_ROW)
    col = sorted(SNAKE_COL)

    if row[0] < 0 or row.pop() >= MAX_BLOCK:
        return True

    if col[0] < 0 or col.pop() >= MAX_BLOCK:
        return True

    return False

# how to represent map pixels to cells?
canvas(CANVAS_SIZE, CANVAS_SIZE)
background(BACKGROUND_COLOR)


def reset():
    global SNAKE_ROW, SNAKE_COL, FOOD_ROW, FOOD_COL

    SNAKE_ROW = [4, 4, 4, 4]
    SNAKE_COL = [4, 5, 6, 7]

    FOOD_ROW = 10
    FOOD_COL = 10

    for i in xrange(0, len(SNAKE_ROW)):
        rect(SNAKE_ROW[i] * BLOCK_SIZE, SNAKE_COL[i] * BLOCK_SIZE,
             BLOCK_SIZE, BLOCK_SIZE, color=SNAKE_COLOR)

# main loop
while True:
    clear()

    # Get the key pressed and change state
    # or direction as appropriate
    key = lastKeyChar()

    if key == keys["left"]:
        DIR = direction["left"]
    elif key == keys["right"]:
        DIR = direction["right"]
    elif key == keys["up"]:
        DIR = direction["up"]
    elif key == keys["down"]:
        DIR = direction["down"]
    elif key == keys["start"]:
        state = PLAY

    # print message
    if state is START:
        text(25, 10, "Press Space to start game!", color=white, attribute=PLAIN)
        text(25, 20, "i = UP", color=white, attribute=PLAIN)
        text(25, 30, "j = LEFT, l = RIGHT", color=white, attribute=PLAIN)
        text(25, 40, "k = DOWN", color=white, attribute=PLAIN)

        reset()
        continue

    # generate food pellet
    if FOOD_EXISTS is False:
        generate_food_pellet()
        FOOD_EXISTS = True

    rect(FOOD_ROW * BLOCK_SIZE, FOOD_COL * BLOCK_SIZE,
         BLOCK_SIZE, BLOCK_SIZE, color=FOOD_COLOR)

    # update snake
    move_snake()

    # check for collisions
    if check_self_collisions() or check_wall_collisions():
        state = START
        text(25, 10, "You lost! Press Space to restart", color=white, attribute=PLAIN)

    refresh(DELAY)
