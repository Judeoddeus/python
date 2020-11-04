# 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
n = str(input('Digite uma frase: ')).strip().upper()
palavra = n.split()
frase = ''.join(palavra)
#inverso = ''
print(f'O inverso de {frase} é {frase[::-1]}')
if frase == frase[::-1]:
    print('A frase é um PALINDROMO')
else:
    print('A frase NÃO é um PALINDROMO')

#n = str(input('Digite uma frase: ')).strip().upper()
#palavra = n.split()
#frase = ''.join(palavra)
#inverso = ''
#for c in range(len(frase) -1, -1, -1):
    #inverso += frase[c]
#print(f'O inverso de {frase} é {inverso}')
#if inverso == frase:
    #print('A frase é um PALINDROMO')
#else:
    #print('A frase NÃO é um PALINDROMO')