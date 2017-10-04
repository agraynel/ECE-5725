# Lab 2 09/27/2017
# Yi Chen yc2329
# Mingda Yang my432

import pygame # Import Library and initialize pygame
import math
from pygame.locals import *
import os
import sys
#os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
#os.putenv('SDL_FBDEV', '/dev/fb1') #
#os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
#os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()

pygame.mouse.set_visible(True)


size = width, height = 320, 240

font_quit = pygame.font.Font(None,20)
buttons = { 'quit':(280,200),'start':(40,200)}
font_cord = pygame.font.Font(None,10)
#font_buttons = pygrame.font.Font(None,20)
#buttons2 = { 'Pause':(40,200),'Fast':(120,200),'Slow':(200,200),'Back':(280,200)}

speed1 = [1,1]
speed2 = [1,1]
tempspeed = [0,0]
temps1 = [0,0]
temps2 = [0,0]
black = 0, 0, 0
WHITE = 255, 255, 255
screen = pygame.display.set_mode(size)
ball1 = pygame.image.load("magic_ball.png")
w1,h1 = ball1.get_size()
ball1 = pygame.transform.scale(ball1,(int(w1/5),int(h1/5)))
ball2 = pygame.image.load("soccer_ball.png")
w2,h2 = ball2.get_size()
ball2 = pygame.transform.scale(ball2,(int(w2/5),int(h2/5)))
ballrect1 = ball1.get_rect()
ballrect2 = ball2.get_rect()

ballrect1.center = [60,100]
ballrect2.center = [140, 180]
radius1 = abs(ballrect1.left-ballrect1.right)/2
radius2 = abs(ballrect2.left-ballrect2.right)/2
#radius1 = 64
#radius2 = 64


x=0
y=0
flag = False
pflag = False


while 1:
    
    
    if flag == True:
        ballrect1 = ballrect1.move(speed1)
        ballrect2 = ballrect2.move(speed2)
        ballrect1.center = [(ballrect1.left+ballrect1.right)/2,(ballrect1.top+ballrect1.bottom)/2]
        ballrect2.center = [(ballrect2.left+ballrect2.right)/2,(ballrect2.top+ballrect2.bottom)/2]
        dist = math.pow((ballrect1.center[0]-ballrect2.center[0]),2)+math.pow((ballrect2.center[1]-ballrect2.center[1]),2)
        dist = math.sqrt(dist)
        if ballrect1.left <= 0 or ballrect1.right >= width:
            speed1[0] = -speed1[0]
        if ballrect1.top <= 0 or ballrect1.bottom >= height:
            speed1[1] = -speed1[1]
        if ballrect2.left <= 0 or ballrect2.right >= width:
            speed2[0] = -speed2[0]
        if ballrect2.top <= 0 or ballrect2.bottom >= height:
            speed2[1] = -speed2[1]
        if dist <= (radius1+radius2):
            tempspeed[0] = speed1[0]
            tempspeed[1] = speed1[1]
            speed1[0] = speed2[0]
            speed1[1] = speed2[1]
            speed2[0] = tempspeed[0]
            speed2[1] = tempspeed[1]

    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif(event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos
            if flag == False:
                if y > 170 and y < 230:
                    if x >250 and x < 310:
                        sys.exit()
                    elif x>10 and x<70:
                        flag = True
            else:    
                if y > 170 and y < 230:
                    if x >250 and x < 310:
                        sys.exit()
                
    screen.fill(black)
    my_out = ("touch at "+str(x)+","+str(y))
    cord_surface = font_cord.render(my_out, True, WHITE)
    rect = cord_surface.get_rect(center = (160,120))
    screen.blit(cord_surface,rect)
    for my_text, text_pos in buttons.items():
        text_surface = font_quit.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)
    # Erase the Work space
    screen.blit(ball1, ballrect1) # Combine Ball surface with workspace surface
    screen.blit(ball2, ballrect2)
    pygame.display.flip() # display workspace on screen
