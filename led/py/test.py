import mraa
import time

LED_PIN_1 = 4
LED_PIN_2 = 5
LED_PIN_3 = 6

LED1 = mraa.Gpio(LED_PIN_1)
LED1.dir(mraa.DIR_OUT)

LED2 = mraa.Gpio(LED_PIN_2)
LED2.dir(mraa.DIR_OUT)

LED3 = mraa.Gpio(LED_PIN_3)
LED3.dir(mraa.DIR_OUT)

try:
    while (True):
        LED1.write(1)
        LED2.write(0)
        LED3.write(0)
        time.sleep(0.1)

        LED1.write(0)
        LED2.write(1)
        LED3.write(0)
        time.sleep(0.1)

        LED1.write(0)
        LED2.write(0)
        LED3.write(1)
        time.sleep(0.1)

except KeyboardInterrupt:
    LED1.write(0)
    LED2.write(0)
    LED3.write(0)