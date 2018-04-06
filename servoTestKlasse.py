import RPi.GPIO as GPIO
from time import sleep

class Servo:

	"""docstring for ClassName"""
	def __init__(self, pin=12, freq=50):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin,freq)
        
        self.angle = 0


def setAngle(angle):
	duty = angle/18+2
	GPIO.output(self.pin,True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(12, False)
    pwm.ChangeDutyCycle(0)

def oneGo(self):
	self.start(0)
	setAngle(180)
	setAngle(0)
	pwm.stop()
 

pwm.stop()
GPIO.cleanup()

