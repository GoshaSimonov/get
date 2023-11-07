import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
try:
    while(1):
        x=input('percent=')
        print('v=',3.3*int(x)/100)
        p=GPIO.PWM(21, 1000)
        p.start(int(x))
        input('press ruturn to stop')
        p.stop()
        GPIO.cleanup
finally:    GPIO.cleanup