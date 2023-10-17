import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
comp = 14
leds=[2,3,4,17,27,22,10,9]
troyka= 13
GPIO.setup(troyka,GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
def decimal2binary (value):
     return [int(element) for element in bin(value)[2:].zfill(8)]
  
def adc ():
    itog =0
    perem=0  
    for i in range(8):
            p2=2**(8-i-1)
            perem= itog +p2
            signal=decimal2binary (perem)
            GPIO.output(dac,signal)
            time.sleep(0.06)
            comparatorval=GPIO.input(comp)
            if comparatorval == 0:
             itog = perem
    return itog
try:
    znach=[]
    startt=time.time()
    while (adc()<207):
     pstart=time.time()   
     value=adc()  
     znach.append(value) 
     voltage=3.3/2**8*value
     print("value=",value,'signal=',decimal2binary (value),'V=',voltage)
     GPIO.output(leds,decimal2binary (value))
     pend=time.time()
    znach.append(207) 
    print("value=",207,'signal=',decimal2binary (207),'V=',3.3/2**8*207)
    GPIO.output(troyka,0)
    while(adc()>168):
     value=adc()  
     znach.append(value) 
     voltage=3.3/2**8*value
     print("value=",value,'signal=',decimal2binary (value),'V=',voltage)
     GPIO.output(leds,decimal2binary (value))
    znach.append(168)
    print("value=",168,'signal=',decimal2binary (168),'V=',3.3/2**8*168)
    endt=time.time()
    vsetime=endt-startt
    print ('time=',endt-startt, "с")
    period= vsetime/ len(znach)
    print('period=',period,"с")
    chast=len(znach)/vsetime
    print('chastota=',chast,"гц")
    kvant=(3.3/256)
    print('shagkvant=',kvant,"В")
    plt.plot(znach)
    plt.show()
    znachstr=[str(item) for item in znach]
    with open('Boris.txt','w') as outfile:
        outfile.write('\n'.join(znachstr))
    with open('settings.txt','w') as outfile:
        outfile.write('time='+str(endt-startt)+'c ')
        outfile.write('period='+str(period)+'c ')
        outfile.write('chastota='+str(chast)+'гц ')
        outfile.write('shagkvant='+str(kvant)+"В ")  

finally:
   GPIO.output(dac, 0)
   GPIO.output(troyka, 0)
   GPIO.cleanup() 