import socket
import time
import pipan

ms=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ms.bind(('',1220)) #connecta al port 1250
ms.listen(5)

[x,y]=[150,150]

p=pipan.PiPan()

p.do_tilt(x)
p.do_pan(y)

while True:
    conn,addr=ms.accept()
    data=conn.recv(1000)
    if data==b'r' and x<250:
        x=x+2
    elif data==b'l' and x>50:
        x=x-2
    elif data==b'u' and y<250:
        y=y-2
    elif data==b'd' and y>50:
        y=y+2
    elif data==b's':
        p.do_pan(150)
        p.do_tilt(150)
        break
    
    p.do_pan(y)
    p.do_tilt(x)

conn.close()
ms.close()
