import time
from threading import Thread
from hal import hal_lcd as LCD

lcd = LCD.lcd()


def clock_thread():
    colon = True
    while True:
        local_time = time.localtime()

        sep = ":" if colon else " "
        time_string = time.strftime("%H", local_time) + sep + \
                      time.strftime("%M", local_time) + sep + \
                      time.strftime("%S", local_time)
        date_string = time.strftime("%d:%m:%Y", local_time)   # date colons never blink

        lcd.lcd_display_string(time_string, 1)
        lcd.lcd_display_string(date_string, 2)

        colon = not colon
        time.sleep(1)


def main():
    lcd.lcd_clear()
    t = Thread(target=clock_thread, daemon=True)
    t.start()

    # Keep the main thread alive so Ctrl+C works
    while True:
        time.sleep(1)


# Main entry point
if __name__ == "__main__":
    main()