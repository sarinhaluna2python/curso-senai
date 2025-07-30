#Cálculo de Porcentagem de um Número.
#• O programa deve calcular e exibir o valor que corresponde a essa
# porcentagem do total. Exemplo: se o usuário digitar 200 como
# valor total e 15 como porcentagem, o programa deverá calcular
# que 15% de 200 é 30.
# • Exemplo de fórmula:

# valor_parte = valor_total * (porcentagem / 100)

con1= float(input("Valor da casa ? "))
con2= float(input('Porcentagem para o banco ?'))

resp = con1 * (con2 / 100) #FORMULA PARA PORCENTAGEM 

print('O valor da porcentegem pago para o banco é', resp )
