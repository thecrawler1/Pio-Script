import pyscreenshot as ImageGrab
import pytesseract as ocr
import time
import clipboard

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

ocr.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

mouse = MouseController()
keyboard = KeyboardController()

directorys = ['C:\\Users\\Gabriel\\Documents\\trees\\SRP\\IP\\PFC\\BB x SB\\Vs regs\\', 'C:\\Users\\Gabriel\\Documents\\trees\\SRP\\IP\\PFC\\BU x CO\\Vs regs\\']
flops = ['8s8dJs:46.25', 'TsTdKs:51.86', 'JsJd9s:29.2', 'QsQdJc:56.75', 'KsKd7s:27.5', 'AsAd7s:24.61']
#flops = ['3s3d2c:20.45', '4s4d5s:32.58', '6s6dAs:31.73', '7s7d6s:21', '8s8dJs:46.25', 'TsTdKs:51.86', 'JsJd9s:29.2', 'QsQdJc:56.75', 'KsKd7s:27.5', 'AsAd7s:24.61', '2s3d7c:55.79', '2d3s9s:19.48', '2s4dQc:46.16', '2s4dAc:19.96', '2s5dTc:43.36', '2s5sAd:24.54', '2d6s9s:87.41', '2s8dJs:65.99', '2dQsKs:43.5', '3s4s6s:50.65', '3s5s9d:73.97', '3d6sKs:43.88', '3s7dQc:21.15', '3d8s9s:26.27', '3s8sQs:31.36', '3s9dAc:52.29', '3dKsAs:62.67', '4s5dJc:66.21', '4s6dTc:59.87', '4s7s8d:66.8', '4s8dKc:50.43', '4sJsKd:43.33', '5s6d8c:24.13', '5s7s9s:35.32', '5s7dTc:42.34', '5dQsAs:82.2', '6s7dTc:16.25', '6s7dQc:65.09', '6dJsAs:44.33', '7s9dKc:31.2', '7sJdAs:26.01', '8s9dQc:26.02', '8sTsQs:47.24', '8sTdKc:40.08', '8sTdAs:51.67', '9sTdQc:31.75', '9dTsKs:36.85', 'TsJdQc:9.57', 'TsJsAd:26.86']


def openTree(directory, flop):
    
    # Select file

    print('Select file')

    with keyboard.pressed(Key.ctrl):
        
        keyboard.press('o')
        keyboard.release('o')

    time.sleep(0.5)
        
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)

    keyboard.type(directory + flop.split(':')[0])
        
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(0.5)

def pioReady():

    time.sleep(0.5)

    screenshot = ImageGrab.grab(bbox=(293, 980, 298, 986))
    pix = screenshot.load()
    ready = True if pix[0, 0] == (225, 225, 225) else False

    print('pioReady: ')
    print(ready)

    return ready

def goToBrowser():

    print('Go to browser')

    time.sleep(0.5)

    mouse.position = (90, 55)
    mouse.click(Button.left)

    time.sleep(0.5)
    
def selectNode(positions):

    print('Select node')

    time.sleep(0.5)

    nodes = positions

    for node in nodes:

        mouse.position = node
        mouse.click(Button.left)

        time.sleep(0.25)

def openPio():

    print('Open Pio')
        
    selectNode([(0, 1079), (1876, 350)])
        
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(2.5)
        
    selectNode([(1050, 20)])

def runFlop(directory, flop):

    print('Flop \"' + flop + '\" selected')
    
    openPio()
    openTree(directory, flop)

    while not pioReady():
        time.sleep(0.5)

    goToBrowser() #((350, 80), 400, 100), 
    selectNode([(350, 100), (1850, 320), (1850, 290), (1035, 75), (363, 177), (950, 75), (1020, 63), (1020, 90), (1020, 115), (1020, 140), (1020, 165), (1020, 190)])
            
if __name__ == '__main__':

    tmp = 5;
    print('Starts in...')

    while tmp > 0:

        print(tmp)
        tmp = tmp - 1
        time.sleep(0.5)

    for flop in flops:
        for directory in directorys:
            runFlop(directory, flop)
            
