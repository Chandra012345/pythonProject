import math_fun

def test_math():
    assert math_fun.add(3,5)==8
    assert math_fun.add(5)==10

def test_multi():
    assert math_fun.multiplication(5,3)==15
    assert math_fun.multiplication(3)==6