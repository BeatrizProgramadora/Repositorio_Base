import csv

dados= [
    ['Nome','Apelido','Idade'],
    ['Meg Maria Mazoni','Meg','8'],
    ['Marisa Mazoni','Isa','7']
]

with open('gatos.csv','w',newline='',encoding='utf-8')as arquivo:
    escritor=csv.writer(arquivo)
    escritor.writerows(dados)

