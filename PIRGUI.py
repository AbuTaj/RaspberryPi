'''
This is the simple code for PIR activated GIF
Connect your PIR and RPI as shown in schematic
Copy paste this code in Python3 and Run

'''
#ELECTRICALTECHY.BLOGSPOT.IN

import RPi.GPIO as GPIO
import time
import os , sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)        

while True:
       i=GPIO.input(4)
       if i==0:
              print ("No intruders",i)
              time.sleep(0.1)
       elif i==1:
             print ("Intruder detected",i)
             os.system('xdg-open /home/pi/AnimatedGIF.gif')
             time.sleep(0.1)
             sys.exit(0)
