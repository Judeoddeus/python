# 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes
r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Os seguimentos forma um triângulo EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('Os seguimentos forma um triângulo ESCALENO!')
    else:
        print('Os seguimentos forma um triângulo ISÓCELES')
else:
    print('Os seguimentos não formam um triângulo.')
