# 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
# e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da
# lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados
# pela função anterior.

# Funções para sortear e somar
from random import randint
numeros = []


def sorteia(lista):
    print(f'Sorteando {len(lista)} valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores de {lista}, temos {soma}.')


sorteia(numeros)
somaPar(numeros)



