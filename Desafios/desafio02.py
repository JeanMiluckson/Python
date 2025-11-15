#Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#  e todas as suas informações possiveis sobre ela
print('Descobrindo a primitiva do que escreveu')
teclado=(input('Digite algo: '))
print('O tipo primitivo dele eh: ', type(teclado))
print('Eh um numero? ', teclado.isnumeric())
print('Tem maiusculo? ', teclado.isupper())
print('Tem minusculo? ', teclado.isalpha())
print('Eh alfabetico? ', teclado.islower())
print('Eh alfanumerico? ', teclado.isalnum())
print('Tem espaco? ', teclado.isspace())
print('Esta capitalizada? ', teclado.istitle())

