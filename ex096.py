# 96: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}mº.')


# Programa Principal
print('   Controle de terreno')
print('-' * 30)
# area(larg=float(input('LARGURA: ')), comp=float(input('COMPRIMENTO: ')))
l = float(input('LARGURA: '))
c = float(input('COMPRIMENTO: '))
area(l, c)
