import pyautogui as pag 
from time import sleep 

#pag.mouseInfo()
def mensagem(email,texto):
    pag.press("win")
    pag.write("Chrome")
    pag.press("enter")
    sleep(1.5)
    pag.write("email")
    pag.press("enter")
    sleep(1)
    pag.moveTo(366,308, duration=1)
    pag.click()
    sleep(1)
    pag.moveTo(1639,113, duration=1)
    pag.click()
    sleep(1)
    pag.moveTo(1055,520,duration=1)
    pag.click()
    sleep(1)
    pag.write("125032726x@aluno.santanadeparnaiba.sp.gov.br")
    pag.press("enter")
    sleep(2)
    pag.moveTo(1019,515,duration=1)
    pag.write("sarahlinda123")
    pag.press("enter")

    sleep(1)
    pag.moveTo(155,178, duration=1)
    pag.click()
    pag.sleep(1)
    pag.write(email)
    pag.press("enter")
    sleep(2)
    pag.moveTo(1298,538,duration=1)
    pag.click()
    pag.write("🚨ATENCAO MENSAGEM IMPORTANTE🚨")
    sleep(2)
    pag.moveTo(1268,570,duration=1)
    pag.click()
    pag.write(texto)
    sleep(1.5)
    pag.moveTo(1302,1004,duration=1)
    pag.click()
    sleep(5)
    pag.hotkey("alt","f4")
    pag.press("enter")


mensagem("sarahfeitosa.sm@gmail.com","hello!")
