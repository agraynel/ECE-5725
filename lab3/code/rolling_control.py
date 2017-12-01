# Lab 3 10/11/2017
# Yi Chen yc2329
# Mingda Yang my432
# TA allows us to combine the code together into this one
import RPi.GPIO as GPIO
import time
import pygame # Import Library and initialize pygame
import math
from pygame.locals import *
import os
import sys
#os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
#os.putenv('SDL_FBDEV', '/dev/fb1') #
#os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
#os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')


GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 17 as input GPIO pin, as pull up network)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 22 as input GPIO pin, as pull up network)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 23 as input GPIO pin, as pull up network)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 27 as input GPIO pin, as pull up network)

# Set GPIO 12 & 18 as output
GPIO.setup(12, GPIO.OUT) 
GPIO.setup(18, GPIO.OUT)

pygame.init()

pygame.mouse.set_visible(True)
size = width, height = 320, 240

font_stop = pygame.font.Font(None,20)
buttons = { 'Stop':(160,120)}
buttonr = { 'Resume':(160,120)}
font_quit = pygame.font.Font(None,20)
font_disp = pygame.font.Font(None,20)

black = 0, 0, 0
WHITE = 255, 255, 255
red = 255, 0, 0
# Set screen
screen = pygame.display.set_mode(size)

stop1 = True
stop2 = True
dc1 = 6.8
dc2 = 6.8
p1 = GPIO.PWM(12,50)
p2 = GPIO.PWM(18,50)
lflag = False
rflag = False
sflag = False
lresult1 = 'stop'
lresult2 = 'stop'
lresult3 = 'stop'
rresult1 = 'stop'
rresult2 = 'stop'
rresult3 = 'stop'
rstate = 'Clock'
lstate = 'Clock'
trstate = 'Clock'
tlstate = 'Clock'
while True:
    if stop1:
        p1.start(dc1)
    else:
        p1.ChangeDutyCycle(0)
    if stop2:
        p2.start(dc2)
    else:
        p2.ChangeDutyCycle(0)
        
        
    if(not GPIO.input(17)):
        time.sleep(0.2)
        rflag = True
        if dc1>7.5:
            dc1 = 6.8
            p1.ChangeDutyCycle(dc1)
            trstate = 'Clock'
            rstate = 'Clock'
            
        else:
            dc1 = 8.2
            p1.ChangeDutyCycle(dc1)
            trstate = 'Counter'
            rstate = 'Counter'
    
    if(not GPIO.input(23)):
        time.sleep(0.2)
        lflag = True
        if dc2>7.5:
            dc2 = 6.8
            p2.ChangeDutyCycle(dc2)
            tlstate = 'Clcok'
            lstate = 'Clock'
            
        else:
            dc2 = 8.2
            p2.ChangeDutyCycle(dc2)
            tlstate = 'Counter'
            lstate = 'Counter'
    
    if(not GPIO.input(22)):
        time.sleep(0.2)
        rflag = True
        if(stop1 == True):
            stop1 = False
            rstate = trstate + 'stop'
        else:
            stop1 = True
            rstate = 'resume ' + trstate
            
    if(not GPIO.input(27)):
        time.sleep(0.2)
        lflag = True
        if(stop2 == True):
            stop2 = False
            lstate = tlstate + ' stop'
        else:
            stop2 = True
            lstate = 'resume ' + tlstate

    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif(event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos
            if x>140 and x<180:
                if y>100 and y<140:
                    sflag = not sflag
                    if sflag == True:
                        tstop1 = stop1
                        tstop2 = stop2
                        stop1 = False
                        stop2 = False
                    else:
                        stop1 = tstop1
                        stop2 = tstop2
            if x >260 and x<300:
                if y>180 and y<220:
                    sys.exit()
                    
    if lflag == True:
        lresult3 = lresult2
        lresult2 = lresult1
        lresult1 = lstate 
        lflag = False
    
    if rflag == True:
        rresult3 = rresult2
        rresult2 = rresult1
        rresult1 = rstate
        rflag = False
    
    screen.fill(black)
    l_surface1 = font_disp.render(lresult1, True, WHITE)
    lrect1 = l_surface1.get_rect(center = (60,20))
    screen.blit(l_surface1,lrect1)
    l_surface2 = font_disp.render(lresult2, True, WHITE)
    lrect2 = l_surface2.get_rect(center = (60,100))
    screen.blit(l_surface2,lrect2)
    l_surface3 = font_disp.render(lresult3, True, WHITE)
    lrect3 = l_surface3.get_rect(center = (60,180))
    screen.blit(l_surface3,lrect3)
    
    r_surface1 = font_disp.render(rresult1, True, WHITE)
    rrect1 = r_surface1.get_rect(center = (300,20))
    screen.blit(r_surface1,rrect1)
    r_surface2 = font_disp.render(rresult2, True, WHITE)
    rrect2 = r_surface2.get_rect(center = (300,100))
    screen.blit(r_surface2,rrect2)
    r_surface3 = font_disp.render(rresult3, True, WHITE)
    rrect3 = r_surface3.get_rect(center = (300,180))
    screen.blit(r_surface3,rrect3)
    
    quit_surf = font_quit.render('Quit', True, WHITE)
    qrect = quit_surf.get_rect(center = (280,200))
    screen.blit(quit_surf,qrect)
    if sflag == False:              
        for my_text, text_pos in buttons.items():
            text_surface = font_stop.render(my_text, True, red)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)

    elif sflag == True:
        for my_text, text_pos in buttonr.items():
            text_surface = font_stop.render(my_text, True, WHITE)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
        
            # Erase the Work space
    pygame.display.flip() # display workspace on screen
