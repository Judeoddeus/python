# 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘
# a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)


def leiaInt(valor):
    while True:
        i = str(input(valor))  # i recebe o valor como string.
        if i.isnumeric():  # Verifica se o valor é númerico, sendo, converte a str para int e
            i = int(i)  # finaliza o programa
            break
        else:  # Não sendo, printa a mensagem de erro.
            print('\033[31mERRO! Digite um número válido.\033[m')
    return i


n = leiaInt('Digite um número: ')
print(f'O número digitado foi {n}')
