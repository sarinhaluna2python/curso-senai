import pyautogui as pag
from time import sleep

pag.press("win")
pag.write("Chrome")
pag.press("enter")
pag.sleep(1.5)
pag.write("https://www.crazygames.com/game/capybara-clicker")
pag.press("enter")
pag.moveTo(845,575,duration=1)
pag.click()
pag.sleep(2)
pag.moveTo(665,500,duration=1)

for i in range(1000):
    pag.click()