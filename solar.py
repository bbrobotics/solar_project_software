import RPi.GPIO as GPIO
import time

#sunrise and sunset are lists of the average time in hours since midnight for sunrise and sunset for each month in the local testing environment.
def sunrise = [7.17, 6.72, 5.93, 5.08, 4.42, 4.16, 4.38, 4.88, 5.43, 6.03, 6.65, 7.13]
def sunset = [16.67, 17,27, 17.88, 18.49, 19.05, 19.41, 19.33, 18.76, 17.92, 17.05, 16.42, 16.27]

def openAngle = 15 #Angle in degrees to which the solar tracker is already open.  15 degrees is not verified and is a placeholder.

def setMotor(motor, outputPercent): #motor is a pwm instance
	if -1 <= outputPercent || outputPercent <= 1:
		outputAdded = outputPercent * 5
		output = 15 + outputPercent
		motor.ChangeDutyCycle(output)
	else:
		print("Error, outputPercent out of range.")

#Returns the sunrise time in hours since midnight.
def getSunriseTime():
	month = int(time.strftime("%m")) - 1
	return sunrise[month]

#Returns the sunset time in hours since midnight.
def getSunsetTime():
	month = int(time.strftime("%m")) - 1
	return sunset[month]

def getCurrentTime():
	#placeholder

def rotateToAngle(motor, encoder, angle):
	#placeholder

def solarTrack():
	startAngle = 180 - 15 * ((getSunsetTime() - getSunriseTime()) / 2)
	currentAngle = startAngle + 15 * (getCurrentTime() - getSunriseTime())
	setAngle = currentAngle + 180 - openAngle
	#rotateToAngle(motor, encoder, setAngle) #placeholder, as the motor and encoder objects are not yet established.

GPIO.setmode(GPIO.BCM)
LED1 = 18
Servo = 23

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(Servo, GPIO.OUT)

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
