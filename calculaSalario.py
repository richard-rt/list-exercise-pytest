'''
Faça uma função que efetua o cálculo do salário líquido de um professor. Os dados fornecidos serão:
valor hora aula, número de aulas dadas e o percentual de desconto do INSS.
'''

def calculaSalarioProfessor(valorHoraAula, numAulas, percentualInss):
    salarioSemDesconto = valorHoraAula * numAulas
    descontoInss =  percentualInss / 100 * salarioSemDesconto
    salarioComDesconto = salarioSemDesconto - descontoInss
    valor_formatado = float("{:.2f}".format(salarioComDesconto))
    return valor_formatado