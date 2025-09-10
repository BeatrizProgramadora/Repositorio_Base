# Cálculo de Desconto em um Produto.
# • Se o usuário informar que o preço original é 100 e o desconto é
# de 20%, o programa deverá calcular que o valor do desconto é 20
# e, consequentemente, o preço final será 80.
# • Exemplo de fórmula:
# valor_desconto = preco_original * (porcentagem_desconto / 100)
# preco_final = preco_original - valor_desconto


Nome_do_produto= input("digite o nome do produto  ")
preço_original= float(input("digite o preço original  "))
porcentagem_de_desconto=  round(float(input("digite a porcentagem de desconto  ")))
desconto= round (float(porcentagem_de_desconto/100)*preço_original)
preço_final= round (float(preço_original-desconto ))
print ("o produto", Nome_do_produto,"com desconto de", porcentagem_de_desconto,"% custará R$",preço_final)