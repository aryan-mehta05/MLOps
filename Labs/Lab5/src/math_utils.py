import math


def _validate_number(value, name="value"):
  """
  Validate that the input is a numeric type (int or float, but not bool).

  Args:
    value: Value to validate.
    name (str): Parameter name for error messaging.

  Raises:
    ValueError: If value is not a valid numeric type.
  """
  if isinstance(value, bool) or not isinstance(value, (int, float)):
    raise ValueError(f"{name} must be an int or float.")


def _validate_non_negative_integer(value, name="value"):
  """
  Validate that the input is a non-negative integer.

  Args:
    value: Value to validate.
    name (str): Parameter name for error messaging.

  Raises:
    ValueError: If value is not a non-negative integer.
  """
  if not isinstance(value, int) or isinstance(value, bool) or value < 0:
    raise ValueError(f"{name} must be a non-negative integer.")


def add(x, y):
  """Return the sum of two numbers."""
  _validate_number(x, "x")
  _validate_number(y, "y")
  return x + y


def subtract(x, y):
  """Return the difference of two numbers."""
  _validate_number(x, "x")
  _validate_number(y, "y")
  return x - y


def multiply(x, y):
  """Return the product of two numbers."""
  _validate_number(x, "x")
  _validate_number(y, "y")
  return x * y


def divide(x, y):
  """
  Divide x by y.

  Raises:
    ValueError: If y is zero.
  """
  _validate_number(x, "x")
  _validate_number(y, "y")
  if y == 0:
    raise ValueError("Cannot divide by zero.")
  return x / y


def safe_divide(x, y, default=0):
  """
  Safely divide x by y.
  Returns default if y is zero.
  """
  _validate_number(x, "x")
  _validate_number(y, "y")
  _validate_number(default, "default")
  if y == 0:
    return default
  return x / y


def power(x, y):
  """Return x raised to the power y."""
  _validate_number(x, "x")
  _validate_number(y, "y")
  return x ** y


def square(x):
  """Return the square of x."""
  _validate_number(x, "x")
  return x ** 2


def cube(x):
  """Return the cube of x."""
  _validate_number(x, "x")
  return x ** 3


def modulus(x, y):
  """Return x % y."""
  _validate_number(x, "x")
  _validate_number(y, "y")
  if y == 0:
    raise ValueError("Cannot take modulus by zero.")
  return x % y


def absolute_value(x):
  """Return the absolute value of x."""
  _validate_number(x, "x")
  return abs(x)


def round_number(x, digits=0):
  """
  Round a number to the specified number of digits.
  """
  _validate_number(x, "x")
  if not isinstance(digits, int):
    raise ValueError("digits must be an integer.")
  return round(x, digits)


def floor_number(x):
  """Return the floor of x."""
  _validate_number(x, "x")
  return math.floor(x)


def ceil_number(x):
  """Return the ceiling of x."""
  _validate_number(x, "x")
  return math.ceil(x)


def average(*args):
  """
  Return the arithmetic mean of one or more numeric values.
  """
  if len(args) == 0:
    raise ValueError("At least one number is required.")
  for i, value in enumerate(args):
    _validate_number(value, f"arg_{i}")
  return sum(args) / len(args)


def maximum(*args):
  """Return the maximum value from the inputs."""
  if len(args) == 0:
    raise ValueError("At least one number is required.")
  for i, value in enumerate(args):
    _validate_number(value, f"arg_{i}")
  return max(args)


def minimum(*args):
  """Return the minimum value from the inputs."""
  if len(args) == 0:
    raise ValueError("At least one number is required.")
  for i, value in enumerate(args):
    _validate_number(value, f"arg_{i}")
  return min(args)


def factorial(n):
  """
  Return factorial of a non-negative integer n.
  """
  _validate_non_negative_integer(n, "n")
  return math.factorial(n)


def fibonacci(n):
  """
  Return the nth Fibonacci number.

  Examples:
    fibonacci(0) -> 0
    fibonacci(1) -> 1
    fibonacci(7) -> 13
  """
  _validate_non_negative_integer(n, "n")

  if n == 0:
    return 0
  if n == 1:
    return 1

  a, b = 0, 1
  for _ in range(2, n + 1):
    a, b = b, a + b
  return b


def is_even(n):
  """Return True if n is even."""
  if not isinstance(n, int) or isinstance(n, bool):
    raise ValueError("n must be an integer.")
  return n % 2 == 0


def is_odd(n):
  """Return True if n is odd."""
  if not isinstance(n, int) or isinstance(n, bool):
    raise ValueError("n must be an integer.")
  return n % 2 != 0


def is_prime(n):
  """
  Return True if n is a prime number.
  """
  if not isinstance(n, int) or isinstance(n, bool):
    raise ValueError("n must be an integer.")
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False

  limit = int(math.sqrt(n)) + 1
  for i in range(3, limit, 2):
    if n % i == 0:
      return False
  return True


def gcd(x, y):
  """Return the greatest common divisor of two integers."""
  if not isinstance(x, int) or isinstance(x, bool):
    raise ValueError("x must be an integer.")
  if not isinstance(y, int) or isinstance(y, bool):
    raise ValueError("y must be an integer.")
  return math.gcd(x, y)


def lcm(x, y):
  """Return the least common multiple of two integers."""
  if not isinstance(x, int) or isinstance(x, bool):
    raise ValueError("x must be an integer.")
  if not isinstance(y, int) or isinstance(y, bool):
    raise ValueError("y must be an integer.")
  if x == 0 or y == 0:
    return 0
  return abs(x * y) // math.gcd(x, y)


def percentage(part, whole):
  """
  Return what percentage 'part' is of 'whole'.

  Raises:
    ValueError: If whole is zero.
  """
  _validate_number(part, "part")
  _validate_number(whole, "whole")
  if whole == 0:
    raise ValueError("whole cannot be zero.")
  return (part / whole) * 100


def clamp(value, min_value, max_value):
  """
  Clamp value within [min_value, max_value].

  Raises:
    ValueError: If min_value > max_value.
  """
  _validate_number(value, "value")
  _validate_number(min_value, "min_value")
  _validate_number(max_value, "max_value")

  if min_value > max_value:
    raise ValueError("min_value cannot be greater than max_value.")

  return max(min_value, min(value, max_value))