"""A simple calculator package that can perform basic arithmetic operations."""
__version__ = "0.1.0"

from typing import Optional


class Calculator:
    """
    A calculator class that can perform basic arithmetic operations.
    """

    def __init__(self) -> None:
        """
        Initialize the calculator with a memory of 0.
        """
        self.memory: float = 0

    def add(self, num1: float, num2: Optional[float] = None) -> float:
        """
        Add two numbers or a single number to the calculator's memory and return the result.
        """
        if num2 is None:
            self.memory += num1
        else:
            self.memory = num1 + num2
        return self.memory

    def subtract(self, num1: float, num2: Optional[float] = None) -> float:
        """
        Subtract two numbers or a single number from the calculator's memory and return the result.
        """
        if num2 is None:
            self.memory -= num1
        else:
            self.memory = num1 - num2
        return self.memory

    def multiply(self, num1: float, num2: Optional[float] = None) -> float:
        """
        Multiply two numbers or a single number with the calculator's memory and return the result.
        """
        if num2 is None:
            self.memory *= num1
        else:
            self.memory = num1 * num2
        return self.memory

    def divide(self, num1: float, num2: Optional[float] = None) -> float:
        """
        Divide the calculator's memory by a number or divide two numbers and return the result.
        """
        if num2 is None:
            if num1 == 0:
                raise ValueError("Cannot divide by zero")
            self.memory /= num1
        else:
            if num1 == 0 or num2 == 0:
                raise ValueError("Cannot divide by zero")
            self.memory = num1 / num2
        return self.memory

    def nth_root(self, root: int, num1: Optional[float] = None, num2: Optional[float] = None) -> float:
        """
        Take the nth root of a number and store the result in the calculator's memory or take the nth root of two numbers.
        """
        if num1 is None:
            if self.memory == 0:
                raise ValueError("Cannot take the 0th root")
            if self.memory < 0 and root % 2 == 0:
                raise ValueError("Cannot take an even root of a negative number")
            self.memory = self.memory ** (1/root)
        elif num2 is None:
            if root == 0:
                raise ValueError("Cannot take the 0th root")
            if num1 < 0:
                raise ValueError("Cannot take root of a negative number")
            self.memory = num1 ** (1/root)
        else:
            if root == 0:
                raise ValueError("Cannot take the 0th root")
            if num1*num2 < 0:
                raise ValueError("Cannot take a root of a negative number")
            self.memory = (num1*num2) ** (1/root)
        return self.memory

    def reset(self) -> float:
        """
        Reset the calculator's memory to 0.
        """
        self.memory = 0
        return self.memory
