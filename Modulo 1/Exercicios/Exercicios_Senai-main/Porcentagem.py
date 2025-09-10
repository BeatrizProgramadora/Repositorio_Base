# Cálculo de Porcentagem de um Número.
# • O programa deve calcular e exibir o valor que corresponde a essa
# porcentagem do total. Exemplo: se o usuário digitar 200 como
# valor total e 15 como porcentagem, o programa deverá calcular
# que 15% de 200 é 30.
# • Exemplo de fórmula:
# valor_parte = valor_total * (porcentagem / 100)

valor_total= float(input('Digite o valor total  '))
Porcentagem= float(input ('digite a porcentagem  '))
resultado= round (float(Porcentagem/100)*valor_total)
print (resultado)