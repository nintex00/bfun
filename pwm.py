import Adafruit_BBIO.PWM as PWM
myPWM = "P8_13"
PWM.start(myPWM, 0, 1000)

for i in range(0,5):
    V = input("What voltage would you like? ")
    DC = (V/3.365)*100
    
    if DC > 100:
        DC=100
    PWM.set_duty_cycle(myPWM, DC)
    PWM.set_frequency(myPWM, 100)
PWM.stop(myPWM)
PWM.cleanup()

