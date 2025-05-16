import pytest

#A function to test
def division(a,b):
return a/b

#A test function
def test_raises():
with pytest.raises(ZeroDivisionError):
division(a=25, b=0)