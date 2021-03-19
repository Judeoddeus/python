# 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um
# valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo
# do fatorial.


def fatorial(n, show=False):
    """
    -> Calcular o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial do número calculado.
    """
    f = 1
    for c in range(n, 0, - 1):
        f *= c
        if show == True:
            print(f'{c} x 'if c > 1 else '= ', end='')
    return f


# Programa Principal
print(fatorial(5))
