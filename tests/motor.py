import RPi.GPIO as GPIO
import time


REDLIGHT = 37
GREENLIGHT = 35
MOTOR = 38
P_SERVO = MOTOR
BUTTON = 16

fPWM = 50


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Lights
GPIO.setup(REDLIGHT,GPIO.OUT)
GPIO.setup(GREENLIGHT,GPIO.OUT)

#Motors
GPIO.setup(MOTOR,GPIO.OUT)

opened = 1
closed = 0
status = closed

def init_door():
    print("Hello world")
   
def rotate_up():
    a=10
    b=2
    direction=50
    time.sleep(0.5)
    #GPIO.output(MOTOR,GPIO.HIGH)
    pwm = GPIO.PWM(P_SERVO, fPWM)
    pwm.start(0)
    duty = a / 180 * direction + b
    pwm.ChangeDutyCycle(duty)
    print ("direction =", direction, "-> duty =", duty)
    
    time.sleep(5)
    GPIO.output(MOTOR,GPIO.LOW)
    
def rotate_down():
    time.sleep(0.5)
    GPIO.output(MOTOR,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(MOTOR,GPIO.LOW)
    
def exit_door():    
    GPIO.output(REDLIGHT,GPIO.LOW)
    GPIO.output(GREENLIGHT,GPIO.LOW)
    GPIO.output(MOTOR,GPIO.LOW)
    GPIO.cleanup()
    print("\nEnd of program\n")
    return

def close_door():
    status=closed
    GPIO.output(REDLIGHT,GPIO.HIGH)
    GPIO.output(GREENLIGHT,GPIO.LOW)
    rotate_down()
    
def open_door():
    status=opened
    GPIO.output(REDLIGHT,GPIO.LOW)
    GPIO.output(GREENLIGHT,GPIO.HIGH)
    rotate_up()


try:
    init_door()
    while True: 
        open_door()
        time.sleep(1)
        close_door()
        time.sleep(1)
            
except KeyboardInterrupt:
    exit_door()
        

    
