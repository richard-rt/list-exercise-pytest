import pytest
from descontoProduto import descontoProduto

def test_um():
    novoValor, valorDesconto = descontoProduto(100)
    assert novoValor == 91.00
    assert valorDesconto == 9.00

def test_dois():
    novoValor, valorDesconto = descontoProduto(1500)
    assert novoValor == 1365.00
    assert valorDesconto == 135.00

def test_tres():
    novoValor, valorDesconto = descontoProduto(60000)
    assert novoValor == 54600.00
    assert valorDesconto == 5400.00

    


