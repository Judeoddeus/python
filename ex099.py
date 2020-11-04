# 99: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(*valores):
    print('-=' * 20)
    print('Analisando os valores mostrados...')
    m = 0
    for numero in valores:
        print(f'{numero}', end=' ')
        m = max(valores)
    print(f'Foram informados {len(valores)} valores ao todo')
    print(f'O maior valor informado foi o {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


''' Testanto o maior valor dentro da tupla
if cont == 0:
    m = valores
else:
    if valores > maior:
        m = valores
cont += 1
'''