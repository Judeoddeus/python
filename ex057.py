# 057: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe seu sexo [F / M]: ')).strip().upper()[0]
while sexo not in 'MnFn':
    print('Dados inválidos. Por favor , informe seu sexo.')
    sexo = str(input('[F/M]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
