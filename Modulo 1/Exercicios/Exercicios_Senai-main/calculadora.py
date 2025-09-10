continuar = 's'
while continuar == 's':
    print ('|-----------------------|')
    print ('|Calculadora')
    print ("|-----------------------|")
    print ('|1- Soma')
    print ('|2- Subtração')
    print ('|3- Multiplicação')
    print ('|4- Divisão')
    print ('|-----------------------|')
    opcoes= input ("escolha uma das opções ")
    n1= float(input('escolha o primeiro número '))
    n2= float(input ('escolha o segundo número '))
    if opcoes=='1':
        print ('o resultado é', n1+n2)
    elif opcoes=='2':
        print  ('o resultado é', n1-n2)
    elif opcoes=='3':
        print ('o resultado é',n1*n2)
    elif opcoes=='4':
        print('o resultado é',n1/n2)
    else:
        print("tente outra opção")
    
    continuar= input('deseja continuar? (s ou n) ') 



print ('fim do programa')
  
