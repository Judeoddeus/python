# 035: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
print('='*20)
print('Analisador de ')
a = float(input('Informe a primeira reta: '))
b = float(input('Informe a segunda reta: '))
c = float(input('Informe a terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('As retas \033[1;35mpodem\033[m formar um triângulo.')
else:
    print('As retas \033[1;34mnão pordem\033[m formar um triângulo.')
