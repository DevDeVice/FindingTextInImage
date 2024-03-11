import cv2
import numpy as np
import pyautogui   
import time

def find_text_on_screen(text):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    
       # Wyszukiwanie napisu na ekranie
    result = cv2.matchTemplate(screenshot, cv2.imread('kliknij.png'), cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    threshold = 0.80  # Prog wartości dopasowania
    
    if max_val >= threshold:
        # Znaleziono napis na ekranie
        print(max_val)
        return max_loc
    else:
        # Napis nie został znaleziony      
        print(max_val)
        return None
   
def click_text():
    pyautogui.rightClick()
    multiple_space_presses(3, 0.2)

def multiple_space_presses(presses, interval):
    for _ in range(presses):
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        time.sleep(interval)

while True:
    text_location = find_text_on_screen("Kliknij spację jeszcze")
    if text_location:
        print("Znaleziono", text_location)
        pyautogui.moveTo(text_location[0]-20,text_location[1]+20)
        click_text()
    else:
        print("Nie znaleziono")   
    time.sleep(1)  # Czekaj 1 sekundę przed kolejnym sprawdzeniem ekranu