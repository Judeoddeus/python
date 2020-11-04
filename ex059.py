# 059: Crie um programa que leia dois valores e mostre um menu na tela:
# somar; multiplicar; maior; novos números; sair do programa.
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('>>>>>Qual é a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'\033[34mA soma entre {n1} + {n2} = {soma}\033[m')
    elif opcao == 2:
        mult = n1 * n2
        print(f'\033[34mA multiplicação de {n1} X {n2} = {mult}\033[m')
    elif opcao == 3:
        maior = n1
        if n2 > n1: maior = n2
        print(f'\033[34mEntre {n1} e {n2} o MAIOR é {maior}\033[m')
    elif opcao == 4:
        print('Informe novos números')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Opção Inválida. Tente outra vez!')
    print('=*' * 15)
print('Encerrando programa...')
sleep(1)
print('Programa finalizado.')
