# 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
maiores = menores = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}º pessoa nasceu?  '))
    idade = atual - nasc
    if idade >= 21:
        maiores += 1 # mais uma pessoa maior de idade
    else:
        menores += 1
print(f'Ao todo tivemos {maiores} maiores de idade')
print(f'Ao todo tivemos {menores} menores de idade')


