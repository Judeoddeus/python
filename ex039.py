# 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou o prazo.
from datetime import date
anoNasc = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
print(f'Quem nasceu em {anoNasc} tem {idade} anos em {anoAtual}')
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade > 18:
    alistamento = idade - 18
    print(f'Você já deveria ter se alistado há {alistamento} anos.')
    print(f'Seu alistamento foi em {anoAtual - alistamento}')
elif idade < 18:
    alistamento = 18 - idade
    print(f'Você ainda tem {alistamento} anos para se alistar.')
    print(f'Seu alistamento será em {anoAtual + alistamento}.')

