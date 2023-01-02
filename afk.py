from pynput import keyboard
from threading import Thread
from time import sleep
import random
import pyautogui as pyg
import pydirectinput, threading, time, sys, os

w = "w"
a = "a"
s = "s"
d = "d"
period = "."
comma =  ","



def press_key(key):
    pydirectinput.press(key)

def hold_key(key, s):
    pydirectinput.keyDown(key)
    time.sleep(s)
    pydirectinput.keyUp(key)



def on_press(key, abortKey='esc'):    
    try:
        k = key.char  
    except:
        k = key.name    

    print('pressed %s' % (k))
    if k == abortKey:
        print('end loop ...')
        return False  

def loop_fun():
    while True:
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)
        pyg.moveTo(x,y,1)
        pyg.press('w')
        print (pyg.position())
        press_key("w")
        sleep(1)




        
if __name__ == '__main__':
    abortKey = 't'
    listener = keyboard.Listener(on_press=on_press, abortKey=abortKey)
    listener.start()  

    
    Thread(target=loop_fun, args=(), name='loop_fun', daemon=True).start()

    listener.join() 
time.sleep(2)
threading.Thread(target=start()).start()

