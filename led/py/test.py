import RPi.GPIO as GPIO
import time

LED1 = 25
LED2 = 24
LED3 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

try:
    while (True):
        GPIO.output(LED1, True)
        GPIO.output(LED2, False)
        GPIO.output(LED3, False)
        time.sleep(0.1)

        GPIO.output(LED1, False)
        GPIO.output(LED2, True)
        GPIO.output(LED3, False)
        time.sleep(0.1)

        GPIO.output(LED1, False)
        GPIO.output(LED2, False)
        GPIO.output(LED3, True)

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.output(LED1, False)
    GPIO.output(LED2, False)
    GPIO.output(LED3, False)
    GPIO.cleanup()