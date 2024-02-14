import pytest

'''This is a pass test'''
def test_one_plus_one():
    assert 1 + 1 == 2

'''This is a fail test, change the  expected value to make it fail.'''
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

'''This is a test case with an exception'''
def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)

'''Parameterized test case'''
# Multiplication test ideas:
# Two positive intergers
# Identity: multiply by 1
# Zero: ,ultiply by 0
# Positive by negative
# Negative by negative
# Floats

products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]

## This is a pytest decorator that parameterizes the test_multiplication function below. The @pytest.mark.parametrize decorator takes two arguments: the name of @pytest.mark.parametrize("a,b,product", products)
@pytest.mark.parametrize('a,b,product', products)
def test_multiplication(a, b, product):
    assert a * b == product