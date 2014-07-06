#This program is designed to be used to calibrate a motor controller for use with the solar tracker.
#Hold the calibrate button and then run this program to calibrate your controller.
#This will calibrate motor controller to set the minimum input period to 1 millisecond and
	#to sent the maximum input period to 2 milliseconds. 
#This program must be run as root.

import RPi.GPIO as GPIO
import time

Servo = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(Servo, GPIO.OUT)

p = GPIO.PWM(Servo, 100) #Creates a new pwm instance with the channel 23 (Servo) 
			 #and the frequency 100 Hz.

p.start(10) #Starts the pmw instance with a duty cycle of 10 percent (1 ms pulse).
time.sleep(1)
p.ChangeDutyCycle(20) #Sets the duty cycle to the maximum of 20 percent (2 ms pulse).
time.sleep(1)
p.ChangeDutyCycle(15) #Sets the duty cycle to the midpoint of 15 percent (1.5 ms pulse).
time.sleep(1)
p.stop()
GPIO.cleanup()
