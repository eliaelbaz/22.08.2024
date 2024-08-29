import pytest
import calculator

def test_calculator_power():
    base: int = 4
    exponent: int = 2
    expected: int = 16
    actual: int = calculator.power(base, exponent)
    assert actual == expected

def test_calculator_sqrt():
    number: int = 25
    expected: int = 5
    actual: int = calculator.sqrt(number)
    assert actual == expected

def test_calculator_sqrt_negative():
    # Arrange
    number: int = -5
    with pytest.raises(ValueError) as ex:
        actual: int = calculator.sqrt(number)
    assert str(ex.value) == "math domain error"

def test_calculator_is_prime_true():
    number: int = 2
    expected: bool = True
    actual: bool = calculator.is_prime(number)
    assert actual == expected

def test_calculator_is_prime_false():
    number: int = 1
    expected: bool = False
    actual: bool = calculator.is_prime(number)
    assert actual == expected

def test_calculator_factorial():
    number: int = 5
    expected: int = 120
    actual: int = calculator.factorial(number)
    assert actual == expected

def test_calculator_factorial_negative():
    number: int = -3
    with pytest.raises(ValueError) as ex:
        actual: int = calculator.factorial(number)
    assert str(ex.value) == "factorial not defined for negative values"
