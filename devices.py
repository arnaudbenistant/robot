#!/usr/bin/env python3
import asyncio
import RPi.GPIO as GPIO
import time
import sysutils
from threading import Thread, RLock
from evdev import InputDevice, categorize, ecodes

#Define Button Mappin
BTN_SELECT = 314
BTN_ZL = 308
BTN_ZR = 309
BTN_WEST = 306
BTN_NORTH = 307
BTN_EAST = 305
BTN_SOUTH = 304
BTN_UPDOWN = 17
BTN_LEFTRIGHT = 16
BTN_HOME = 317
#EVENT_TYPE_VALUE
KEY_UP = 0
KEY_DOWN = 1
KEY_HOLD = 2

#GPIO
GREEN_LIGHT = 33
RED_LIGHT = 37
BLUE_LIGHT = 35

#Define GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GREEN_LIGHT,GPIO.OUT)
GPIO.setup(RED_LIGHT,GPIO.OUT)
GPIO.setup(BLUE_LIGHT,GPIO.OUT)

global display_status
display_status = 0
verrou = RLock()

def west_pressed(value):
    #print("WEST")
    turn_light(GREEN_LIGHT,value)
    turn_light(RED_LIGHT,value)
    turn_light(BLUE_LIGHT,value)
    
def north_pressed(value):
    #print("NORTH")
    turn_light(GREEN_LIGHT,value)
    
def south_pressed(value):
    #print("SOUTH")
    turn_light(BLUE_LIGHT,value)
    
def east_pressed(value):
    #print("EAST")
    turn_light(RED_LIGHT,value)
    
def display(text):
    print(text)
    
def changeDisplayStatus(var):
    with verrou :
        global display_status
        display_status=var;
       
    
def home_pressed(value):
    if (display_status == 0):
        if(value == KEY_HOLD):    
            changeDisplayStatus(1)
            display("Wifi : "+sysutils.getIp())
            time.sleep(1)
            display("CPU T° : "+str(sysutils.getTemp())+"° C")
            time.sleep(1)
    if(value == KEY_UP):
       changeDisplayStatus(0)
       
    
def turn_light(light,event_value):
    #print("turn ",light," code ",event_value)
    if(event_value == KEY_DOWN):
        GPIO.output(light,GPIO.HIGH)
    if(event_value == KEY_UP):
        GPIO.output(light,GPIO.LOW)

def exitlight():
    GPIO.output(BLUE_LIGHT,GPIO.LOW)
    GPIO.output(RED_LIGHT,GPIO.LOW)
    GPIO.output(GREEN_LIGHT,GPIO.LOW)
    GPIO.cleanup()
    print("\nEnd of program\n")
    return

async def helper(dev):
    async for ev in dev.async_read_loop():
        #print(ev.code)
        if(ev.code == BTN_EAST):
            east_pressed(ev.value)
        elif(ev.code == BTN_NORTH):                
            north_pressed(ev.value)
        elif(ev.code == BTN_SOUTH):                
            south_pressed(ev.value)
        elif(ev.code == BTN_WEST):                
            west_pressed(ev.value)
        elif(ev.code == BTN_HOME):
            home_pressed(ev.value)
        

joycon = InputDevice('/dev/input/event5')
print(joycon)
try:
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(helper(joycon))
except KeyboardInterrupt:
    exitlight()