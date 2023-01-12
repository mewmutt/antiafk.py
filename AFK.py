import random
import threading
import time
import pyautogui as pyg
import pydirectinput

def press_key(key):
    pydirectinput.press(key)

def hold_key(key, s):
    pydirectinput.keyDown(key)
    time.sleep(s)
    pydirectinput.keyUp(key)

def random_movement():
    while True:
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)
        pyg.moveTo(x,y,1)
        pyg.press('w')
        print(pyg.position())
        press_key("w")
        time.sleep(1)

def on_press(key):    
    try:
        k = key.char  
    except AttributeError:
        k = key.name    

    if k == 'esc':
        print('end loop ...')
        return False  

if __name__ == '__main__':
    listener = pydirectinput.keyboard.Listener(on_press=on_press)
    listener.start()  

    threading.Thread(target=random_movement, args=(), name='random_movement', daemon=True).start()

    listener.join()
