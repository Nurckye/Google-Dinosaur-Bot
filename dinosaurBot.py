# Radu Nitescu @ Personal Project
# June 2019

import pyautogui, sys
import pyscreenshot as ImageGrab
import time
from PIL import ImageOps
from numpy import *

class Coordinates():
    tryAgainButton = (485, 284)
    dinosaur = (208, 306)

def restartGame():
    pyautogui.click(Coordinates.tryAgainButton)
def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')
    time.sleep(0.05)
def takeImageOfScreen():
    box = (Coordinates.dinosaur[0], Coordinates.dinosaur[1],Coordinates.dinosaur[0] + 40, Coordinates.dinosaur[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

defaultValue = 1447
restartGame()
while True:
    obstacle= takeImageOfScreen()
    if obstacle != 1447:
        jump()
