from src.keyboard import Keyboard

keyboard = Keyboard()
try:
  keyboard.automate()
except Exception as e:
  with open('error.log', 'w') as file:
    file.write(repr(e))

