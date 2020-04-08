import RPi.GPIO as GPIO
import socket
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
pwm=GPIO.PWM(12,50)
pwm.start(7)

ms=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ms.bind(('',1250))
ms.listen(5)

l_m='m'

while True:
    print('starting new loop')
    conn,addr=ms.accept()
    data=conn.recv(1000)
    print(data)
    if data==b'r':
        if l_m=='l':
            for i in range(2,13):
                pwm.ChangeDutyCycle(i)
                time.sleep(0.1)
                l_m='r'
        elif l_m=='m':
            for i in range(7,13):
                pwm.ChangeDutyCycle(i)
                time.sleep(0.1)
                l_m='r'
        else:
            continue
        conn.sendall(b'turned right')
        
    elif data==b'l':
        if l_m=='r':
            for i in range(12,1,-1):
                pwm.ChangeDutyCycle(i)
                time.sleep(0.1)
                l_m='l'
        elif l_m=='m':
            for i in range(7,1,-1):
                pwm.ChangeDutyCycle(i)
                time.sleep(0.1)
                l_m='l'
        else:
            continue
        conn.sendall(b'turned left')
        
    elif data==b'm':
        if l_m=='r':
            for i  in range(12,6,-1):
                pwm.ChangeDutyCycle(i)
                time.sleep(0.1)
                l_m='m'
        elif l_m=='l':
            for i in range(2,8):
                pwm.ChangeDutyCycle(i)
                time.sleep(0.1)
                l_m='m'
        else:
            continue
        conn.sendall(b'went to the middle')
        
    elif data==b's':
        conn.sendall(b'It stopped')
        break
    else:
        conn.sendall(b'Wrong button')

pwm.ChangeDutyCycle(7)
conn.close()
ms.close()