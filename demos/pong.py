# pong.py
#
# Jysaw demo - a pong game
#
# Attribution: Ported to Jygsaw by Avery Yen from Dartmouth
# CS 1 lab solution

# pong.py
# Solution to CS 1 Lab Assignment #1.
# Written by Peter Johnson, updated for cs1lib by Devin Balkcom.
# Major changes by THC.
# Ported to Jygsaw by Avery Yen.
# Plays a game of pong.  A ball bounces around, and paddles move
# up and down to meet the ball.  Whenever the ball hits the left or
# right wall, the game is over.  Whenever the ball hits the top or
# bottom wall, it bounces off the wall.  Whenever the ball hits a
# paddle, it bounces off the paddle.
# Pressing "a" moves the left paddle up.
# Pressing "z" moves the left paddle down.
# Pressing "k" moves the right paddle up.
# Pressing "m" moves the right paddle down.
# Pressing the space bar starts a new game.
# Pressing "q" quits the program.

from jygsaw.graphics import *

# Constants for the keys that matter.
RESTART_KEY = "SPACE"
QUIT_KEY = "q"
LEFT_PADDLE_UP_KEY = "a"
LEFT_PADDLE_DOWN_KEY = "z"
RIGHT_PADDLE_UP_KEY = "k"
RIGHT_PADDLE_DOWN_KEY = "m"

PADDLE_HEIGHT = 80          # paddle height, in pixels
PADDLE_WIDTH = 20           # paddle width, in pixels
PADDLE_MOVE_SPEED = 5      # how many pixels paddles move per frame

WINDOW_WIDTH = 400          # in pixels
WINDOW_HEIGHT = 400         # in pixels

BALL_RADIUS = 10            # in pixels
INITIAL_HORIZ_VELOCITY = 3  # the ball's initial horizontal velocity
INITIAL_VERT_VELOCITY = 3   # the ball's initial vertical velocity

WALL_THICKNESS = 5          # thickness of each wall, in pixels

DELAY = 0.02                # duration of nap time

# The leftmost coordinates of the two paddles.
LEFT_PADDLE_X = WALL_THICKNESS
RIGHT_PADDLE_X = WINDOW_WIDTH - WALL_THICKNESS - PADDLE_WIDTH

# The inner x-coordinates of the two paddles.
LEFT_PADDLE_RIGHT = LEFT_PADDLE_X + PADDLE_WIDTH
RIGHT_PADDLE_LEFT = RIGHT_PADDLE_X

# Locations of wall sides and wall dimensions.
TOP_WALL_TOP = 0
TOP_WALL_BOTTOM = WALL_THICKNESS
HORIZ_WALL_LEFT = 0
HORIZ_WALL_RIGHT = WINDOW_WIDTH
HORIZ_WALL_WIDTH = WINDOW_WIDTH
HORIZ_WALL_HEIGHT = WALL_THICKNESS
BOTTOM_WALL_TOP = WINDOW_HEIGHT - WALL_THICKNESS
LEFT_WALL_LEFT = 0
LEFT_WALL_RIGHT = WALL_THICKNESS
VERT_WALL_TOP = WALL_THICKNESS
VERT_WALL_BOTTOM = WINDOW_HEIGHT - WALL_THICKNESS
VERT_WALL_WIDTH = WALL_THICKNESS
VERT_WALL_HEIGHT = WINDOW_HEIGHT - 2 * WALL_THICKNESS
RIGHT_WALL_LEFT = WINDOW_WIDTH - WALL_THICKNESS

# Where the string saying how to start the game is placed.
GAME_START_MSG_WIDTH = 222      # in pixels
GAME_START_MSG_X = (WINDOW_WIDTH - GAME_START_MSG_WIDTH) / 2
GAME_START_MSG_Y = 3 * WINDOW_HEIGHT / 4


# Determine whether the ball touches a vertical line and within a given
# vertical range.
def ball_touches_vert_line(ball_x, ball_y, line_x, line_top, line_bottom):
    # Does a horizontal line going through the center of the ball intersect
    # the line?
    return (line_x >= ball_x - BALL_RADIUS and line_x <= ball_x + BALL_RADIUS and
            ball_y >= line_top and ball_y <= line_bottom)


# Determine whether the ball touches a horizontal line and within a given
# horiztonal range.
def ball_touches_horiz_line(ball_x, ball_y, line_y, line_left, line_right):
    # Does a vertical line going through the center of the ball intersect
    # the line?
    return (line_y >= ball_y - BALL_RADIUS and line_y <= ball_y + BALL_RADIUS and
            ball_x >= line_left and ball_y <= line_right)


# Draw the background, including the walls.
def draw_walls():
    # Draw the left and right walls in red.
    fill(255, 0, 0)
    rect(LEFT_WALL_LEFT, VERT_WALL_TOP, VERT_WALL_WIDTH, VERT_WALL_HEIGHT)
    rect(RIGHT_WALL_LEFT, VERT_WALL_TOP, VERT_WALL_WIDTH, VERT_WALL_HEIGHT)

    # Draw the top and bottom walls in blue.
    fill(0, 0, 255)
    rect(HORIZ_WALL_LEFT, TOP_WALL_TOP, HORIZ_WALL_WIDTH, HORIZ_WALL_HEIGHT)
    rect(HORIZ_WALL_LEFT, BOTTOM_WALL_TOP, HORIZ_WALL_WIDTH, HORIZ_WALL_HEIGHT)


# Put the ball in the middle of the window.
def center_ball():
    global ball_x, ball_y

    ball_x = WINDOW_WIDTH / 2
    ball_y = WINDOW_HEIGHT / 2


# Start the game.
def start_game():
    global ball_x_velocity, ball_y_velocity
    global game_in_progress

    ball_x_velocity = INITIAL_HORIZ_VELOCITY
    ball_y_velocity = INITIAL_VERT_VELOCITY
    game_in_progress = True


# Halt the game.
def stop_game():
    global game_in_progress

    game_in_progress = False


# Main function.  Plays the game.
canvas(WINDOW_WIDTH, WINDOW_HEIGHT, "PONG")
center_ball()
stop_game()
background(255, 255, 96)

# Start both paddles at the top.
left_paddle_y = TOP_WALL_TOP + HORIZ_WALL_HEIGHT
right_paddle_y = TOP_WALL_TOP + HORIZ_WALL_HEIGHT

while True:
    clear()

    if isKeyPressed(QUIT_KEY):
        exit()
    elif isKeyPressed(RESTART_KEY):
        # Start a game.
        center_ball()
        start_game()

    draw_walls()

    # Draw the paddles.
    fill(0, 128, 0)   # dark green
    rect(LEFT_PADDLE_X, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    rect(RIGHT_PADDLE_X, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    # Draw the ball.
    fill(128, 0, 64)    # purple
    circle(ball_x, ball_y, BALL_RADIUS)

    # If no game in progress, tell user how to start.
    if not game_in_progress:
        text(GAME_START_MSG_X, GAME_START_MSG_Y,
             "Press the SPACE bar to start a game")

    # End the game if the ball touches a vertical wall.
    if (ball_touches_vert_line(ball_x, ball_y, LEFT_WALL_RIGHT,
                               VERT_WALL_TOP, VERT_WALL_BOTTOM) or
        ball_touches_vert_line(ball_x, ball_y, RIGHT_WALL_LEFT,
                               VERT_WALL_TOP, VERT_WALL_BOTTOM)):
        stop_game()

    # Negate x velocity if the ball touches a vertical paddle surface,
    # but also move it a ball radius away from the paddle so that we don't
    # get caught oscillating the x-velocity.
    elif (ball_touches_vert_line(ball_x, ball_y, LEFT_PADDLE_RIGHT,
                                 left_paddle_y, left_paddle_y + PADDLE_HEIGHT) or
          ball_touches_vert_line(ball_x, ball_y, RIGHT_PADDLE_LEFT,
                                 right_paddle_y, right_paddle_y + PADDLE_HEIGHT)):
        ball_x_velocity = - ball_x_velocity
        if ball_x > WINDOW_WIDTH / 2:
            ball_x = RIGHT_PADDLE_LEFT - \
                BALL_RADIUS    # move away from right paddle
        else:
            ball_x = LEFT_PADDLE_RIGHT + \
                BALL_RADIUS    # move away from left paddle

    # Negate y velocity if the ball touches a horizontal wall.
    if (ball_touches_horiz_line(ball_x, ball_y, TOP_WALL_BOTTOM,
                                HORIZ_WALL_LEFT, HORIZ_WALL_RIGHT) or
        ball_touches_horiz_line(ball_x, ball_y, BOTTOM_WALL_TOP,
                                HORIZ_WALL_LEFT, HORIZ_WALL_RIGHT)):
        ball_y_velocity = - ball_y_velocity

    # If the game is in progress, update the ball's position in both
    # directions.
    if game_in_progress:
        ball_x = ball_x + ball_x_velocity
        ball_y = ball_y + ball_y_velocity

    # Move the paddles appropriately, but never let them go out of the
    # field of play.
    if isKeyPressed(LEFT_PADDLE_UP_KEY) and left_paddle_y > TOP_WALL_TOP + HORIZ_WALL_HEIGHT:
        left_paddle_y = left_paddle_y - PADDLE_MOVE_SPEED
    if isKeyPressed(LEFT_PADDLE_DOWN_KEY) and left_paddle_y + PADDLE_HEIGHT < BOTTOM_WALL_TOP:
        left_paddle_y = left_paddle_y + PADDLE_MOVE_SPEED
    if isKeyPressed(RIGHT_PADDLE_UP_KEY) and right_paddle_y > TOP_WALL_TOP + HORIZ_WALL_HEIGHT:
        right_paddle_y = right_paddle_y - PADDLE_MOVE_SPEED
    if isKeyPressed(RIGHT_PADDLE_DOWN_KEY) and right_paddle_y + PADDLE_HEIGHT < BOTTOM_WALL_TOP:
        right_paddle_y = right_paddle_y + PADDLE_MOVE_SPEED

    refresh(DELAY)
