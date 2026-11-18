from hal import hal_adc as adc
from time import sleep

adc.init()
while True:
    print(adc.get_adc_value(1))   # potentiometer
    sleep(0.5)