I'm using https://pyautogui.readthedocs.io/en/latest/index.html

first install using pip install pyautogui

Server - run this on the Stream-7 machine
Client - this shows you how to call the server , copy required lines into the python code that present the movie 

 Matlab usage notes (client)
 ## One time openning 
 t = tcpip('132.64.105.40', 65432, 'NetworkRole', 'client');
 fopen(t);

 # write as many as you need 
 fwrite(t, 'f9')
 # Cleaning at the end 
 fclose(t);
 delete(t);
 clear t

Note that if fwrite is happening very often then messages will be combined, since our usage assumes event every >1 sec it's not an issue
