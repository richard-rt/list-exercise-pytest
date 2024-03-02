'''Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% de comissão para o
garçom. Faça uma função que receba o valor gasto com despesas realizadas em um restaurante e
devolva o valor total da conta e o valor da gorjeta.'''

def calculaTotalConta(valorDespesa):
    valorGorjeta = float("{:.2f}".format(valorDespesa * 0.1))
    valorTotalConta = float("{:.2f}".format(valorDespesa + valorGorjeta))
    print(valorGorjeta,valorTotalConta)
    return valorTotalConta, valorGorjeta

