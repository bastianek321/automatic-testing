
class Calculator:

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

class Table:

    def has_number(self, array, x):
        return x in array

    def sum(self, array):
        result = 0
        for number in array:
            result += number
        return result
