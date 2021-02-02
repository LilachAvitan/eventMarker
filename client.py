import socket
import time


HOST = '132.64.105.40'  # The IP address of the streams-7 macing, can be obtained using ipconfig 
PORT = 65432        # The port used by the server

print ("Trying to connect host "+HOST+" Port "+ str(PORT))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    tsStart = time.time()
    s.sendall(b'f9') #sending f9 that cause stream-7 to create event-marker 
    #data = s.recv(1024)
    #print('Received', repr(data))
    #tsEnd=time.time()
    #print("time diff =" ,(tsEnd-tsStart)/10)
    