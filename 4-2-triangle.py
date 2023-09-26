import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
def decimal2binary (value):
     return [int(element) for element in bin(value)[2:].zfill(8)]
try: 
    while(1):
     T=int(input('период='))
     N=int(input('количество повторов='))
     i=0
     for j in range(N):
         while i<255:
             GPIO.output(dac,decimal2binary (int(i)))
             i= i+1
             time.sleep(T/512)
         while i>0:
             GPIO.output(dac,decimal2binary (int(i)))
             i= i-1
             time.sleep(T/512)    
             
     
     
finally:     GPIO.output(dac,0)    