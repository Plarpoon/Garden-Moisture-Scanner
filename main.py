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

    celsius = (millivoltsTemp - 500.0) / 10.0
    print("The temperature is ", celsius, "Celsius")

    if moisture <= thresholdDown:
        print("Dry, Water it!")
        print(moisture)

        # Send plant moisture status to Pybytes
        pybytes.send_signal(2, "The Plant is Dry! Water it!")

    if moisture >= thresholdUp:
        print("Wet, Leave it!")
        print(moisture)

        # Send plant moisture status to Pybytes
        pybytes.send_signal(2, "The Plant is Wet! Leave it!")

    # Send temperature data to Pybytes.
    pybytes.send_signal(1, celsius)
    print("sending: {}".format(celsius))

    time.sleep(10)
