import pytest
from calc import Calculator

new_calculator = Calculator(1, 3)

def add_test():
    result = new_calculator.addition()
    assert result == 4

add_test()
def main():
    add_test()

if __name__ == "__main__":
    main()