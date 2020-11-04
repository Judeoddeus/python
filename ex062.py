#  062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#  O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiroTermo
c = 1
total = 0 # conta quantos termos esta sendo usado
novoTermo = 10
while novoTermo != 0:
    total = total + novoTermo
    while c <= total:
        print(termo, end='-> ')
        termo += razao
        c += 1
    print('PAUSA')
    novoTermo = int(input('quantos termos você quer mostrar mais? '))
print(f'A prograssão foi finalizada com {total} termos')
print('FIM')
