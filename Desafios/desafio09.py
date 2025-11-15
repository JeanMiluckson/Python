#Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta, pinta uma área de 2m^2
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura 
litros = 2.0
tinta = area / litros
print(f'A sua area eh {area:.2f}m^2')
print(f'A quantidade de tinta necessária eh {tinta:.2f} Litros')