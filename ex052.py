# 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[36m', end=' ')
    print(c, end=' ')
print(f'\033[m\nO número {num} foi divisível {cont} vezes')
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')
