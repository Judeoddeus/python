print('Gerador de P.A')
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão da P.A: '))
termo = primeiroTermo
c = 1
while c <= 10:
    print(termo, end=' ')
    termo += razao
    c += 1