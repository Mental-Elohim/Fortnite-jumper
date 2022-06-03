# Imports/
import keyboard
import pyautogui
import time
 
time.sleep(4) # time so you can change it to fortnite you can change the timer to how many seconds you want it to be
# Function that starts the jump movement 
def pressSpace():
    pyautogui.press('space') # Tells the code what button/key will be pressed
# take the main and is added to a loop so it's a jumping loop.
while True: 
        pressSpace()
        time.sleep(0.1)
        # The code below lets the user break the loop with a button you can change it to what ever key you want 
        if keyboard.is_pressed('v'):
            break
            
# This was my first code idea if you have idea please give some :)