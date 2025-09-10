altura= float(input ('Qual sua altura?  '))
peso= float(input('Qual é seu peso?  '))
IMC= round (peso/(altura*altura))
print ('seu IMC é', IMC)
if IMC<= 18.5:
 print ("você está abaixo do peso")
elif  18.5 <= IMC <25:
 print ('Você está no peso normal')
elif  25 <= IMC <30:
 print ('Você está com sobrepeso')
elif  30 <= IMC < 35:
 print ('Você está com obesidade grau 1')
elif  35 <=IMC < 40:
 print ('Você está com obesidade grau 2')
else: 
  print ('Você está com obesidade grau 3')