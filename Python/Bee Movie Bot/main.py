import time
import pyautogui

script = open("script.txt")
for text in script:
    time.sleep(0.8)
    pyautogui.write(text)
