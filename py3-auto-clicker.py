import win32api
import win32con
import time

import threading
from threading import Thread

cps = 0
speed = 0.01 #Click per second modifier

def counter():

    while True:
        """Prints the amount of Clicks per Second and resets the counter every second."""

        global cps
        print("Clicks Per Second {}  ".format(cps), end = "\r") #Two spaces needed after cps in order to avoid number overlapping
        cps = 0
        time.sleep(1)

def clicker():
    """Checks for keyboard combinations and handles clicking."""

    global cps
    global speed

    while True:

        if win32api.GetAsyncKeyState(81) != 0 and win32api.GetAsyncKeyState(16) != 0: #Check if Shift + Q is pressed

            while True:

                (x,y) = win32api.GetCursorPos() #Get the current position of the cursor
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
                cps += 1
                time.sleep(speed)

                if win32api.GetAsyncKeyState(38) != 0 and win32api.GetAsyncKeyState(16) != 0 and speed > 0.005: #Check if Shift + Up is pressed
                    speed -= 0.005
                    cps = 0
                    time.sleep(0.1)

                if win32api.GetAsyncKeyState(40) != 0 and win32api.GetAsyncKeyState(16) != 0 and speed < 1: #Check if Shift + Down is pressed
                    speed += 0.005
                    cps = 0
                    time.sleep(0.1)

                if win32api.GetAsyncKeyState(87) != 0 and win32api.GetAsyncKeyState(16) != 0: #Check if Shift + W is pressed
                    break
                    cps = 0

t1 = Thread(target = clicker) #If threads were not daemons the program would not exit with keyboard interrupt
t1.daemon = True
t1.start()

t2 = Thread(target = counter)
t2.daemon = True
t2.start()

while True: #As all threads created by the program are daemons, the program would exit immediately if this infinite loop wasn't here
    time.sleep(1)
