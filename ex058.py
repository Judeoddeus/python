from random import randint

computador = randint(0, 10)
print('''\033[1;36mSOU SEU COMPUTADOR...\033[m
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
acertou = False
cont = 0
while not acertou:
    palpite = int(input('Qual é seu palpite? '))
    cont += 1
    if palpite == computador:
        acertou = True
    else:
        if palpite < computador:
            print('Mais...Tente mais uma vez.')
        elif palpite > computador:
            print('Menos...Tente mais uma vez.')
    print('=' * 20)
print(f'Acertou com {cont} tentativas.Parabéns!')


