import pyscreenshot as ImageGrab
import pytesseract as ocr
import time

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

from os import listdir, chdir
from os.path import isfile, join, abspath

ocr.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

mouse = MouseController()
keyboard = KeyboardController()

ACCURACY = 0.25
DIRECTORY = 'C:\\Users\\gabri\\Documents\\Trees\\Awaiting'

def allFiles (path):

    chdir(path)

    items = [abspath(x) for x in listdir(path)]
    files = [f for f in items if isfile(f)]
    
    for item in items:
        if not item in files:
            files.extend(allFiles(item))

    return files

def accuracy():

    screenshot = ImageGrab.grab(bbox=(500, 1000, 1600, 1050))
    text = ocr.image_to_string(screenshot)
    words = text.split(' ')
    accuracy = 101 if len(words) < 10 else float(words[2][:-1])

    print('Accuracy: ')
    print(accuracy)
    
    return accuracy

def openTree(path):
    
    # Select file

    print('Select file')

    with keyboard.pressed(Key.ctrl):
        
        keyboard.press('o')
        keyboard.release('o')

    time.sleep(2)
        
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)

    keyboard.type(path)
        
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(2)


def startSolving():

    print('Go')
        
    mouse.position = (110, 1030)
    mouse.click(Button.left)

    time.sleep(2)

def stop():

    print('Stop')

    mouse.position = (190, 1025)
    mouse.click(Button.left)

    time.sleep(20)

def saveFullTree(path):

    print('Save full tree')

    with keyboard.pressed(Key.ctrl):
        
        keyboard.press('s')
        keyboard.release('s')

    time.sleep(2)
        
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)

    keyboard.type(path)
        
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(2)

def saveSmallTree(path):

    print('Save small tree')
        
    mouse.position = (80, 30)
    mouse.click(Button.left)

    time.sleep(1)
        
    mouse.position = (120, 120)
    mouse.click(Button.left)

    time.sleep(2)
        
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)

    keyboard.type(path)
        
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(2)

def replaceConfirm():

    print('Replace confirm')

    keyboard.press(Key.left)
    keyboard.release(Key.left)
        
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(2)

def pioReady():

    time.sleep(2)

    screenshot = ImageGrab.grab(bbox=(293, 980, 298, 986))
    pix = screenshot.load()
    ready = True if pix[0, 0] == (225, 225, 225) else False

    print('pioReady: ')
    print(ready)

    return ready
            
if __name__ == '__main__':

    tmp = 5;
    print('Starts in...')

    while tmp > 0:

        print(tmp)
        tmp = tmp - 1
        time.sleep(1)

    for path in allFiles(DIRECTORY):

        print('File \"' + path + '\" selected')

        openTree(path)

        while not pioReady():

            time.sleep(2)

        if accuracy() <= ACCURACY:

            continue

        startSolving()

        while accuracy() > ACCURACY:

            time.sleep(10)

        stop()

        saveSmallTree(path)

        replaceConfirm()

        while not pioReady():

            time.sleep(2)
