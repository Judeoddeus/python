# 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a
# ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nomeJogador='<desconhecido>', gols=0):
    print(f'O jogador {nomeJogador} fez {gols} gol(s) no campeonato.')


# Programa Principal
j = str(input('Nome do Jogador: ')).capitalize()
g = str(input('Número de gols: '))
if g.isnumeric():  # Verifica se o g é numérico, sendo passa para valor inteiro
    g = int(g)
else:
    g = 0  # Se não for retorna 0
if j.strip() == '':  # Verifica se j está vazio, estando retorna apenas os gols
    ficha(gols=g)
else:  # Se não estiver vazio retorna os param
    ficha(j, g)
