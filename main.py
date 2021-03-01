import pyautogui
import time
import random
import webbrowser

googleUrl = 'https://www.google.com/?client=safari&channel=mac_bm'
youtubeUrl = 'https://www.youtube.com'
listGmail = []
listUser = []
listPassword = []
listRecovery = []


def readFileText():
    time.sleep(2)
    f = open("gmail.txt", "r")
    listGmail = f.readlines()
    for i in listGmail:
        user = i.split('|')[0]
        password = i.split('|')[1]
        recovery = i.split('|')[2].replace('\n', '')

        listUser.append(user)
        listPassword.append(password)
        listRecovery.append(recovery)


def deleteFirstLine():
    time.sleep(2)
    f = open("gmail.txt", "r+")
    f.writelines('\n')


def getFirstName():
    time.sleep(2)
    firstName = open("firstName.txt", "r")
    listFirstName = firstName.readlines()
    firstNameRandom = random.choice(listFirstName)
    return firstNameRandom


def getLastName():
    time.sleep(2)
    lastName = open("lastName.txt", "r")
    listLastName = lastName.readlines()
    lastNameRandom = random.choice(listLastName)
    return lastNameRandom


def exitBrowser(timeMin, timeMax):
    time.sleep(random.randint(timeMin, timeMax))
    pyautogui.hotkey('command', 'q', interval=0.05)


def waitForImgAppear(image, timeMin, timeMax, type, x0, y0, imgClick):
    while True:
        time.sleep(random.randint(timeMin, timeMax))
        logo = pyautogui.locateOnScreen(image, confidence=0.8)
        if logo is not None:
            time.sleep(random.randint(timeMin, timeMax))
            if type == 'click':
                pyautogui.click(x0, y0)
            elif type == 'tab':
                pyautogui.typewrite(['tab'])
            elif type == 'image':
                xC, yC = pyautogui.locateCenterOnScreen(imgClick)
                pyautogui.click(xC, yC)


def waitForImageAppearAndClick(image, timeMin, timeMax, timeClick):
    while True:
        time.sleep(random.randint(timeMin, timeMax))
        logo = pyautogui.locateOnScreen(image, confidence=0.8)
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


def isImageAppear(image, timeSleep):
    time.sleep(timeSleep)
    if pyautogui.locateOnScreen(image, confidence=0.8) is not None:
        return True

    return False


def enterText(timeMin, timeMax, text, interval):
    time.sleep(random.randint(timeMin, timeMax))
    pyautogui.typewrite(text, interval)
    pyautogui.typewrite(['\n'])


def pressTab(timeMin, timeMax):
    time.sleep(random.randint(timeMin, timeMax))
    pyautogui.press('tab')


def openSafari(timeMin, timeMax):
    time.sleep(random.randint(timeMin, timeMax))
    webbrowser.open(googleUrl)


def login():
    readFileText()
    for i in range(len(listUser)):
        time.sleep(5)
        webbrowser.open(googleUrl)
        waitForImageAppearAndClick('btnDangNhap.png', 1, 2, 1)
        time.sleep(3)
        enterText(2, 3, listUser[i], 0.15)
        time.sleep(3)
        enterText(1, 2, listPassword[i], 0.15)

        time.sleep(6)
        squareRecovery = isImageAppear('btnAddRecovery.png', 1)
        rectangleRecovery = isImageAppear('imgLockAndKey.png', 1)
        agreeButton = isImageAppear('btnDongY.png', 1)
        noBirthday = isImageAppear('imgNoBirthday.png', 1)
        if squareRecovery:
            waitForImageAppearAndClick('btnAddRecovery.png', 1, 2, 1)
            waitForImageAppearAndClick('btnHuy.png', 1, 2, 1)
            time.sleep(2)
            pressTab(2, 3)
            enterText(3, 5, listRecovery[i], 0.15)
            waitForImageAppearAndClick('btnXong.png', 1, 2, 1)
            w = open('gmailSuccess.txt', 'a')
            w.write(listUser[i] + '|' + listPassword[i] + '|' + listRecovery[i] + '\n')

        elif rectangleRecovery:
            waitForImageAppearAndClick('btnCapNhat.png', 1, 2, 1)
            waitForImageAppearAndClick('btnBoQua.png', 1, 2, 1)
            time.sleep(2)
            pressTab(2, 3)
            enterText(2, 4, listRecovery[i], 0.15)
            w = open('gmailSuccess.txt', 'a')
            w.write(listUser[i] + '|' + listPassword[i] + '|' + listRecovery[i] + '\n')

        elif agreeButton:
            clickAgreeButton()
            exitBrowser(3, 5)
            webbrowser.open(googleUrl)
            waitForImageAppearAndClick('btnDangNhap.png', 1, 2, 1)
            enterText(3, 5, listUser[i], 0.15)
            enterText(3, 5, listPassword[i], 0.15)
            squareRecovery = isImageAppear('btnAddRecovery.png', 6)
            rectangleRecovery = isImageAppear('btnAddRecovery.png', 2)
            if squareRecovery:
                waitForImageAppearAndClick('btnAddRecovery.png', 1, 2, 1)
                waitForImageAppearAndClick('btnHuy.png', 1, 2, 1)
                time.sleep(2)
                pyautogui.typewrite(['tab'])
                enterText(3, 5, listRecovery[i], 0.15)
                waitForImageAppearAndClick('btnXong.png', 1, 2, 1)
                w = open('gmailSuccess.txt', 'a')
                w.write(listUser[i] + '|' + listPassword[i] + '|' + listRecovery[i] + '\n')
            elif rectangleRecovery:
                waitForImageAppearAndClick('btnCapNhat.png', 1, 2, 1)
                waitForImageAppearAndClick('btnBoQua.png', 1, 2, 1)
                time.sleep(2)
                pressTab(2, 3)
                enterText(2, 4, listRecovery[i], 0.15)
                w = open('gmailSuccess.txt', 'a')
                w.write(listUser[i] + '|' + listPassword[i] + '|' + listRecovery[i] + '\n')

        elif noBirthday:
            pressTab(2, 4)
            enterText(2, 4, '15', 0.15)
            pressTab(2, 3)
            pyautogui.press('down')
            pyautogui.press('down')
            pressTab(2, 3)
            enterText(2, 3, '1995', 0.1)
            waitForImageAppearAndClick('btnLuu.png', 1, 2, 1)
            waitForImageAppearAndClick('btnXong.png', 1, 2, 1)
            myAccountLink = 'https://myaccount.google.com/?utm_source=OGB&utm_medium=app'
            pressTab(3, 5)
            enterText(2, 3, myAccountLink, 0.1)
            secureAccount = isImageAppear('btnSecureAccount.png', 5)
            if secureAccount:
                waitForImageAppearAndClick('btnSecureAccount.png', 1, 2, 1)
                signInAndRecovery = isImageAppear('signinAndRecovery.png', 5)
                if signInAndRecovery:
                    waitForImageAppearAndClick('signinAndRecovery.png', 1, 2, 1)
                    pyautogui.click(1034, 511, interval=0.5)
                    enterText(2, 4, listPassword[i], 0.15)
                    pressTab(4, 6)
                    pressTab(1, 1)
                    enterText(2, 3, listRecovery[i], 0.15)
                    waitForImageAppearAndClick('btnDone.png', 1, 2, 1)
                    w = open('gmailSuccess.txt', 'a')
                    w.write(listUser[i] + '|' + listPassword[i] + '|' + listRecovery[i] + '\n')
        exitBrowser(3, 5)


def clickAgreeButton():
    waitForImageAppearAndClick('btnDongY.png', 1, 2, 6)


login()
