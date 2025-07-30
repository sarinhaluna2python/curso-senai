import pyautogui as pag
from time import sleep

# pag.displayMousePosition()


pag.press("win")
pag.write("chrome")
pag.press("enter")
sleep(2)
pag.write("https://br.pinterest.com/")
pag.press("enter")
sleep(2)
pag.moveTo(1750,140,duration=1)
pag.click()
sleep(1)
pag.write("sarahfeitosa.sm@gmail.com")
pag.press("tab")
pag.write("sarahlinda123")
pag.press("enter")