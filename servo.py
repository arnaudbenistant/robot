#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
GPIO.setwarnings(False) #Disable warnings

pwm_gpio_g = 11
pwm_gpio_d = 7

frequence = 50
GPIO.setup(pwm_gpio_g,GPIO.OUT)
GPIO.setup(pwm_gpio_d,GPIO.OUT)

pwm_g = GPIO.PWM(pwm_gpio_g,frequence)
pwm_d = GPIO.PWM(pwm_gpio_d,frequence)

#Define properties
AVANT=1
VITE=2

#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent
    # 0,0472222
    angle_as_percent = angle * ratio

    return start + angle_as_percent

def moteurG(code):
    pwm_g.start(code)

def moteurD(code):
    pwm_d.start(code)

def stop():
    moteurG(100)
    moteurD(100)

def avancer():
    moteurG(1)
    moteurD(10)

def reculer():
    moteurG(10)
    moteurD(1)
    
def tournerGauche():
    moteurG(1)
    moteurD(1)
    
def tournerDroite():
    moteurG(10)
    moteurD(10)
    
def guidageStart():
    print("GOOOO")

def guidageStop():
    pwm_g.stop()
    pwm_d.stop()
    GPIO.cleanup()
    
