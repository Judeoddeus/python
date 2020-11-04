# 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
jogo = []
n = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(1, n + 1):
    for i in range(6):
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogo.sort()
    print(f'Jogo {c}: {jogo}')
    jogo.clear()
    sleep(1)

print('-'*5, '>>> BOA SORTE! <<<', '-'*5)




'''
lista, jogos = [], []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont == 6: break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: {v}')
    sleep(1)
print('-'*5, '>>> BOA SORTE! <<<', '-'*5)'''