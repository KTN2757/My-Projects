import time
import pyautogui

pyautogui.FAILSAFE = True
script = open("script.txt")
for text in script:
    time.sleep(2)
    pyautogui.write(text)
