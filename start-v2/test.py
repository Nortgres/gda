import unittest
from my_sum import sum
from fractions import Fraction
class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__== "__main__":
    unittest.main()

# python -m unittest test
# python -m unittest -v test #- с выводом
# python -m unittest discover #- автоматическое обнаружение тестов.