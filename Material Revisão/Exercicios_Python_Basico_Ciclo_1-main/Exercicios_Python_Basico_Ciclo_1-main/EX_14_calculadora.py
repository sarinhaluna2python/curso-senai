# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação
# OUTPUT ESPERADO:
#---------------------------------------- Exemplo 1 (Soma)
# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0
# ----------------------------------------- Exemplo 2 (Multiplicação)
# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0
# ----------------------------------------- Exemplo 3 (Opção inválida)
# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.
# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|------------------------------|')
print('| Calculadora')
print('|------------------------------|')
print('| 1 - Soma')
print('| 2 - Subtração')
print('| 3 - Multiplicação')
print('| 4 - Divisão ')
opc= int(input('Digite a opção: '))
if opc == 1:
    valo1=float(input('Digite o primeiro número:')) 
    valo2=float(input('Digite o segundo número: '))
    soma  = valo1 +  valo2 
    print(f'O valor é {soma}')
elif opc == 2:
    num1=float(input('Digite o primeiro número:'))
    num2=float(input('Digite o segundo número:'))
    subtracao= num1-num2
    print(f'O valor é {subtracao}')
elif opc == 3:
    val1=float(input('Digite o primeiro número:'))
    val2=float(input('Digite o segundo número:'))
    multiplicao=val1*val2
    print(f'O valor é {multiplicao}')
elif opc == 4:
    nu1=float(input('Digite o primeiro número: '))
    nu2=float(input('Digite o segundo número: '))
    divisao=nu1/nu2
    print(f'o valo é {divisao}')
else:
    print('errado')