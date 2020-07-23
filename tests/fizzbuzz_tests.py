import unittest
from src.fizzbuzz import fizzbuzz


class TestFizzbuzz(unittest.TestCase):
    def test_check_return_input(self):
        self.assertEqual("7", fizzbuzz(7))

    def test_return_fizz_divide_by_3_3(self):
        self.assertEqual("Fizz", fizzbuzz(3))

    def test_return_fizz_divide_by_3_6(self):
        self.assertEqual("Fizz", fizzbuzz(6))

    def test_return_buzz_divisible_by_5_5(self):
        self.assertEqual("Buzz", fizzbuzz(5))