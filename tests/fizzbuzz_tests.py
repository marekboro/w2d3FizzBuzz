import unittest
from src.fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):

    def test_check_return_input(self):
        self.assertEqual('7', fizzbuzz(7))

    #def test_return_fizz_divide_by_3(self):
    #    self.assertEqual