import webbrowser
import pyautogui
import pyperclip
import time

print(pyautogui.size())
print(pyautogui.position())

text = pyautogui.prompt('원하는 메시지를 입력해주세요')
pyperclip.copy(text)

url = "https://www.youtube.com/"

webbrowser.open_new(url)

time.sleep(2)

pyautogui.dragTo(894, 100)
pyautogui.click(button='left')

pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
