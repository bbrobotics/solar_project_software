import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED1 = 18
Servo = 23

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(Servo, GPIO.OUT)

def setMotor(motor, outputPercent): #motor is a pwm instance
	if -1 <= outputPercent || outputPercent <= 1:
		outputAdded = outputPercent * 5
		output = 15 + outputPercent
		motor.ChangeDutyCycle(output)
	else:
		print("Error, outputPercent out of range.")

p = GPIO.PWM(Servo, 100) #Creates a new pwm instance with the channel 25 (Servo) 
			 #and the frequency 1000 Hz.

p.start(15) #Starts the pmw instance with a duty cycle of 1.5 percent.
time.sleep(1)
p.ChangeDutyCycle(10) #8.7
time.sleep(1)
p.ChangeDutyCycle(15)
time.sleep(1)
p.ChangeDutyCycle(20)
time.sleep(1)
p.ChangeDutyCycle(15)
time.sleep(1)
p.stop()

GPIO.output(LED1, True)

time.sleep(1)

GPIO.output(LED1, False)
GPIO.cleanup()
