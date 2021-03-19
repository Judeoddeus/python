# 106 – Interactive helping system in Python com cores de fundo diferentes
cores = ('\033[0;m',  # cor 0
         '\033[0;30;44m',  # cor 1 azul
         '\033[7;38m',  # cor 2 branca
         '\033[0;30;41m',  # cor 3 vermelha
         '\033[0;30;47m',  # cor 4 cinza
         )


def titulo(texto, cor=0):
    tam = len(texto) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f' {texto}')
    print('~' * tam)
    print(cores[0], end='')


def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4)
    print(cores[2], end='')
    help(comando)
    print(cores[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    resp = str((input('Função ou Biblioteca > ')))
    if resp.upper() in 'FIM':
        break
    else:
        ajuda(resp)

titulo('ATÉ LOGO!', 3)
