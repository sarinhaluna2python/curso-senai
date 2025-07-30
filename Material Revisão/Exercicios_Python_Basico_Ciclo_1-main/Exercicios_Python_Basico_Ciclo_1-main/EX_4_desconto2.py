# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
nome= input('o que vamos comprar')
valor= float(input('preço do produto? '))
desconto=int(input('porcentagem de desconto? '))

soma = valor * (desconto/100)
total= valor - soma 

print('o ',nome,'com',soma,'de desconto custará ', total )

