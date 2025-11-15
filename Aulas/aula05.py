#operadores aritimeticos
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2 
divisaoInteira = n1 // n2
restodaDivisao = n1 % n2
potencia = n1 ** n2
print(f' Soma = {soma}\n', f'Subtracao = {subtracao}\n' ,f'Multiplicacao = {multiplicacao}\n', f'Divisao = {divisao:.2f}\n', end = '')
print(f'DivisaoInteira = {divisaoInteira}\n', f'Resto Da Divisao = {restodaDivisao}\n', f'potencia = {potencia}\n')