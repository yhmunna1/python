import pyautogui

# Read the number from the user
n = int(input(5))

# Set the initial coordinates
x, y = 500, 500

# Loop to draw the pyramid
for i in range(1, n + 1):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.typewrite('#' * i)
    y -= 20
    x -= 10
