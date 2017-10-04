# Lab 2 09/18/2017
# Yi Chen yc2329
# Mingda Yang my432

import pygame # Import Library and initialize pygame
from pygame.locals import *
import os
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1') #
os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()

pygame.mouse.set_visible(False)

size = width, height = 320, 240
speed1 = [2,2]
speed2 = [1,1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball1 = pygame.image.load("magic_ball.png")
ball2 = pygame.image.load("soccer_ball.png")
ballrect1 = ball1.get_rect()
ballrect2 = ball2.get_rect()

while 1:
    if ( not GPIO.input(27) ):                      # Check GPIO 17, if it is pressed, report             
        break
    ballrect1 = ballrect1.move(speed1)
    ballrect2 = ballrect2.move(speed2)
    if ballrect1.left < 0 or ballrect1.right > width:
        speed1[0] = -speed1[0]
    if ballrect1.top < 0 or ballrect1.bottom > height:
        speed1[1] = -speed1[1]
    if ballrect2.left < 0 or ballrect2.right > width:
        speed2[0] = -speed2[0]
    if ballrect2.top < 0 or ballrect2.bottom > height:
        speed2[1] = -speed2[1]
    screen.fill(black) # Erase the Work space
    screen.blit(ball1, ballrect1) # Combine Ball surface with workspace surface
    screen.blit(ball2, ballrect2)
    pygame.display.flip() # display workspace on screen