# 97: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
# como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreva(‘Olá, Mundo!’) Saída:  Olá, Mundo!
def escreva(texto):
    tam = len(texto)
    print('-'* tam)
    print(f'{texto}')
    print('-'* tam)


escreva('Olá, Mundo!')
escreva('Cruso em Python')
escreva('Junie')

