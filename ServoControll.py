import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p= GPIO.PWM(12,50)
p.start(0)

def setAngle(angle):
duty=angle/18+2
GPIO.output(12,True)
p.changeDutyCycle(duty)
sleep(1)
GPIO.output(12,False)
p.changeDutyCycle(0)

setAngle(180)
setAngle(0)

p.stop()
GPIO.cleanup()