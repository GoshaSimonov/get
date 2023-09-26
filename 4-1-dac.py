import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
def decimal2binary (value):
     return [int(element) for element in bin(value)[2:].zfill(8)]
try: 
    while(1):
     print("введите число от 0 до 255")
     n=input()
     
     if n.isdigit() is False:
        print('ошибка не подходит') 
        n = 0
     elif (int(n)>255):
         print('ошибка превышения') 
         n = 0         
     else: 
         n=int(n)
     GPIO.output(dac,decimal2binary (n))
     print('v=',3.3/2**8*n)


finally:     GPIO.output(dac,0)    