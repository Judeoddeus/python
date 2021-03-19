# 105 – Analisando notas e gerando Dicionários


def notas(*n, sit=False):
    """
    -> Função notas analisa a situação das notas de cada aluno.
    :param n: Recebe uma ou mais notas dos alunos.
    :param sit: Valor (Opcional), que indica se deve ou não mostrar a situação (Boa, Razoável, Ruim) do aluno.
    :return: Retorna um dicionário com várias informações da turma.
    """
    geral = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n) / len(n)}
    if sit:
        if geral['media'] >= 7:
            geral['situação'] = 'Boa'
        elif 5 < geral['media'] < 7:
            geral['situação'] = 'Razoável'
        else:
            geral['situação'] = 'Ruim'
    return geral


# Programa Principal
resp = notas(5.5, 2.5, 8.2, 9, sit=True)
print(resp)
