# Lab 2 09/18/2017
# Yi Chen yc2329
# Mingda Yang my432

import RPi.GPIO as GPIO
import time
import subprocess

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
    time.sleep(0.2)  # Without sleep, no screen output!
    if ( not GPIO.input(17) ):                      # Check whether 17 is pressed, if yes, send cmd echo pause to my_fifo
        cmd = 'echo "pause" > /home/pi/Desktop/Lab1/my_fifo'
	print subprocess.check_output(cmd,shell=True)   # Run the commend with subprocess, first check whether commend is exist  and correct, then if yes return, else raise error flag
    elif( not GPIO.input(22) ):                     # Check whether 22 is pressed, if yes, send cmd echo seek +10s to my_fifo
	cmd = 'echo "seek 10" > /home/pi/Desktop/Lab1/my_fifo'
	print subprocess.check_output(cmd,shell=True)   # Run the commend with subprocess, first check whether commend is exist  and correct, then if yes return, else raise error flag
    elif( not GPIO.input(23) ):                     # Check whether 23 is pressed, if yes, send cmd echo seek -10s to my_fifo
	cmd = 'echo "seek -10" > /home/pi/Desktop/Lab1/my_fifo'
	print subprocess.check_output(cmd,shell=True)   # Run the commend with subprocess, first check whether commend is exist  and correct, then if yes return, else raise error flag
    elif( not GPIO.input(26) ):                     # Check whether 26 is pressed, if yes, send cmd echo seek +10s to my_fifo
	cmd = 'echo "seek 30" > /home/pi/Desktop/Lab1/my_fifo'
	print subprocess.check_output(cmd,shell=True)   # Run the commend with subprocess, first check whether commend is exist  and correct, then if yes return, else raise error flag
    elif(GPIO.input(5) ):                     # Check whether 5 is pressed, if yes, send cmd echo seek -10s to my_fifo
	cmd = 'echo "seek -30" > /home/pi/Desktop/Lab1/my_fifo'
	print subprocess.check_output(cmd,shell=True)   # Run the commend with subprocess, first check whether commend is exist  and correct, then if yes return, else raise error flag
    elif( not GPIO.input(27) ):                     # Check whether 27 is pressed, if yes, send cmd echo quit to my_fifo
	cmd = 'echo "quit" > /home/pi/Desktop/Lab1/my_fifo'
	print subprocess.check_output(cmd,shell=True)   # Run the commend with subprocess, first check whether commend is exist  and correct, then if yes return, else raise error flag
	break                                           # Then quit the program.

