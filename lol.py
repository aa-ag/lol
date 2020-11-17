import pyautogui

'''
PyAutoGUI lets your Python scripts control 
the mouse and keyboard to automate interactions 
with other applications.

>>> https://github.com/asweigart/pyautogui 
'''

def do_not_sleep():
    # Sets a 2 second pause after each PyAutoGUI call:
    pyautogui.PAUSE = 1

    # How manu pixels PyAutoGUI will use to move in screen
    pixel = 20

    pyautogui.confirm('Hit "Ok" and sit back and relax: I gotcha ;)')

    while True:
        pixel *= -1 # move pixel in opposite directions 
        pyautogui.moveRel(0, pixel, duration=1) # duration = speed of mouse movement
    

do_not_sleep()

