import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
comp = 14
troyka= 13
GPIO.setup(troyka,GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def decimal2binary (value):
     return [int(element) for element in bin(value)[2:].zfill(8)]
def adc ():
     for value in range(256):
            signal=decimal2binary (value)
            GPIO.output(dac,signal)
            time.sleep(0.005)
            comparatorval=GPIO.input(comp)
            if comparatorval == 1:
                return value
                break
try:
    while 1:
     value=adc()   
     voltage=3.3/2**8*value
     print("value=",value,'signal=',decimal2binary (value),'V=',voltage)
     
finally:
   GPIO.output(dac, 0)
   GPIO.output(troyka, 0)
   GPIO.cleanup() 
