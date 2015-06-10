import Adafruit_BBIO.GPIO as GPIO
import Adafruit_DHT
import time

# LED initialize
LED = "P8_12"

GPIO.setup(LED, GPIO.OUT)

try:
    while (True):
        GPIO.output(LED, GPIO.HIGH)

        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, "P9_11")

        if humidity is not None:
            print "Read humidity = {0:0.1f}%  //  temperature = {1:0.1f}C".format(humidity, temperature)
        else:
            print "Can't read humidity!"

        GPIO.output(LED, GPIO.LOW)

        time.sleep(0.1)



except KeyboardInterrupt:
    GPIO.output(LED, GPIO.LOW)
    GPIO.cleanup()