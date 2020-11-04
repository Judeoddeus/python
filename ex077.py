lista = ('aprender', 'programar', 'libguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in lista:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for vogais in palavra:
        if vogais in 'aeiou':
            print(f'{vogais}', end=' ')

