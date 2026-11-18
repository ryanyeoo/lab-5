from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import led_control

lcd = LCD.lcd()


def show_status(line2):
    lcd.lcd_clear()
    lcd.lcd_display_string("LED Control", 1)
    lcd.lcd_display_string(line2, 2)


# Callback function invoked when any key on keypad is pressed
def key_pressed(key):
    print(key)

    if key == 1:                    # REQ-02
        led_control.delay = 1
        show_status("Blink LED")
    elif key == 0:                  # REQ-03
        led_control.delay = 0
        show_status("OFF LED")
    # REQ-04: any other key does nothing


def main():
    # REQ-01: initial display, LED off
    show_status("0:Off 1:Blink")

    # Initialize the HAL keypad driver
    keypad.init(key_pressed)

    # Keypad scanning runs forever in its own thread
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

    led_control.led_control_init()


# Main entry point
if __name__ == "__main__":
    main()