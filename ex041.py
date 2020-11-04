#  041: A Confederação Nacional de Natação precisa de um programa que leia
#  o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
from datetime import date
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    classificacao = 'Mirim'
elif idade <= 14:
    classificacao = 'Infantil'
elif idade <= 19:
    classificacao = 'Junior'
elif idade <= 25:
    classificacao = 'Sênior'
else:
    classificacao = 'Master'
print(f'Classificação: {classificacao}')

