import pytest
from calc import Calculator

new_calculator = Calculator(1, 3)

def add(x, y):
    return x + y

def add_test():
    result = add(2, 2)
    assert result == 4

def divide_test():
    with pytest.raises(ZeroDivisionError):
        result = new_calculator.divide(4, 2)
        assert result == 2

add_test()
def main():
    add_test()

if __name__ == "__main__":
    main()