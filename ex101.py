# 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano
# de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
# voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(anoNasc):
    from _datetime import datetime
    idade = datetime.now().year - anoNasc
    if 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa Principal
nasc = (int(input('Em que ano você nasceu? ')))
print(voto(nasc))
