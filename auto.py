import pyautogui
import time


def click():
    x, y = pyautogui.position()
    print(x, y)
    # 214 229
    pyautogui.moveTo(214, 229, duration=1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(297, 197, duration=1)
    pyautogui.click()

    pyautogui.moveTo(1086, 602, duration=1)
    pyautogui.click()
    time.sleep(3)

    # pyautogui.moveTo(1142, 600, duration=1)
    # pyautogui.click()
    # time.sleep(3)


for i in range(30):
    print(i)
    click()
    time.sleep(1)
