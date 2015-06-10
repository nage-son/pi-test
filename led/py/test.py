import RPi.GPIO as GPIO
import time

LED1 = 18
# LED2 = "P8_16"
# LED3 = "P8_18"

# GPIO.setup(LED1, GPIO.OUT)
# GPIO.setup(LED2, GPIO.OUT)
# GPIO.setup(LED3, GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)

try:
    while (True):
        GPIO.output(LED1, True)
        # GPIO.output(LED2, GPIO.LOW)
        # GPIO.output(LED3, GPIO.LOW)
        # time.sleep(0.1)

        # GPIO.output(LED1, GPIO.LOW)
        # GPIO.output(LED2, GPIO.HIGH)
        # GPIO.output(LED3, GPIO.LOW)
        # time.sleep(0.1)

        # GPIO.output(LED1, GPIO.LOW)
        # GPIO.output(LED2, GPIO.LOW)
        # GPIO.output(LED3, GPIO.HIGH)

        time.sleep(0.1)

        GPIO.output(LED1, False)

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.output(LED1, False)
    # GPIO.output(LED2, GPIO.LOW)
    # GPIO.output(LED3, GPIO.LOW)
    GPIO.cleanup()