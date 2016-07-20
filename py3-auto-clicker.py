import win32api
import win32con
import threading
import time

cps = 0

def counter():

    while True:
        global cps
        print("Clicks Per Second", cps)
        cps = 0
        time.sleep(1)

def clicker():

    global cps

    while True:

        if win32api.GetAsyncKeyState(81) != 0 and win32api.GetAsyncKeyState(16) != 0:

            while True:

                (x,y) = win32api.GetCursorPos() #Get the current position of the cursor
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
                cps += 1
                time.sleep(0.01)

                if win32api.GetAsyncKeyState(87) != 0 and win32api.GetAsyncKeyState(16) != 0:
                    break
                    cps = 0


threading.Thread(target = clicker).start()
threading.Thread(target = counter).start()
