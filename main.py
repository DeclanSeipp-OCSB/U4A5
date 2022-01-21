import pygame
import random
from pygame import Color, draw, display, time

# Variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
center_ball_x = 250
center_ball_y = 250
ball_radius = 30

# change position of ball
dx = random.randint(2, 4)
dy = random.randint(2, 4)

# inizialize pygame modules
pygame.init()
clock = time.Clock()

# create surface fir graphics display
gameDisplay = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.flip()

while True:

  # white background
  gameDisplay.fill(Color('white'))

  #draw a ball
  draw.circle(gameDisplay, Color('blue'), (center_ball_x, center_ball_y), ball_radius)

  center_ball_x = center_ball_x + dx
  center_ball_y = center_ball_y + dy

  # make ball bounce off walls
  if center_ball_x + ball_radius > SCREEN_WIDTH or center_ball_x - ball_radius < 0:
    dx = -dx

  if center_ball_y + ball_radius > SCREEN_HEIGHT or center_ball_y - ball_radius < 0:
    dy = -dy

  center_ball_x = center_ball_x + dx
  center_ball_y = center_ball_y + dy

  # show graphics on screen  
  display.flip()
  # change speed of ball
  clock.tick(40)
