import pyautogui as p
from time import sleep

# p.mouseInfo()


p.press('win')
p.write('chrome',interval=0.2)
p.press('enter')
sleep(1)
p.write('www.youtube.com',interval=0.2)
p.press('enter')
p.moveTo(794,110,duration=1)
p.click()
p.write('receita de bolo de cenoura com chocolate')
p.press('enter')
