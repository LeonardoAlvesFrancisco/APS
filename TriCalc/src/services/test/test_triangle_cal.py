import pytest
from services.triangle_calculator.calculator import TriangleCalculator
@pytest.fixture
def triangle_calculator():
    return TriangleCalculator()
    
def test_validate_triangle( triangle_calculator):
    """Este teste verifica se os objetos são ou não triângulos."""
    assert triangle_calculator.validate_triangle(3, 4, 5) == True
    assert triangle_calculator.validate_triangle(1, 1, 3) == False
    assert triangle_calculator.validate_triangle(0, 0, 0) == False
    assert triangle_calculator.validate_triangle(-1, 2, 3) == False    

def test_get_triangle_type( triangle_calculator):
    """Este teste verifica qual o tipo do triangulo calculado."""
    assert triangle_calculator.get_triangle_type(3, 3, 3) == "Equilátero"
    assert triangle_calculator.get_triangle_type(3, 3, 4) == "Isósceles"
    assert triangle_calculator.get_triangle_type(3, 4, 5) == "Escaleno"
    assert triangle_calculator.get_triangle_type(1, 1, 3) ==  "Triangulo invalido, forneça outras informações."

def test_get_triangle_type_invalid_input( triangle_calculator):
    """Este teste verifica os inputs invalidos para os triangulos"""
    assert triangle_calculator.get_triangle_type(0, 0, 0) ==  "Triangulo invalido, forneça outras informações."
    assert triangle_calculator.get_triangle_type(-1, 2, 3) == "Triangulo invalido, forneça outras informações."

def test_get_triangle_type_equilateral(triangle_calculator):
    """Este teste verifica se os triangulos são equilateros"""
    assert triangle_calculator.get_triangle_type(3, 3, 3) == "Equilátero"
    assert triangle_calculator.get_triangle_type(8, 8, 8) == "Equilátero"

def test_get_triangle_type_isosceles(triangle_calculator):
    """Este teste verifica se os triângulos são isósceles."""
    assert triangle_calculator.get_triangle_type(3, 3, 4) == "Isósceles"
    assert triangle_calculator.get_triangle_type(7, 7, 9) == "Isósceles"

def test_get_triangle_type_scalene(triangle_calculator):
    """Este teste verifica se os triângulos são escaleno."""
    assert triangle_calculator.get_triangle_type(3, 4, 5) == "Escaleno"
    assert triangle_calculator.get_triangle_type(5, 12, 13) == "Escaleno"
    assert triangle_calculator.get_triangle_type(9, 12, 15) == "Escaleno"

@pytest.mark.xfail(condition=lambda: True, reason='Esperamos que o teste falhe')
def test_expect_triangle_to_be_invalid(triangle_calculator):
    assert triangle_calculator.validate_triangle(0, 0, 0) == False
