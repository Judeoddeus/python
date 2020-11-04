# 034: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00,# calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Informe o salário R$'))
if salario > 1250:
    novo = (salario * 0.1) + salario
    print('O aumento foi de 10%')
else:
    novo = (salario * 0.15) + salario
    print('O aumento foi de 15%')
print(f'O funcionário recebia R${salario:.2f} e passará a receber R${novo:.2f} com aumento.')