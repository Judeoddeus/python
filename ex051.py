# 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimotermo = primeiroTermo + (10 - 1) * razao
for c in range(primeiroTermo, decimotermo + 1, razao):
    print(c, end=' -> ')
print('Acabou.')
