import pyautogui
import numpy as np
import time

class Mouse:
  def __init__(self):
    self.obj = pyautogui
    self.obj.FAILSAFE = False
    self.x_max, self.y_max = self.obj.size()

  def moveTo(self, x, y, duration=2):
    self.obj.moveTo(x, y, duration=duration)

  def move(self, x_delta, y_delta, duration=2):
    self.obj.moveRel(x_delta, y_delta, duration=duration)

  def getPosition(self):
    return tuple(self.obj.position())

  def randomMove(self, x_min=-192, x_max=192, y_min=-108, y_max=108, duration=None):
    x_delta = np.random.randint(x_min, x_max)
    y_delta = np.random.randint(y_min, y_max)
    if duration is None:
      duration = np.sqrt(x_delta ** 2 + y_delta ** 2)/100
    x, y = self.getPosition()
    x_delta = min(x_delta, self.x_max - x)
    y_delta = min(y_delta, self.y_max - y)
    self.move(x_delta, y_delta, duration=duration)

  def humanRandomMove(self):
    num_moves = np.random.randint(5, 8)
    base_duration = np.random.randint(1, 3)
    for move in range(0, num_moves):
      move_time = (np.random.randn() + 1.1) * float(base_duration) / num_moves
      self.randomMove(x_min=-1, x_max=1, y_min=-1, y_max=1, duration=move_time/5)

  def automate(self):
    while True:
      self.humanRandomMove()
      wait = np.random.randint(10, 60) + (np.random.randn() + 1) * 10
      print('Waiting {0:.2f} sec'.format(wait))
      wait = wait if wait > 0 else 0
      time.sleep(wait)
