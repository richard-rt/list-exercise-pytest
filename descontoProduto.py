'''Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo
desconto aos clientes. Faça uma função que receba um valor de um produto e devolva um novo valor
tendo em vista que o desconto foi de 9%.'''

def descontoProduto(valorProduto):
    valorDesconto = float("{:.2f}".format(valorProduto / 100 * 9))
    novoValor = float("{:.2f}".format(valorProduto - valorDesconto))
    return novoValor, valorDesconto
