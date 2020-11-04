# 038: Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem: # - O primeiro valor é maior
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são iguais!')

