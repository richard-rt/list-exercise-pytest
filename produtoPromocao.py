'''Faça uma função que leia dois números reais, um será o valor de um produto e o outro o valor do
desconto que esse produto está recebendo. Devolva quantos reais o produto custa na promoção.'''

def descontoProduto(valorProduto, valorDesconto):
    produtoComDesconto = float("{:.2f}".format(valorProduto - valorDesconto))
    return produtoComDesconto
