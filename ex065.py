# 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = media = cont = maior = menor = 0
continuar = 'S'
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média foi de {media:.2f}')
print(f'O MAIOR valor foi {maior} e o MENOR foi {menor}')

