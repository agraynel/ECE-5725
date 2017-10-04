# Lab 2 09/18/2017
# Yi Chen yc2329
# Mingda Yang my432

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...
# setup piTFT buttons
#                        V need this so that button doesn't 'float'!
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 17 as input GPIO pin, as pull up network)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 22 as input GPIO pin, as pull up network)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 23 as input GPIO pin, as pull up network)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 27 as input GPIO pin, as pull up network)
# add two new buttons
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set up broadcom number 26 as input GPIO pin, as pull up network)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # set up broadcom number 5 as input GPIO pin, as pull up network)

while True:
    time.sleep(0.2)                                 # Without sleep, no screen output!
    if ( not GPIO.input(17) ):                      # Check GPIO 17, if it is pressed, report             
        print (" ")
        print "Button 17 pressed...."

    elif( not GPIO.input(22) ):                     # Check GPIO 22, if it is pressed, report  
		print (" ")
		print "Button 22 pressed...."                     
    elif( not GPIO.input(23) ):                     # Check GPIO 23, if it is pressed, report  
		print (" ")
		print "Button 23 pressed...." 
    elif( not GPIO.input(26) ):                     # Check GPIO 26, if it is pressed, report  
		print (" ")
		print "Button 26 pressed...."
    elif( GPIO.input(5) ):                     # Check GPIO 5, if it is pressed, report  
		print (" ")
		print "Button 5 pressed...."	                  
    elif( not GPIO.input(27) ):                     # Check GPIO 27, if it is pressed, report, then quit the program
		print (" ")
		print "Button 27 pressed...."
		break
