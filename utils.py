class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b if b != 0 else 0

    @staticmethod
    def sum_list(lst):
        return sum(lst)
