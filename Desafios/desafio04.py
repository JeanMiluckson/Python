#Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
n1 = int(input('Digite um numero: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)
print(f'O dobro de {n1} eh = {dobro}')
print(f'O triplo de {n1} eh = {triplo}')
print(f'A raiz quadrada de {n1} eh = {raiz:.2f}')
