from unittest import TestCase
from functions import divide,multiply


class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expected_results = 5.0
        self.assertAlmostEqual(divide(dividend,divisor),expected_results,delta=0.0001)
    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEqual(divide(dividend,divisor),expected_result,delta=0.001)
    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = 1
        expected_result = 0
        self.assertAlmostEqual(divide(dividend,divisor),expected_result,delta=0.1)
    
    def test_divide_error_on_zero(self):
        self.assertRaises(ValueError,lambda:divide(20,0))
        with self.assertRaises(ValueError):
            divide(23,0)

    def test_multiply_empty(self):
        with self.assertRaises(ValueError ):
            multiply()
    
    def test_multiply_single_value(self):
        expected = 15
        self.assertEqual(multiply(expected),expected)
    
    def test_multiply(self):
        inputs = (3,5)
        expected = 15
        self.assertEqual(multiply(*inputs),expected)
    

    def test_multiply_zero(self):
        inputs = (2,23,9,0)
        expected = 0
        self.assertEqual(multiply(*inputs),expected)
    
    def test_multiply_negative_value(self):
        inputs = (2,2,1,-1)
        expected = -4
        self.assertEqual(multiply(*inputs),expected)
