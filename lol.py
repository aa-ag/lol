import pyautogui

'''
PyAutoGUI lets your Python scripts control 
the mouse and keyboard to automate interactions 
with other applications.

>>> https://github.com/asweigart/pyautogui 
'''

pixel = 20

while True:
    pixel *= -1
    pyautogui.moveRel(0, pixel, duration=1)