import pyautogui as pag
from time import sleep

pag.press("win")
pag.write("chrome")
pag.press("enter")
sleep(2)
pag.write("https://pt.duolingo.com/")
pag.press("enter")
sleep(1)
pag.moveTo(1100,635)
pag.click()

