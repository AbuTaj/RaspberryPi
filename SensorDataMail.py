#Abu Taj
#Alert MailSender.

import RPi.GPIO as GPIO               
import time

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail=MIMEMultipart()

ser=smtplib.SMTP('smtp.gmail.com',587) #SMTP Server and Port Number
ser.starttls()  #Server Starting
ser.login('sender@gmail.com','senderpassword')  #Authentication Point


GPIO.setmode(GPIO.BCM)  #Numbering the GPIO pin                 

TRIG = 23
ECHO = 24

pulse_start=0
pulse_end=0

GPIO.setup(TRIG,GPIO.OUT)  #GPIO Mapping              
GPIO.setup(ECHO,GPIO.IN)               

while True:

  GPIO.output(TRIG, False)               
  time.sleep(0.1)
  GPIO.output(TRIG, True)                
  time.sleep(0.00001)                    
  GPIO.output(TRIG, False)               
  while GPIO.input(ECHO)==0:
    pulse_start = time.time()
  while GPIO.input(ECHO)==1:
    pulse_end = time.time() 
  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150       
  distance = round(distance)            
  if distance < 50 :  #Only Sends mail when sensor reads Less than 50 cm
    mail['From']='Home Automation Systems'
    mail['To']='receiver@gmail.com'
    mail['Subject']='Sensor Data - Alert'
    body='Sensor Read the Critical Data Distance of '+str(distance)+' cm'
    mail.attach(MIMEText(body,'plain'))    
    msg=mail.as_string()
    ser.sendmail('sender@gmail.com','receiver@gmail.com',msg)
    print('Mail Sent')   
GPIO.cleanup()
