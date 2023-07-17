import pyautogui
import time
spam = open("text.txt")
for text in spam:
    time.sleep(.8)
    pyautogui.write(text)
