import pytest

class Calculator:
    def __init__(self, operation, operands=[]):
        self.operands = operands
        self.operations = operation

    def addition(self):
        return self.x + self.y
    
    def multiply(self):
        return self.x * self.y
    
    def divide(self):
        if self.y == 0:
            raise ValueError("The value of y cannot be zero")
        return self.x / self.y
    
    def mod(self):
        return self.x % self.y
    
    def long_divide(self):
        return self.x // self.y
    
    def __str__(self):
        return f"This an a calculating operation between 2 numbers"