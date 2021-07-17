import machine
import time

adc = machine.ADC()
MoisturePin = adc.channel(pin='P16')
TempPin = adc.channel(pin='P20')

thresholdUp = 400
thresholdDown = 250

while True:
    moisture = MoisturePin()
    millivoltsTemp = TempPin.voltage()

    if moisture <= thresholdDown:
        print("Dry, Water it!")
        print(moisture)

    if moisture >= thresholdUp:
        print("Wet, Leave it!")
        print(moisture)

    celsius = (millivoltsTemp - 500.0) / 10.0
    print("The temperature is ", celsius, "Celsius")

    time.sleep(1)
