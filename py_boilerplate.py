### Good to do:
### - Use Black for formatting
### - Use flake8 as linter

### calc.py ####

class Calculator:
    def __init__(self, num_1: int, num_2: int):
        """Class initializer; Takes two numbers and allow to do calculations
        Args:
            num_1 (int): First number for the calculation
            num_2 (int): Second number for the calculation
        """
        self.num_1 = num_1
        self.num_2 = num_2
        return

    def sum(self) -> int:
        """Perform summation of two numbers"""
        return self.num_1 + self.num_2


#### test_calc.py ####

import pytest


def test_sum():
    num_1 = 3
    num_2 = 4
    calc = Calculator(num_1, num_2)
    sum = calc.sum()
    assert sum == num_1 + num_2


pytest.main()

#### main.py ####

# from calc import Calculator
def main():
    calc = Calculator(2, 2)
    sum = calc.sum()
    print(f"The sum is {sum}")


if __name__ == "__main__":
    main()
