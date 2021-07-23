import machine
import time

#   These define which pin you are using on your Lopy4
#   I suggest you open their documentation and check what you can and cannot use before doing any changes.
adc = machine.ADC()
MoisturePin = adc.channel(pin='P16')
TempPin = adc.channel(pin='P20')

#   These are the values to change if you want to adjust the moisture threshold yourself.
thresholdUp = 400
thresholdDown = 250

while True:
    moisture = MoisturePin()
    millivoltsTemp = TempPin.voltage()
    drynessStatus = False

    celsius = (millivoltsTemp - 500.0) / 10.0                       #   Equation to calculate Celsius from millivolts
    round(celsius, 3)                                               #   Do the rounding to only 3 digits

    celsiustext = "The temperature is {} Celsius.".format(celsius)  #   Build the string in question

    if moisture <= thresholdDown:
        print("The plant is dry!")
        print(moisture)
        drynessStatus = True

    if moisture >= thresholdUp:
        print("The plant is wet!")
        print(moisture)

    #   Send result to PyBytes.
    if drynessStatus == True and celsius <= 30:
        print("The plant is ready to be watered.")
        pybytes.send_signal(3, "The plant is dry, water it NOW!")
        pybytes.send_signal(1, celsiustext)
        print("sending: {}".format(celsiustext))

    #   This number decides how often you will receive a status report on Discord.
    #   In this case you will receive notice every 15 minutes.
    time.sleep(900)
