import jetFunctions as j
directionPin = 27
enablePin = 22
stepPin = 17
j.initSpiAdc()
j.initStepMotorGpio()
n = 0
while (n < 100):
    n = n+1
    print(j.getAdc())
    j.time.sleep(0.5)
