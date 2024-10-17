import pytest

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 5
    assert subtract(0, 0) == 0
    assert subtract(3, 5) == -2