num = int(input('Digite um número inteiro qualquer: '))
if num % 2 == 0:
    print(f'O número {num} é \033[33mPAR\033[m')
else:
    print(f'O número {num} é \033[36mIMPAR\033[m')
