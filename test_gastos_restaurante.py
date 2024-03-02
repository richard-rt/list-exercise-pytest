import pytest
from gastosRestaurante import calculaTotalConta

def test_um():
    totalConta, valorGorjeta = calculaTotalConta(75.00)
    assert totalConta == 82.50
    assert valorGorjeta == 7.5

def test_dois():
    totalConta, valorGorjeta = calculaTotalConta(125)
    assert totalConta == 137.50
    assert valorGorjeta == 12.5

def test_tres():
    totalConta, valorGorjeta = calculaTotalConta(350.87)
    assert totalConta == 385.96
    assert valorGorjeta == 35.09