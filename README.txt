Welcome to the solar project software package.
This contains all the software needed to run the solar tracker.
All programs are writted in python and must be run as root.

Minimum System Requirements:
Raspberry Pi
Python 2.7
RPi.GPIO library

calibrate.py:
The program 'calibrate.py' is designed to be used to calibrate a motor controller for use with this system.
To use this program, connect the motor controller to the raspberry pi with GPIO pin 23 as the pwm channel pin,
hold down the calibrate button on the motor controller, and run the program by typing into your command line:
'sudo python calibrate.py' 

