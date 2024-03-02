import pytest
from produtoPromocao import descontoProduto

def test_um():
    assert descontoProduto(500.00, 50.00) == 450.00

def test_dois():
    assert descontoProduto(10500.00, 500.00) == 10000.00

def test_tres():
    assert descontoProduto(90.00, 0.80) == 89.20
