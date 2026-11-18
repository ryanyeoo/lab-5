from time import sleep
from hal import hal_adc as adc
from hal import hal_servo as servo


def main():
    # Call each init function once
    adc.init()
    servo.init()

    while True:
        value = adc.get_adc_value(1)          # potentiometer, 0 to 1023
        angle = 180 - (value * 180 / 1023)    # ADC 0 -> 180 deg, ADC 1023 -> 0 deg
        print(value, angle)
        servo.set_servo_position(angle)
        sleep(0.1)


# Main entry point
if __name__ == "__main__":
    main()