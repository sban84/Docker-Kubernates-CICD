import math


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        return self.x + self.y

    def subtract(self, x, y):
        print("inside sub method")
        pass


if __name__ == "__main__":
    a, b = 2, 3
    cal = Calculator(2, 3)
    print(f"addition of {a} and {b} = {cal.add(a, b)}")
    print(f"subtraction of {a} and {b} = {cal.subtract(a, b)}")
