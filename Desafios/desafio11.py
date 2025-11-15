#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
salario = float(input('Digite o salario: '))
aumento = salario * 0.15
novoSalario = salario + aumento 
print(f'Novo salario de: {novoSalario:.2f}')