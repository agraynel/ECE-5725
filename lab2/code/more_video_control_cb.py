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

#Call back functions
def GPIO17_callback(channel):
    print "falling edge detected on 17"
    cmd = 'echo "pause" > /home/pi/Desktop/Lab1/my_fifo'
	print subprocess.check_output(cmd,shell=True)   # Run the command with subprocess, first check whether commend is exist  and correct, then if yes return, else raise error flag
def GPIO22_callback(channel):
    print "falling edge detected on 22"
    cmd = 'echo "seek 10" > /home/pi/Desktop/Lab1/my_fifo'
	print subprocess.check_output(cmd,shell=True)   # Run the command with subprocess, first check whether commend is exist  and correct, then if yes return, else raise error flag
def GPIO23_callback(channel):
    print "falling edge detected on 23"
    cmd = 'echo "seek -10" > /home/pi/Desktop/Lab1/my_fifo'
	print subprocess.check_output(cmd,shell=True)   # Run the command with subprocess, first check whether commend is exist  and correct, then if yes return, else raise error flag
def GPIO26_callback(channel):
    print "falling edge detected on 26"
    cmd = 'echo "seek 30" > /home/pi/Desktop/Lab1/my_fifo'
	print subprocess.check_output(cmd,shell=True)   # Run the command with subprocess, first check whether commend is exist  and correct, then if yes return, else raise error flag
def GPIO5_callback(channel):
    print "falling edge detected on 05"
    cmd = 'echo "seek -30" > /home/pi/Desktop/Lab1/my_fifo'
	print subprocess.check_output(cmd,shell=True)   # Run the command with subprocess, first check whether commend is exist  and correct, then if yes return, else raise error flag

# Add event detection
GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback, bouncetime=300) 
GPIO.add_event_detect(22, GPIO.FALLING, callback=GPIO22_callback, bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=GPIO23_callback, bouncetime=300) 
GPIO.add_event_detect(26, GPIO.FALLING, callback=GPIO26_callback, bouncetime=300)
GPIO.add_event_detect(05, GPIO.FALLING, callback=GPIO06_callback, bouncetime=300) 

# Wait for quit command
try:
    GPIO.wait_for_edge(27, GPIO.FALLING) 
    print "falling edge detected on 27"
    cmd = 'echo "quit" > /home/pi/Desktop/Lab1/my_fifo'
    print subprocess.check_output(cmd,shell=True) # quit mplayer
except KeyboardInterrupt:
    GPIO.cleanup() # keyboard interrupt
GPIO.cleanup() # normal clean up
