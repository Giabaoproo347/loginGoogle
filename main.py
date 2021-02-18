import pyautogui
import pyrobogui
import time
import random
import webbrowser
from key import username, password

googleUrl = 'https://www.google.com/?client=safari&channel=mac_bm'


def waitForLoadPage(image, timeMin, timeMax, timeClick):
    while True:
        time.sleep(random.randint(timeMin, timeMax))
        logo = pyautogui.locateOnScreen(image)
        if logo is not None:
            x, y = pyautogui.locateCenterOnScreen(image)
            if timeClick > 1:
                for i in range(timeClick):
                    time.sleep(1)
                    pyautogui.click(x / 2, y / 2)
            else:
                time.sleep(1)
                pyautogui.click(x / 2, y / 2)
            break


def login():
    time.sleep(5)
    webbrowser.open(googleUrl)
    waitForLoadPage('btnDangNhap.png', 3, 5, 1)

    time.sleep(3)
    pyautogui.typewrite(username, 0.1)
    pyautogui.typewrite(['\n'])

    time.sleep(3)
    pyautogui.typewrite(password, 0.15)
    pyautogui.typewrite(['\n'])

    waitForLoadPage('btnDongY.png', 3, 5, 6)


def testRobogui():
    pyrobogui.robo.waitImageToAppear()