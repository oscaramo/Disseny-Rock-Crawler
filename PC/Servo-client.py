import socket
while True:
    ms=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='192.168.1.40'
    ms.connect((host,1234))

    message=input('Instruction:')
    message=message.encode('utf-8')
    ms.sendall(message)
    if message=='s':
        break
    else:
        data=ms.rcv(1000)
        print(data)
        ms.close()
