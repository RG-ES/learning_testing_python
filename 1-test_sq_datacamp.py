import pytest

#A function to test
def squared(number):
return number*number

# A test function always start with "test"
def test_sqared():
assert squared(-2) == squared(2)
