from random import randint
cont = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDE!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! venceu {cont} vezes.')



'''
print('-_-'*10)
print('VAMOS JOGAR \033[34mPAR\033[m OU \033[33mIMPAR\033[m')
print('-_-'*10)
venceu = total = 0
while True:
    jogador = int(input('Digite um valor: '))
    escolha = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
    computador = randint(0, 10)
    soma = jogador + computador
    print('-' * 40)
    if soma % 2 == 0:
        jogada = 'P'
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu PAR')
        print('-' * 40)
    else:
        jogada = 'I'
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu IMPAR')
        print('-' * 40)
    if escolha == jogada:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        total += 1
        print('-' * 40)
    if jogada != escolha:
        break
print('Você PERDEU!')
print('-'*40)
print(f'GAME OVER! venceu {total} vezes.')
'''

