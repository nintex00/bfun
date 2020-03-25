import Adafruit_BBIO.ADC as ADC
ADC.setup()
from time import sleep
analogPin="P9_33"
while(1):
	potVal = 1.8*ADC.read(analogPin)
	print("The Potentiometer Value is: " +str( potVal))
	sleep(0.5)

