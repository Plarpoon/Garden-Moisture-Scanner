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
    drynessStatus = False

    celsius = (millivoltsTemp - 500.0) / 10.0
    print("The temperature is ", celsius, "Celsius")

    if moisture <= thresholdDown:
        print("The plant is dry!")
        print(moisture)
        drynessStatus = True

        # Send plant moisture status to Pybytes
        pybytes.send_signal(2, "The Plant is Dry!")

    if moisture >= thresholdUp:
        print("The plant is wet!")
        print(moisture)

        # Send plant moisture status to Pybytes
        pybytes.send_signal(2, "The Plant is Wet!")

    if drynessStatus == True and celsius < 30:
        print("The plant is ready to be watered.")
        pybytes.send_signal(3, "Water it NOW!")
        pybytes.send_signal(1, celsius)
        print("sending: {}".format(celsius))

    time.sleep(10)
