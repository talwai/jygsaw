from jygsaw.graphics import *
from random import randint


# Count the number of adjacent cells 'on'
def neighbors(x, y):
    return (world[(x + 1) % sx][y][0] +
            world[x][(y + 1) % sy][0] +
            world[(x + sx - 1) % sx][y][0] +
            world[x][(y + sy - 1) % sy][0] +
            world[(x + 1) % sx][(y + 1) % sy][0] +
            world[(x + sx - 1) % sx][(y + 1) % sy][0] +
            world[(x + sx - 1) % sx][(y + sy - 1) % sy][0] +
            world[(x + 1) % sx][(y + sy - 1) % sy][0])


canvas(64, 36)
background(black)
frameRate(12)
sx = width()
sy = height()
world = [[[0 for k in xrange(2)] for j in xrange(sy)] for i in xrange(sx)]
density = 0.5

# Set random cells to 'on'
for i in range(sx * sy * density):
    x = randint(0, sx - 1)
    y = randint(0, sy - 1)
    world[x][y][1] = 1

while True:
    clear()
    # Drawing and update cycle
    for x in range(sx):
        for y in range(sy):
            if ((world[x][y][1] == 1) or (world[x][y][1] == 0 and world[x][y][0] == 1)):
                world[x][y][0] = 1
                point(x, y, white)

        if (world[x][y][1] == -1):
            world[x][y][0] = 0
            world[x][y][1] = 0

    # Birth and death cycle
    for x in range(sx):
        for y in range(sy):
            count = neighbors(x, y)
            if (count == 3 and world[x][y][0] == 0):
                world[x][y][1] = 1

            if ((count < 2 or count > 3) and world[x][y][0] == 1):
                world[x][y][1] = -1

    refresh(1.0 / 12)
