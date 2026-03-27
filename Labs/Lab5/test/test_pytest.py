import pytest
from src import math_utils


def test_add():
  assert math_utils.add(2, 3) == 5
  assert math_utils.add(-1, 1) == 0
  assert math_utils.add(2.5, 1.5) == 4.0


def test_subtract():
  assert math_utils.subtract(10, 3) == 7
  assert math_utils.subtract(-1, -1) == 0


def test_multiply():
  assert math_utils.multiply(4, 5) == 20
  assert math_utils.multiply(-2, 3) == -6


def test_divide():
  assert math_utils.divide(10, 2) == 5
  assert math_utils.divide(7, 2) == 3.5
  with pytest.raises(ValueError):
    math_utils.divide(5, 0)


def test_safe_divide():
  assert math_utils.safe_divide(10, 2) == 5
  assert math_utils.safe_divide(10, 0) == 0
  assert math_utils.safe_divide(10, 0, default=-1) == -1


def test_power():
  assert math_utils.power(2, 3) == 8
  assert math_utils.power(5, 0) == 1


def test_square_and_cube():
  assert math_utils.square(4) == 16
  assert math_utils.cube(3) == 27


def test_modulus():
  assert math_utils.modulus(10, 3) == 1
  with pytest.raises(ValueError):
    math_utils.modulus(5, 0)


def test_absolute_value():
  assert math_utils.absolute_value(-8) == 8
  assert math_utils.absolute_value(8) == 8


def test_round_number():
  assert math_utils.round_number(3.14159, 2) == 3.14
  assert math_utils.round_number(3.6) == 4


def test_floor_and_ceil():
  assert math_utils.floor_number(3.9) == 3
  assert math_utils.ceil_number(3.1) == 4


def test_average():
  assert math_utils.average(2, 4, 6) == 4
  assert math_utils.average(5) == 5
  with pytest.raises(ValueError):
    math_utils.average()


def test_maximum_and_minimum():
  assert math_utils.maximum(1, 8, 3, 4) == 8
  assert math_utils.minimum(1, 8, 3, 4) == 1
  with pytest.raises(ValueError):
    math_utils.maximum()
  with pytest.raises(ValueError):
    math_utils.minimum()


def test_factorial():
  assert math_utils.factorial(0) == 1
  assert math_utils.factorial(5) == 120
  with pytest.raises(ValueError):
    math_utils.factorial(-1)


def test_fibonacci():
  assert math_utils.fibonacci(0) == 0
  assert math_utils.fibonacci(1) == 1
  assert math_utils.fibonacci(7) == 13
  with pytest.raises(ValueError):
    math_utils.fibonacci(-2)


def test_is_even_and_is_odd():
  assert math_utils.is_even(4) is True
  assert math_utils.is_even(5) is False
  assert math_utils.is_odd(5) is True
  assert math_utils.is_odd(4) is False


def test_is_prime():
  assert math_utils.is_prime(2) is True
  assert math_utils.is_prime(17) is True
  assert math_utils.is_prime(1) is False
  assert math_utils.is_prime(12) is False


def test_gcd_and_lcm():
  assert math_utils.gcd(12, 18) == 6
  assert math_utils.lcm(12, 18) == 36
  assert math_utils.lcm(0, 5) == 0


def test_percentage():
  assert math_utils.percentage(25, 100) == 25
  assert math_utils.percentage(1, 4) == 25
  with pytest.raises(ValueError):
    math_utils.percentage(10, 0)


def test_clamp():
  assert math_utils.clamp(5, 1, 10) == 5
  assert math_utils.clamp(-3, 0, 10) == 0
  assert math_utils.clamp(25, 0, 10) == 10
  with pytest.raises(ValueError):
    math_utils.clamp(5, 10, 1)


def test_invalid_numeric_inputs():
  with pytest.raises(ValueError):
    math_utils.add("2", 3)
  with pytest.raises(ValueError):
    math_utils.multiply(None, 2)
  with pytest.raises(ValueError):
    math_utils.round_number(3.14, "2")


def test_integer_validation_errors():
  with pytest.raises(ValueError):
    math_utils.is_even(2.5)

  with pytest.raises(ValueError):
    math_utils.is_odd("3")

  with pytest.raises(ValueError):
    math_utils.is_prime(True)

  with pytest.raises(ValueError):
    math_utils.gcd(4.5, 2)

  with pytest.raises(ValueError):
    math_utils.lcm(4, "6")


def test_non_negative_integer_validation_errors():
  with pytest.raises(ValueError):
    math_utils.factorial(3.5)

  with pytest.raises(ValueError):
    math_utils.fibonacci(True)


def test_more_invalid_numeric_inputs():
  with pytest.raises(ValueError):
    math_utils.safe_divide(10, 0, default="invalid")

  with pytest.raises(ValueError):
    math_utils.ceil_number("abc")

  with pytest.raises(ValueError):
    math_utils.floor_number(None)


def test_average_maximum_minimum_invalid_argument_types():
  with pytest.raises(ValueError):
    math_utils.average(1, "bad", 3)

  with pytest.raises(ValueError):
    math_utils.maximum(1, True, 3)

  with pytest.raises(ValueError):
    math_utils.minimum(1, None, 3)


def test_bool_inputs_are_rejected_where_numbers_are_expected():
  with pytest.raises(ValueError):
    math_utils.add(True, 2)

  with pytest.raises(ValueError):
    math_utils.safe_divide(10, 2, default=True)

  with pytest.raises(ValueError):
    math_utils.absolute_value(False)


def test_bool_inputs_are_rejected_for_non_negative_integer_functions():
  with pytest.raises(ValueError):
    math_utils.factorial(True)

  with pytest.raises(ValueError):
    math_utils.fibonacci(False)


def test_bool_inputs_are_rejected_for_integer_only_functions():
  with pytest.raises(ValueError):
    math_utils.is_even(True)

  with pytest.raises(ValueError):
    math_utils.is_odd(False)

  with pytest.raises(ValueError):
    math_utils.gcd(True, 6)

  with pytest.raises(ValueError):
    math_utils.lcm(4, False)


# Add missing tests for 100% coverage.
def test_is_prime_loop_branch_false_case():
  assert math_utils.is_prime(9) is False


def test_gcd_invalid_y_branch():
  with pytest.raises(ValueError):
    math_utils.gcd(10, 2.5)


def test_lcm_invalid_x_branch():
  with pytest.raises(ValueError):
    math_utils.lcm("4", 6)