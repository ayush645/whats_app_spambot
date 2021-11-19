import pyautogui
import  webbrowser
import  time
webbrowser.open('https://whatsapp.com')
time.sleep(60)

for i in range(25):
    pyautogui.press("s")
    pyautogui.press("p")
    pyautogui.press("a")
    pyautogui.press("m")
    pyautogui.press("enter")
