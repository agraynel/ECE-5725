# Lab 3 10/04/2017
# Yi Chen yc2329
# Mingda Yang my432

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 17 as input GPIO pin, as pull up network)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 22 as input GPIO pin, as pull up network)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 23 as input GPIO pin, as pull up network)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 27 as input GPIO pin, as pull up network)

# Set GPIO 12 & 18 as output
GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

stop1 = True
stop2 = True
# Set duty cycle
dc1 = 6.8
dc2 = 6.8
# Set channel & frequency
p1 = GPIO.PWM(12,50)
p2 = GPIO.PWM(18,50)


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
        if dc1>7.5:
            dc1 = 6.5
            p1.ChangeDutyCycle(dc1)
        else:
            dc1 = 8.2
            p1.ChangeDutyCycle(dc1)
    
    if(not GPIO.input(23)):
        time.sleep(0.2)
        if dc2>7.5:
            dc2 = 6.8
            p2.ChangeDutyCycle(dc2)
        else:
            dc2 = 8.2
            p2.ChangeDutyCycle(dc2)
    
    if(not GPIO.input(22)):
        time.sleep(0.2)
        if(stop1 == True):
            stop1 = False
        else:
            stop1 = True
    if(not GPIO.input(27)):
        time.sleep(0.2)
        if(stop2 == True):
            stop2 = False
        else:
            stop2 = True




