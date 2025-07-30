# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|______________________________|')
print('|___________CADASTRO___________|')
print('|______________________________|')
nome = input('| Nome:')
idade = input('| Idade:')
email = input('| Email:')
senha = input('| Senha:')

print('|______________________________|')
print('|______USUÁRIO CADASTRADO______|')
print('| Seja bem vindo(a)', nome+'!')
print('|',email)
print('|______________________________|')