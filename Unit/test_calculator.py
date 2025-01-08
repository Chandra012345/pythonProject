import unittest
from calculator import calc_add

class TestsCalculator(unittest.TestCase):
    def test_add_functionality(self):
        result=calc_add(10,20)
        assert result==30

    def test_add_functionality_two_negative_numbers(self):
        result=calc_add(-10,-20)
        assert result==-30