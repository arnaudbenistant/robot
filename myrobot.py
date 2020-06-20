#!/usr/bin/env python3
import asyncio
import time
import servo
from threading import Thread, RLock
from evdev import InputDevice, categorize, ecodes

#Define Button Mapping
BTN_UPDOWN = 17
BTN_UPDOWN_UP = -1
BTN_UPDOWN_RELEASED = 0
BTN_UPDOWN_DOWN = 1

BTN_LR = 16
BTN_LR_L = -1
BTN_LR_R = 1
BTN_LR_RELEASED = 0

#Define current robot direction
AVANT = -1
ARRIERE = 1
ARRET = 0
DIRECTION = 0

#Define Bluetooth Settings ####
joycon = InputDevice('/dev/input/event5')
print(joycon)

# Exit process and free GPIO and stuff like that
def exitbl():
    servo.guidageStop() 
    print("Fin")
    return

# With a given event provided by bluetooth joycon, define robot behaviour
async def helper(dev):
    async for ev in dev.async_read_loop():
        #print(str(ev.code)+" - "+str(ev.value))

        if(ev.code == BTN_UPDOWN):
            if(ev.value == BTN_UPDOWN_UP):
                DIRECTION = AVANT  
                servo.avancer()
            if(ev.value == BTN_UPDOWN_RELEASED):
                DIRECTION = ARRET 
                servo.stop()
            if(ev.value == BTN_UPDOWN_DOWN):
                DIRECTION = ARRIERE 
                servo.reculer()
                
        if(ev.code == BTN_LR):
            if(ev.value == BTN_LR_L):
                if (DIRECTION == ARRIERE):
                    servo.tournerDroite()
                else:
                    servo.tournerGauche()
            if(ev.value == BTN_LR_RELEASED):
                if (DIRECTION == AVANT):
                    servo.avancer()
                elif (DIRECTION == ARRIERE):
                    servo.reculer()
                else:
                    servo.stop() 
            if(ev.value == BTN_LR_R):
                if (DIRECTION == ARRIERE):
                    servo.tournerGauche()
                else:
                    servo.tournerDroite()


# Launch main program of my robot :)        
try:
    # Start RFID Management
    # TODO

    # Start display Management
    # TODO

    # Start Motors management
        servo.guidageStart() 

    # Start Video Management
    # TODO
 
    # Launch Thread to capture joycon events 
        loop = asyncio.get_event_loop()

    # Capture events from the joycon 
        loop.run_until_complete(helper(joycon))
except KeyboardInterrupt:
    exitbl()
