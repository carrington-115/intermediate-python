# calculator function
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y
    
    def multiply(self):
        return self.x * self.y
    
    def divide(self):
        if self.y == 0:
            raise ZeroDivisionError("The value of y cannot be zero")
        return self.x / self.y
    
    def mod(self):
        return self.x % self.y
    
    def long_divide(self):
        return self.x // self.y
    
    def __str__(self):
        return f"This an a calculating operation between 2 numbers"