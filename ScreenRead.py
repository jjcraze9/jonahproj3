import pyautogui
import cv2
import numpy as np
from pynput.keyboard import Key, Controller
import time
import keyboard

time.sleep(5)

keyboar = Controller()

# Define the colors to find. OpenCV uses BGR instead of RGB
#grey = [174,163,135]

#blue = [255,255,0]
#green = [5,250,18]
#red = [63,57,249]
#purple = [153,75,194]

while True:
	#saves a screenshot to a certain path
	im = pyautogui.screenshot(region = (2040, 180, 1250, 320))

	# Load image
	purp = im.getpixel((180, 50))
	red = im.getpixel((1100, 50))
	green = im.getpixel((805, 55))
	blue = im.getpixel((485, 55))

	if (blue == (0,255,255)):
		keyboar.press('s')
		keyboar.release('s')
		print("test")

	if (green == (18,250,5)):
		keyboar.press('w')
		keyboar.release('w')

	if (red == (249,57,63)):
		keyboar.press('d')
		keyboar.release('d')

	if (purp == (194,75,153)):
		keyboar.press('a')
		keyboar.release('a')

	pyautogui.press('enter')