import unittest
from calculator_v2 import Calculator

class TestsCalculatorV2(unittest.TestCase):
    def test_add_functionality(self):
        calc1=Calculator(10,30)
        result=calc1.calc_add()
        assert result==40

    def test_add_functionality_one_negative_number(self):
        cal2=Calculator(10,-30)
        result=cal2.calc_add()
        assert result==-20
