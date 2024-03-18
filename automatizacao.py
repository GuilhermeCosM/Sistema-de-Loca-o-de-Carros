import pyautogui
import time
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

 

link = "https://www.youtube.com"

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=436, y=124)
pyautogui.write("alanzoka")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=522, y=450)