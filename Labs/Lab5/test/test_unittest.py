import sys
import os
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import math_utils


class TestMathUtils(unittest.TestCase):

  def test_add(self):
    self.assertEqual(math_utils.add(2, 3), 5)
    self.assertEqual(math_utils.add(-1, 1), 0)

  def test_subtract(self):
    self.assertEqual(math_utils.subtract(9, 2), 7)

  def test_multiply(self):
    self.assertEqual(math_utils.multiply(4, 3), 12)

  def test_divide(self):
    self.assertEqual(math_utils.divide(8, 2), 4)
    with self.assertRaises(ValueError):
      math_utils.divide(8, 0)

  def test_safe_divide(self):
    self.assertEqual(math_utils.safe_divide(8, 0), 0)
    self.assertEqual(math_utils.safe_divide(8, 0, default=-1), -1)

  def test_power(self):
    self.assertEqual(math_utils.power(3, 2), 9)

  def test_square(self):
    self.assertEqual(math_utils.square(5), 25)

  def test_cube(self):
    self.assertEqual(math_utils.cube(2), 8)

  def test_modulus(self):
    self.assertEqual(math_utils.modulus(10, 4), 2)

  def test_absolute_value(self):
    self.assertEqual(math_utils.absolute_value(-7), 7)

  def test_round_number(self):
    self.assertEqual(math_utils.round_number(2.718, 2), 2.72)

  def test_floor_number(self):
    self.assertEqual(math_utils.floor_number(5.9), 5)

  def test_ceil_number(self):
    self.assertEqual(math_utils.ceil_number(5.1), 6)

  def test_average(self):
    self.assertEqual(math_utils.average(2, 4, 6, 8), 5)

  def test_maximum(self):
    self.assertEqual(math_utils.maximum(2, 7, 1), 7)

  def test_minimum(self):
    self.assertEqual(math_utils.minimum(2, 7, 1), 1)

  def test_factorial(self):
    self.assertEqual(math_utils.factorial(4), 24)

  def test_fibonacci(self):
    self.assertEqual(math_utils.fibonacci(8), 21)

  def test_is_even(self):
    self.assertTrue(math_utils.is_even(10))
    self.assertFalse(math_utils.is_even(9))

  def test_is_odd(self):
    self.assertTrue(math_utils.is_odd(9))
    self.assertFalse(math_utils.is_odd(10))

  def test_is_prime(self):
    self.assertTrue(math_utils.is_prime(13))
    self.assertFalse(math_utils.is_prime(15))

  def test_gcd(self):
    self.assertEqual(math_utils.gcd(48, 18), 6)

  def test_lcm(self):
    self.assertEqual(math_utils.lcm(4, 6), 12)

  def test_percentage(self):
    self.assertEqual(math_utils.percentage(30, 60), 50)

  def test_clamp(self):
    self.assertEqual(math_utils.clamp(15, 0, 10), 10)

  def test_invalid_inputs(self):
    with self.assertRaises(ValueError):
      math_utils.add("a", 2)
    with self.assertRaises(ValueError):
      math_utils.factorial(-3)
    with self.assertRaises(ValueError):
      math_utils.clamp(5, 10, 2)

  def test_integer_validation_errors(self):
    with self.assertRaises(ValueError):
      math_utils.is_even(2.5)
    with self.assertRaises(ValueError):
      math_utils.is_odd("3")
    with self.assertRaises(ValueError):
      math_utils.is_prime(True)
    with self.assertRaises(ValueError):
      math_utils.gcd(4.5, 2)
    with self.assertRaises(ValueError):
      math_utils.lcm(4, "6")

  def test_non_negative_integer_validation_errors(self):
    with self.assertRaises(ValueError):
      math_utils.factorial(3.5)
    with self.assertRaises(ValueError):
      math_utils.fibonacci(True)

  def test_more_invalid_numeric_inputs(self):
    with self.assertRaises(ValueError):
      math_utils.safe_divide(10, 0, default="invalid")
    with self.assertRaises(ValueError):
      math_utils.ceil_number("abc")
    with self.assertRaises(ValueError):
      math_utils.floor_number(None)

  def test_integer_validation_errors(self):
    with self.assertRaises(ValueError):
      math_utils.is_even(2.5)
    with self.assertRaises(ValueError):
      math_utils.is_odd("3")
    with self.assertRaises(ValueError):
      math_utils.is_prime(True)
    with self.assertRaises(ValueError):
      math_utils.gcd(4.5, 2)
    with self.assertRaises(ValueError):
      math_utils.lcm(4, "6")

  def test_non_negative_integer_validation_errors(self):
    with self.assertRaises(ValueError):
      math_utils.factorial(3.5)
    with self.assertRaises(ValueError):
      math_utils.fibonacci(True)

  def test_more_invalid_numeric_inputs(self):
    with self.assertRaises(ValueError):
      math_utils.safe_divide(10, 0, default="invalid")
    with self.assertRaises(ValueError):
      math_utils.ceil_number("abc")
    with self.assertRaises(ValueError):
      math_utils.floor_number(None)

  def test_average_maximum_minimum_invalid_argument_types(self):
    with self.assertRaises(ValueError):
      math_utils.average(1, "bad", 3)

    with self.assertRaises(ValueError):
      math_utils.maximum(1, True, 3)

    with self.assertRaises(ValueError):
      math_utils.minimum(1, None, 3)

  def test_bool_inputs_are_rejected_where_numbers_are_expected(self):
    with self.assertRaises(ValueError):
      math_utils.add(True, 2)

    with self.assertRaises(ValueError):
      math_utils.safe_divide(10, 2, default=True)

    with self.assertRaises(ValueError):
      math_utils.absolute_value(False)

  def test_bool_inputs_are_rejected_for_non_negative_integer_functions(self):
    with self.assertRaises(ValueError):
      math_utils.factorial(True)

    with self.assertRaises(ValueError):
      math_utils.fibonacci(False)

  def test_bool_inputs_are_rejected_for_integer_only_functions(self):
    with self.assertRaises(ValueError):
      math_utils.is_even(True)

    with self.assertRaises(ValueError):
      math_utils.is_odd(False)

    with self.assertRaises(ValueError):
      math_utils.gcd(True, 6)

    with self.assertRaises(ValueError):
      math_utils.lcm(4, False)

  def test_is_prime_loop_branch_false_case(self):
    self.assertFalse(math_utils.is_prime(9))

  def test_gcd_invalid_y_branch(self):
    with self.assertRaises(ValueError):
      math_utils.gcd(10, 2.5)

  def test_lcm_invalid_x_branch(self):
    with self.assertRaises(ValueError):
      math_utils.lcm("4", 6)


if __name__ == "__main__":
  unittest.main()