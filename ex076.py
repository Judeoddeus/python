print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)
listagem = ("Lápis", 1.75,
            "Borracha", 2.00,
            "Caderno",15.90,
            "Estoujo", 25.00,
            "Transferidor",  4.20,
            "Compasso", 9.99,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "Livro", 34.90)

for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end=' ')
    else:
        print(f'R${listagem[posicao]:>7.2f}')
