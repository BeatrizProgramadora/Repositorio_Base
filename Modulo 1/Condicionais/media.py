from colorama import init,Fore


init(autoreset=True)

nome= input ('Qual é o nome do aluno? ')
nota1= int (input('Qual é a nota da primeira prova? '))
nota2= int (input('Qual é a nota da segunda prova? '))
nota3= int (input ('Qual é a nota da terceira prova? '))
media= round(nota1+nota2+nota3)/3
print ('Aluno', nome,'\nMedia: ', media)
if media >=5:
 print(Fore.GREEN+'Aluno aprovado')
else:
 print(Fore.RED+'Aluno reprovado')