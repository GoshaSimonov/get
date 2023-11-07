import RPi.GPIO as GPIO
import time
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
    while 1:
     value=adc()   
     voltage=3.3/2**8*value
     print("value=",value,'signal=',decimal2binary (value),'V=',voltage)
     if value>=32*8:
         GPIO.output(leds,[1,1,1,1,1,1,1,1])
     elif value>=32*7:
         GPIO.output(leds,[0,1,1,1,1,1,1,1])
     elif value>=32*6:
         GPIO.output(leds,[0,0,1,1,1,1,1,1])
     elif value>=32*5:
         GPIO.output(leds,[0,0,0,1,1,1,1,1])
     elif value>=32*4:
         GPIO.output(leds,[0,0,0,0,1,1,1,1])
     elif value>=32*3:
         GPIO.output(leds,[0,0,0,0,0,1,1,1])
     elif value>=32*2:
         GPIO.output(leds,[0,0,0,0,0,0,1,1])
     elif value>=32:
         GPIO.output(leds,[0,0,0,0,0,0,0,1])
     else:  
         GPIO.output(leds,[0,0,0,0,0,0,0,0]) 
finally:
   GPIO.output(dac, 0)
   GPIO.output(troyka, 0)
   GPIO.cleanup() 