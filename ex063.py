# 063: Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
print('-' * 30)
print('Sequência de Fibionacci')
print('-' * 30)
termos = int(input('Quantos termos você quer mostrar? '))
a = 0
b = 1
cont = 3
print(f'{a} -> {b}', end=' -> ')
while cont <= termos:
    c = a + b
    print(c, end=' -> ')
    a = b
    b = c
    cont += 1
print('FIM')
