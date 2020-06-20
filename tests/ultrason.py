import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18

print ("Test en cours")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,False)
print("Attente de l'envoi au capteur")
time.sleep(2)

GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,False)

while GPIO.input(ECHO) == 0: 
	pulse_start = time.time()

while GPIO.input(ECHO) == 1:
	pulse_end = time.time()

pulse_duration = pulse_end - pulse_start


print("duration",pulse_duration)

distance = pulse_duration * 17150
distance = round(distance,2)

print("Distance : ",distance," cm")

GPIO.cleanup()
