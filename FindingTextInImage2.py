import pyautogui

res = pyautogui.locateOnScreen('raz1.png')
print(res)
edit_but = pyautogui.center(res)

pyautogui.moveTo(edit_but)