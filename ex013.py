# 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Salário R$: '))
aumento = salario * 0.15
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${salario + aumento:.2f}')
