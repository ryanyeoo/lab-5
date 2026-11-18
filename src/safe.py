from time import sleep
from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_buzzer as buzzer

CORRECT_PIN = [1, 2, 3, 4]

lcd = LCD.lcd()
entered = []      # digits typed so far
attempts = 0      # number of wrong PINs
locked = False    # True after unlock or disable, so keys are ignored


def show_prompt():                       # REQ-01 (and REQ-02 asterisks)
    lcd.lcd_clear()
    lcd.lcd_display_string("Safe Lock", 1)
    lcd.lcd_display_string("Enter PIN: " + "*" * len(entered), 2)


def show_message(line1):                 # line 2 stays blank
    lcd.lcd_clear()
    lcd.lcd_display_string(line1, 1)


def key_pressed(key):
    global entered, attempts, locked

    if locked:
        return
    if not isinstance(key, int):         # '*' and '#' are ignored
        return

    entered.append(key)
    show_prompt()

    if len(entered) < 4:
        return

    # Check the PIN after the 4th digit
    if entered == CORRECT_PIN:           # REQ-03
        show_message("Safe Unlocked")
        locked = True
        return

    attempts += 1
    entered = []

    if attempts >= 3:                    # REQ-05
        show_message("Safe Disabled")
        locked = True
    else:                                # REQ-04
        show_message("Wrong PIN")
        buzzer.turn_on_with_timer(1)     # buzzer on for 1 second
        sleep(2)
        show_prompt()


def main():
    buzzer.init()
    keypad.init(key_pressed)
    show_prompt()

    keypad_thread = Thread(target=keypad.get_key, daemon=True)
    keypad_thread.start()

    while True:                          # keep main alive so Ctrl+C works
        sleep(1)


# Main entry point
if __name__ == "__main__":
    main()