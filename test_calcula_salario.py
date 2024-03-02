import pytest
from calculaSalario import calculaSalarioProfessor

def test_um():
    assert calculaSalarioProfessor(6.25, 160, 1.3) == 987.00

def test_dois():
    assert calculaSalarioProfessor(20.5, 240, 1.7) == 4836.36

def test_tres():
    assert calculaSalarioProfessor(13.9, 200, 6.48) == 2599.86
