# 073: Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
times = ('Grêmio', 'Fluminense', 'Bahia', 'Bragantino-SP',
         'Athético-PR', 'Vasco da Gama', 'Santos', 'Fortaleza',
         'Atlético_GO', 'Palmeiras', 'Corinthians', 'Chapecoense',
         'São Paulo', 'Atlético-MG', 'Coririba', 'Ceará SC', 'Goiás',
         'Botafogo', 'Sport Recife', 'Internacional')
#for t in times:
    #print(t)
print('-='*30)
print(f'Lista de times do Brasileirão: {times}')
print('-='*30)
print(f'Os 5 primeiros são: {times[:5]}')
print('-='*30)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*30)
print(f'Os times em Ordem Alfabética: {sorted(times)}')
print('-='*30)
print(f'O  Chapecoense está na {times.index("Chapecoense") + 1}º posição')
