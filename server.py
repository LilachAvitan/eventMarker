import socket
from datetime import datetime
import pyautogui
import time

print ("Server V6 started...")
HOST = ''  # listening to all ocmmming connections 
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
noOfMsgs = 0 
print ("alt-tab to Stream-7 window")
time.sleep(5)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print("Listening...")
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                pyautogui.press(data.decode("utf-8"))
                noOfMsgs += 1
                print("Message "+str(noOfMsgs)+ " : "+data.decode("utf-8"))
