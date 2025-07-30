#con1= float(input("Digite o valor da casa ? "))
#con2= float(input('Quanto é a porcentagem que será paga para o banco ?'))

#resp = con1 * (con2 / 100)

#print('O valor da porcentegem pago para o banco é', resp )
from colorama import  init, Fore
init(autoreset=True)

inf1=(input('O que vamos comprar? '))
inf2=float(input("Quanto custa? "))
inf3=float(input("Quanto é o desconto? "))

cal= inf2 * (inf3 / 100) # AQUI DESCOBRIMOS A POR CENTAGEM 
des= inf2-cal # CALCULO APOS DESCOBRIR A PORCENTAGEM 

print(f'o desconto aplicado na sua{inf1} de {cal}')
print(Fore.GREEN +f'pagará apenas {des}')
