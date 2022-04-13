import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 440)
pwm.start(100)
time.sleep(2)
pwm.stop()

GPIO.cleanup()
