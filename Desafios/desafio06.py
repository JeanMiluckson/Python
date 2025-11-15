#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
metros = int(input('Metros: '))
conversaocm = metros * 100
conversaoml = metros * 1000
print(f'conversao para Centimetros = {conversaocm} cm')
print(f'Conversao para milimetros = {conversaoml} mm')
