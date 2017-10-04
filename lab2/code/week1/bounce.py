# Lab 2 09/18/2017
# Yi Chen yc2329
# Mingda Yang my432

import pygame # Import Library and initialize pygame

pygame.init()
size = width, height = 320, 240
speed = [2,2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball = pygame.image.load("magic_ball.png")
ballrect = ball.get_rect()

while 1:
    ballrect = ballrect.move(speed)
    # The ball will bounce when out of screen
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black) # Erase the Work space
    screen.blit(ball, ballrect) # Combine Ball surface with workspace surface
    pygame.display.flip() # display workspace on screen