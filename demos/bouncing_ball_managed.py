# CS 1 example: Simple animation of a bouncing ball
# Devin Balkcom
# August, 2011
# Modified by THC.

from jygsaw.graphics import *

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

FRAME_RATE = 60     # how many frames to display per second
TIMESTEP = 1.0 / FRAME_RATE    # how often to refresh the frame

# Computations will now use meters, and we'll convert meters to
# pixels with a scaling factor during drawing:
PIXELS_PER_METER = 10.0

FLOOR_Y = 4.0       # location now in meters

INITIAL_X = 5.0     # locations are now measuRED in meters
INITIAL_Y = 25.0
INITIAL_V_X = 4.0
INITIAL_V_Y = 0.0   # velocity is now measuRED in meters/second

EARTH_GRAVITY_ACCELERATION = -9.8  # m/sec^2

BALL_RADIUS = 10  # radius of the ball in pixels, not used in velocity computations


def draw_ball(x, y):
    fill(BLUE)   # blue ball

    # compute screen coordinates based on meter location of ball
    sx = x * PIXELS_PER_METER
    sy = WINDOW_HEIGHT - y * PIXELS_PER_METER

    no_stroke()
    circle(sx, sy, BALL_RADIUS)


def draw_floor():
    # strokeWidth(2)
    stroke(BLACK)  # black floor

    line(0, WINDOW_HEIGHT - FLOOR_Y * PIXELS_PER_METER, WINDOW_WIDTH,
         WINDOW_HEIGHT - FLOOR_Y * PIXELS_PER_METER)


# Computation of position uses meters, not pixels.
def compute_next_position(position, velocity, timestep):
    return position + velocity * timestep


def compute_next_velocity(velocity, acceleration, timestep):
    return velocity + acceleration * timestep

# Initial coordinates for the ball.
x = INITIAL_X
y = INITIAL_Y

# x and y velocities for the ball.
v_x = INITIAL_V_X
v_y = INITIAL_V_Y

canvas(WINDOW_WIDTH, WINDOW_HEIGHT, "Bouncing ball")

background(WHITE)

def bounce():
    global x, y, v_x, v_y

    # Draw the current frame.
    clear()
    draw_ball(x, y)
    draw_floor()

    # Update the state for the next frame.
    # See where the ball will be at its current velocity.
    next_y = compute_next_position(y, v_y, TIMESTEP)
    next_x = compute_next_position(x, v_x, TIMESTEP)

    # Will the ball bounce off the floor?
    if next_y - (BALL_RADIUS / PIXELS_PER_METER) < FLOOR_Y:
        v_y = -v_y

    # Will the ball bounce off a side wall?
    if (next_x * PIXELS_PER_METER + BALL_RADIUS > WINDOW_WIDTH or
        next_x * PIXELS_PER_METER - BALL_RADIUS < 0):
        v_x = -v_x

    # Now compute the real next position and next velocity.
    x = compute_next_position(x, v_x, TIMESTEP)
    y = compute_next_position(y, v_y, TIMESTEP)
    v_y = compute_next_velocity(v_y, EARTH_GRAVITY_ACCELERATION, TIMESTEP)

on_draw(bounce)
jygsaw_start(TIMESTEP)
