from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
sleep(1)
print(f'Seu nome em maiúscula é {nome.upper()}')
print(f'Seu nome em minúscula é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome) - nome.count(" ")} letras')
#nome.find(' ') - Me encontre o primeiro espaço "Conta a quantidade de letras até o 1º espaço"
n = nome.split()
print(f'Seu primeiro nome é {n[0]} e ele tem {len(n[0])} letras')


