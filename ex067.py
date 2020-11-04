while True:
    tabuada = int(input('Quer a tabuada de qual número? '))
    if tabuada < 0: break
    print('-' * 40)
    for c in range(0, 11):
        print(f'{tabuada} x {c:2} = {tabuada * c}')
    print('-' * 40)
print('Programa de tabuada encerrado.')
