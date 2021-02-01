import pyautogui
import time

cmd = input("start or exit [start]?")
while cmd=="start" or cmd=="":
    time.sleep(5)
    with open("input.txt") as f:
        while True:
            c = f.read(1)
            if not c:
                print ("End of file")
                break
            pyautogui.press(c)
            print (c)
    cmd = input("start or exit?")
