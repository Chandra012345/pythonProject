import unittest
from calculator_v_02 import Calculator
class Testcalculatorbasefunctionality(unittest.TestCase):
    def test_add(self):
        calc=Calculator(10,20)
        result=calc.add()
        self.assertEqual(result,30)

    def test_sub(self):
        calc=Calculator(30,40)
        result=calc.sub()
        self.assertEqual(result,-10)

    def test_multi(self):
        calc=Calculator(10,20)
        result=calc.multi()
        self.assertEqual(result,200)

class TestCalculatorAddFunctionality(unittest.TestCase):
    def test_add_positive_numbers(self):
        calc=Calculator(30,40)
        result=calc.add()
        self.assertEqual(result,70)

    def test_add_one_negative_number(self):
        calc=Calculator(30,-40)
        result=calc.add()
        self.assertEqual(result,-10)

    def test_add_negative_numbers(self):
        calc=Calculator(-10,-20)
        result=calc.add()
        self.assertEqual(result,-30)