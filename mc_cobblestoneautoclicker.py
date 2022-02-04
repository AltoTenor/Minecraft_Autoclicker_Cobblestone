import mouse
import keyboard
import time
time.sleep(15)
i=0
while True:
    i+=1
    mouse.drag(0,0,0,0, absolute=False, duration=1.1)
    time.sleep(1)
    if i>130:
        mouse.wheel(1)
        i=0
    if keyboard.is_pressed('o'):
        break
