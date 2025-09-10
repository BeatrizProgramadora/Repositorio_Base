print ('opçoes:')
print ('1-Real para dólar')
print("2-Dólar para real")

opcao= (input("informe a opção "))

if opcao== '1':
    cotacao_dolar= float(input('digite a cotação do dolar '))
    valor_real= float(input('digite o valor em reais que quer converter '))
    valor_convertido= float(cotacao_dolar*valor_real)
    print ('convertido fica', valor_convertido)

elif opcao== '2':
    cotacao_dolar= float(input('digite a cotação do dolar '))
    valor_dolar= float(input('digite o valor em dolares que quer converter '))
    valor_convertido= round(float(valor_dolar/cotacao_dolar))
    print ('convertido fica',valor_convertido)