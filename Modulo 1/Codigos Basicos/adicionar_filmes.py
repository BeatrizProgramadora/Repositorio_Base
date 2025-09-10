quantidade_de_filmes= int(input('digite quantos filmes quer adicionar: '))
contador=1
filmes=[]
while contador<=quantidade_de_filmes:
    filme= input(f'digite o nome do filme {contador}: ')
    filmes.append(filme) 
    contador= contador+1

print(filmes)
