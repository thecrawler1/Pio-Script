import pyscreenshot as ImageGrab
import pytesseract as ocr
import time

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

ocr.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

mouse = MouseController()
keyboard = KeyboardController()

ACCURACY = 0.25
directory = 'C:\\Users\\Gabriel\\Documents\\gametrees\\SRP\\SB x BB\\Vs regs\\'

flops = ['6s7dTc:16.25', '6s7dQc:65.09', '6dJsAs:44.33', '7s9dKc:31.2', '7sJdAs:26.01', '8s9dQc:26.02', '8sTsQs:47.24', '8sTdKc:40.08', '8sTdAs:51.67', '9sTdQc:31.75', '9dTsKs:36.85', 'TsJdQc:9.57', 'TsJsAd:26.86']
#flops = ['3s3d2c:20.45', '4s4d5s:32.58', '6s6dAs:31.73', '7s7d6s:21', '8s8dJs:46.25', 'TsTdKs:51.86', 'JsJd9s:29.2', 'QsQdJc:56.75', 'KsKd7s:27.5', 'AsAd7s:24.61', '2s3d7c:55.79', '2d3s9s:19.48', '2s4dQc:46.16', '2s4dAc:19.96', '2s5dTc:43.36', '2s5sAd:24.54', '2d6s9s:87.41', '2s8dJs:65.99', '2dQsKs:43.5', '3s4s6s:50.65', '3s5s9d:73.97', '3d6sKs:43.88', '3s7dQc:21.15', '3d8s9s:26.27', '3s8sQs:31.36', '3s9dAc:52.29', '3dKsAs:62.67', '4s5dJc:66.21', '4s6dTc:59.87', '4s7s8d:66.8', '4s8dKc:50.43', '4sJsKd:43.33', '5s6d8c:24.13', '5s7s9s:35.32', '5s7dTc:42.34', '5dQsAs:82.2', '6s7dTc:16.25', '6s7dQc:65.09', '6dJsAs:44.33', '7s9dKc:31.2', '7sJdAs:26.01', '8s9dQc:26.02', '8sTsQs:47.24', '8sTdKc:40.08', '8sTdAs:51.67', '9sTdQc:31.75', '9dTsKs:36.85', 'TsJdQc:9.57', 'TsJsAd:26.86']

def accuracy():

    screenshot = ImageGrab.grab(bbox=(500, 1000, 1600, 1050))
    text = ocr.image_to_string(screenshot)
    words = text.split(' ')
    accuracy = 101 if len(words) < 10 else float(words[2][:-1])

    print('Accuracy: ')
    print(accuracy)
    
    return accuracy

def openTree(flop):
    
    # Select file

    print('Select file')

    with keyboard.pressed(Key.ctrl):
        
        keyboard.press('o')
        keyboard.release('o')

    time.sleep(2)
        
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)

    keyboard.type(directory + flop.split(':')[0])
        
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(2)


def startSolving():

    print('Go')
        
    mouse.position = (110, 1030)
    mouse.click(Button.left)

    time.sleep(2)

def stopAndSaveTree(flop):

    # Stop

    print('Stop')

    mouse.position = (190, 1025)
    mouse.click(Button.left)

    time.sleep(20)

    # Save tree

    print('Save tree')

    with keyboard.pressed(Key.ctrl):
        
        keyboard.press('s')
        keyboard.release('s')

    time.sleep(2)
        
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)

    keyboard.type(directory + flop.split(':')[0])
        
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(1)

    # Replace confirm

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

    for flop in flops:

        print('Flop \"' + flop + '\" selected')

        openTree(flop)

        while not pioReady():

            time.sleep(2)

        if accuracy() <= ACCURACY:

            continue

        startSolving()

        while accuracy() > ACCURACY:

            time.sleep(10)

        stopAndSaveTree(flop)

        while not pioReady():

            time.sleep(2)
