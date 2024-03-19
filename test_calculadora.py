import pytest
from calculadora import suma, resta

def test_suma():
    assert suma(2, 3) == "error"
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_resta():
    assert resta(5, 2) == 3
    assert resta(10, 5) == 5
    assert resta(100, 100) == 0

if __name__ == "__main__":
    pytest.main()