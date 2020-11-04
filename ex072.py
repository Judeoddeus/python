# 072: Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoite', ' dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre [0 - 20]: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número \033[1;34m{extenso[num]}\033[m')
    else:
        print('Tente novamente!', end='')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N': break
print('Fim do Processo.')









