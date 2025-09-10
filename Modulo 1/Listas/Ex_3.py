# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE
quantidade_filmes=int(input('Quantos filmes deseja adicionar? '))
contador=1
while contador<=(quantidade_filmes):
    filme=input(f'Digite o nome do filme {contador}: ')
    filmes.append(filme)
    contador=contador+1
print(filmes)





# LOOP FOR

for i in filmes:
    filme=input('Digite o nome do{i+1} filme: ')
    filmes.append(filme)
print(filmes)

