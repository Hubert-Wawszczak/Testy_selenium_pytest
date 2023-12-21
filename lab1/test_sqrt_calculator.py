
from lab1.sqrt_calculator import oblicz_sqrt
import pytest

def test_sqrt_dodatnia():
    assert oblicz_sqrt(4) == 2.0

def test_sqrt_zero():
    assert oblicz_sqrt(0) == 0.0

def test_sqrt_ujemna():
    with pytest.raises(ValueError):
        oblicz_sqrt(-1)
