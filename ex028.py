from time import sleep
from random import randint

print(':=' * 25)
print('\033[1;36mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print(':=' * 25)
n = int(input('Em que número eu pensei? '))
pc = randint(0, 5)
print('Processando...')
sleep(1)
if n == pc:
    print('\033[1;33mParabéns!\033[m Você consegui acertar!')
else:
    print(f'\033[1;33mErrou!\033[m Eu pensei no número {pc}.')
