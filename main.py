import pyautogui
import time
import random
import webbrowser
import cv2
from key import username, password, recovery
import json
from pyrobogui import robo, pag

googleUrl = 'https://www.google.com/?client=safari&channel=mac_bm'
youtubeUrl = 'https://www.youtube.com'
listGmail = []
listUser = []
listPassword = []
listRecovery = []


def readFile():
    f = open("gmail.txt", "r")
    listGmail = f.readlines()
    for i in listGmail:
        user = i.split('|')[0]
        password = i.split('|')[1]
        recovery = i.split('|')[2].replace('\n', '')

        listUser.append(user)
        listPassword.append(password)
        listRecovery.append(recovery)


def waitForLoadPage(image, timeMin, timeMax, timeClick):
    while True:
        time.sleep(random.randint(timeMin, timeMax))
        logo = pyautogui.locateOnScreen(image, confidence=0.8)
        if logo is not None:
            x, y = pyautogui.locateCenterOnScreen(image)
            print(x, 'x')
            print(y, 'y')
            if timeClick > 1:
                for i in range(timeClick):
                    time.sleep(1)
                    pyautogui.click(x / 2, y / 2)
            else:
                time.sleep(1)
                pyautogui.click(x / 2, y / 2)
            break


def login():
    readFile()
    for i in range(10):
        time.sleep(5)
        webbrowser.open(googleUrl)
        waitForLoadPage('btnDangNhap.png', 1, 2, 1)

        time.sleep(3)
        pyautogui.typewrite(listUser[0], 0.1)
        pyautogui.typewrite(['\n'])

        time.sleep(3)
        pyautogui.typewrite(listPassword[0], 0.15)
        pyautogui.typewrite(['\n'])


def clickAgreeButton():
    waitForLoadPage('btnDongY.png', 1, 2, 6)


def addRecovery():
    time.sleep(4)
    pyautogui.typewrite(['tab'])
    time.sleep(1)
    pyautogui.typewrite(['delete'])
    time.sleep(1)
    waitForLoadPage('btnAddRecovery.png', 1, 2, 1)
    time.sleep(2)
    waitForLoadPage('btnHuy.png', 1, 2, 1)
    time.sleep(2)
    pyautogui.typewrite(['tab'])
    time.sleep(2)
    pyautogui.typewrite(recovery, 0.1)
    time.sleep(1)
    pyautogui.typewrite('\n')
    time.sleep(1)
    waitForLoadPage('btnXong.png', 1, 2, 1)
    time.sleep(2)
    pyautogui.typewrite(['tab'])
    time.sleep(2)
    pyautogui.typewrite(youtubeUrl, 0.1)
    time.sleep(1)
    pyautogui.typewrite('\n')


def clickToiDongY():
    login()
    time.sleep(2)
    clickAgreeButton()
    time.sleep(3)
    pyautogui.hotkey('command', 'q', interval=0.01)


def run():
    clickToiDongY()
    login()
    addRecovery()
    time.sleep(3)
    pyautogui.hotkey('command', 'q', interval=0.01)
