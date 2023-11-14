
import jetFunctions as j
directionPin = 27
enablePin = 22
stepPin = 17
j.initSpiAdc()
j.initStepMotorGpio()
try:
    data = []
    print('введите необходимое количество шагов')
    kolich = input()  
    steps = 0
    while(steps < int(kolich)):
        steps = steps + 1
        j.time.sleep(0.01)
        if (steps <= int(kolich) / 2):
            j.stepForward(2)
            sum = j. getAdc() 
            data.append(sum)
        else:
            j.stepBackward(2)    

    print(data)
    datastr=[str(item) for item in data]
    with open('gusenichka.txt','w') as outfile:
        outfile.write('\n'.join(datastr))
finally:
    j.deinitSpiAdc()
    j.deinitStepMotorGpio()

