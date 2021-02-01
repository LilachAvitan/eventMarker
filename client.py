import socket
import time


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    tsStart = time.time()
    for i in range(1,10):
        s.sendall(b'i')
        data = s.recv(1024)
        print('Received', repr(data))
    tsEnd=time.time()
    print("time diff =" ,(tsEnd-tsStart)/10)
    