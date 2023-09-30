import pyautogui
from time import sleep
sleep(3)

for i in range(0,3):
 pyautogui.write('Hello World!', interval=0.25)
 pyautogui.press('enter')



