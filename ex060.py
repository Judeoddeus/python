# 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''
##### MEU MODO #####
from math import factorial
n = int(input('Informe um número para calcular seu fatorial: '))
c = 1
f = factorial(n)
print(f'Calculando {n}! =', end=' ')
while c <= n:
    print(n, end=' x ' if n > 1 else ' = ')
    n -= 1
print(f'{f}')

##### MODO DO GUANABARA #####
n = int(input('Informe um número para calcular seu fatorial: '))
c = n
f = 1  # multiplicaçao ou divisão limpa começa com 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(c, end=' x ' if c > 1 else ' = ')
    f = f * c
    c -= 1
print(f, end='')
'''
##### DESAFIO FOR ######
n = int(input('Informe um número para calcular seu fatorial: '))
f = 1
for c in range(n, 0, -1):
    print(c, end=' x ' if c > 1 else ' = ')
    f = f * c
print(f, end='')
