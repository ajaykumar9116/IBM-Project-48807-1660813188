#1.write a program to blink LED using while loop
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
while True:
    GPIO.output(8,True)
    print("LED IS ON")
    time.sleep(1)
    GPIO.output(8,False)
    print("LED IS OFF")
    time.sleep(1)
    
    