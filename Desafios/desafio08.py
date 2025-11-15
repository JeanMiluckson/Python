#Crie um programa que leia quanto dinheiro uma pessoa tem na carteina
# e mostre quantos dólares ela pode comprar. Considere US$1.00 = 5.30
saldo = float(input('Digite o seu saldo total: '))
compra = saldo / 5.30
print(f'Com um saldo de {saldo:.2f}, voce pode comprar {compra:.2f} dólares')