# Lab 1 09/13/2017
# Yi Chen yc2329
# Mingda Yang my432

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...
# setup piTFT buttons
#                        V need this so that button doesn't 'float'!
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 22 as input GPIO pin, as pull up network)

while True:
    time.sleep(0.2)  # Without sleep, no screen output!
    if ( not GPIO.input(22) ):                      # Check GPIO 22, if it is pressed, report
        print (" ")
        print "Button 22 pressed...."

