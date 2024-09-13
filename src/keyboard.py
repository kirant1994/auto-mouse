import pyautogui
import numpy as np
import time

class Keyboard:
  def __init__(self):
    self.obj = pyautogui
    self.obj.FAILSAFE = False

  def pressShift(self):
    self.obj.keyDown('shift')
    self.obj.keyUp('shift')

  def automate(self):
    while True:
      self.pressShift()
      wait = np.abs(np.random.randint(100, 150) + (np.random.randn() + 1) * 10)
      print('Waiting {0:.2f} sec'.format(wait))
      time.sleep(wait)
