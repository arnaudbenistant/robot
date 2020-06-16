import RPi.GPIO as GPIO
import time

BLUELIGHT = 12
REDLIGHT = 37
GREENLIGHT = 35
BUTTON = 16
EXIT_BUTTON = 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#Lights
GPIO.setup(BLUELIGHT,GPIO.OUT)
GPIO.setup(REDLIGHT,GPIO.OUT)
GPIO.setup(GREENLIGHT,GPIO.OUT)
#Buttons
GPIO.setup(BUTTON,GPIO.IN)
GPIO.setup(EXIT_BUTTON,GPIO.IN)

mode_auto = 0
last_button_statement = 0

def initlight():
    print("Hello world")
    #Welcome process
    i = 0
    GPIO.output(BLUELIGHT,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(REDLIGHT,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GREENLIGHT,GPIO.HIGH)
    time.sleep(1)
    while i<5:
        GPIO.output(REDLIGHT,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(GREENLIGHT,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(REDLIGHT,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(GREENLIGHT,GPIO.HIGH)
        time.sleep(0.1)
        i=i+1
    #End of welcome process  
    GPIO.output(REDLIGHT,GPIO.LOW)
    GPIO.output(GREENLIGHT,GPIO.LOW)
    GPIO.output(BLUELIGHT,GPIO.LOW)    
    print("Ready")
    
def exitlight():
    GPIO.output(BLUELIGHT,GPIO.LOW)
    GPIO.output(REDLIGHT,GPIO.LOW)
    GPIO.output(GREENLIGHT,GPIO.LOW)
    GPIO.cleanup()
    prin("\nEnd of program\n")
    return

try:
    initlight()
    while True: 
        button_state = GPIO.input(BUTTON)
        exit_button_state = GPIO.input(EXIT_BUTTON)
        
        #Affichage vert et rouge pendant l'appuye
        if button_state==1:
            print("Button")
            GPIO.output(GREENLIGHT,GPIO.HIGH)
            GPIO.output(REDLIGHT,GPIO.HIGH)
        else:
            GPIO.output(GREENLIGHT,GPIO.LOW)
            GPIO.output(REDLIGHT,GPIO.LOW)
        
        if button_state==1 and last_button_statement !=1:
            if mode_auto == 1:
                mode_auto = 0
                print("No Auto")                
            else:
                mode_auto = 1
                print("Auto")                
        
        last_button_statement=button_state
        
        if mode_auto==1 :
            GPIO.output(GREENLIGHT,GPIO.HIGH)
            GPIO.output(REDLIGHT,GPIO.LOW)
            GPIO.output(BLUELIGHT,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(BLUELIGHT,GPIO.LOW)
            time.sleep(1)
            
        if mode_auto==0 :
            GPIO.output(GREENLIGHT,GPIO.LOW)
            GPIO.output(REDLIGHT,GPIO.HIGH)
            
        if exit_button_state == 1 :
            exitlight()
            
except KeyboardInterrupt:
    exitlight()
        

    
