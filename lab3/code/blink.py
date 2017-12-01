# Lab 3 10/04/2017
# Yi Chen yc2329
# Mingda Yang my432

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...
GPIO.setup(12, GPIO.OUT) # Set GPIO 12 as output

p = GPIO.PWM(12,50)		# channel & frequency

p.start(7.5)			# duty cycle

time.sleep(10)
p.stop()


