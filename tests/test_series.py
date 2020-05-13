from math_series.series import fibonacci

def test_one():
  expected = 0
  actual = fibonacci(0)
  assert actual == expected

def test_two():
  expected = 1
  actual = fibonacci(1)
  assert actual == expected

def test_three():
  expected = 2
  actual = fibonacci(3)
  assert actual == expected

def test_four():
  expected = 1
  actual = fibonacci(2)
  assert actual == expected

  def test_five():
    expected = 5
    actual = fibonacci(4)
    assert actual == expected

