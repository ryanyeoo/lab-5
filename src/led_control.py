from hal import hal_led as led
from threading import Thread
from time import sleep

delay = 0  # 0 = LED off, 1 = blink every 1 second


def led_thread():
    while True:
        if delay != 0:
            led.set_output(20, 1)
            sleep(delay)
            led.set_output(20, 0)
            sleep(delay)
        else:
            led.set_output(20, 0)   # make sure LED is off
            sleep(0.1)


def led_control_init():
    led.init()
    t1 = Thread(target=led_thread, daemon=True)
    t1.start()