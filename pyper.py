from PIL import ImageGrab
from PIL import Image, ImageEnhance, ImageFilter
import os
import time
from pynput.keyboard import Key, Controller
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#Put tesseract in
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def takeImg():
    im = ImageGrab.grab(bbox=(701, 832, 1214, 951)) #banner
    #im = ImageGrab.grab(bbox=(705, 736, 1209, 847)) #no banner
    imb = im.convert('L')
    imbr = imb.resize((1000,232))
    imbr.save('words.png')

def scanImg():
    global output
    output = pytesseract.image_to_string(Image.open('words.png'))
    print(output)

def type():
    keyboard = Controller()
    keyboard.type(output)

takeImg()
scanImg()
type()