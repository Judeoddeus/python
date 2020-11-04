# 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TERSOURA
Qual é a sua jogada? '''))
sleep(0.5)
print('\033[33mJO')
sleep(1)
print('\033[34mKEN')
sleep(1)
print('\033[35mPOW!!\033[m')
sleep(1)
print('=-' * 30)
print(f'Jogador escolheu {itens[jogador]} \nComputador escolheu {itens[computador]}')
print('=-' * 30)
if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA inválida!')
elif computador == 1:
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
       print('JOGADOR VENCE')
    elif jogador == 0:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA inválida!')
elif computador == 2:
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
       print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA inválida!')

