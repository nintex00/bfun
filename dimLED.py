import Adafruit_BBIO.PWM as PWM
tLED="P9_16"
bLED="P9_22"
PWM.start(tLED,0,1000)
PWM.start(bLED,0,1000)
for i in range(0,5):
    tB=input("Brightness Top LED? (0-7) ")
    bB=input("Brightness Bottom LED? (0-7) ")
    tBDC=2**tB
    bBDC=2**bB
    if tBDC>100:
        tBDC=100
    if bBDC>100:
        bBDC=100
    PWM.set_duty_cycle(tLED, tBDC)
    PWM.set_duty_cycle(bLED, bBDC)
PWM.stop(tLED)
PWM.stop(bLED)
PWM.cleanup()

