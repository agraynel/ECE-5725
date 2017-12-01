# Lab 3 10/04/2017
# Yi Chen yc2329
# Mingda Yang my432

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...

GPIO.setup(12, GPIO.OUT) # Set GPIO 12 as output
p1 = GPIO.PWM(12,50)

#Set duty cycle for clockwise 10 speed steps
dc = 7.5
p1.start(dc)
time.sleep(2)
print("Clock wise\n")
while dc>6.6:
    dc = dc - 0.1
    print('Now step time is: %f ms, clockwise incrementing\n'%(dc))
    p1.ChangeDutyCycle(dc)
    time.sleep(3)

#Set duty cycle for counter clockwise 10 speed steps
dc = 7.5
print("counter clock wise\n")
while dc<8.4:
    dc = dc+0.1
    print('Now step time is: %f ms, counter clockwise incrementing\n'%(dc))
    p1.ChangeDutyCycle(dc)
    time.sleep(3)
    
p1.stop()
