import pyautogui
from time import sleep
s = int(input())
sleep(3)

for i in range(s):
 for j in range(i+1):
    pyautogui.write('#', interval=0.25)
 pyautogui.press('enter')
