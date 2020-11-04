# 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
lista = []
'''for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    for i, v in enumerate(lista):
        if numero < v:
            lista.insert(i, numero)
            break
    else:
        lista.append(numero)'''
for c in range(0, 5):
    numero = int(input('Digite um número: '))
    if c == 0 or numero > lista[-1]:# Para a primeira e última posição
        lista.append(numero)
        print(f'Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista): # Para verificar o meio
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adiciona na {pos} da lista')
                break
            pos += 1
print(lista)
