import pyautogui

'''
PyAutoGUI lets your Python scripts control 
the mouse and keyboard to automate interactions 
with other applications.

>>> https://github.com/asweigart/pyautogui 
'''

# Sets a 2 second pause after each PyAutoGUI call:
pyautogui.PAUSE = 2

# How manu pixels PyAutoGUI will use to move in screen
pixel = 200

while True:
    pixel *= -1 # move 200 pixels in opposite directions 
    pyautogui.moveRel(0, pixel, duration=5) # duration = speed of mouse movement

# End program by control + c via CLI