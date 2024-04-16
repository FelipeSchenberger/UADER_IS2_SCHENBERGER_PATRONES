#!/usr/python
#*--------------------------------------------------
#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
class SingletonMeta(type):
    """
    This metaclass ensures that there will be only one instance of any class
    that uses it.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class FactorialCalculator(metaclass=SingletonMeta):
    """
    This class calculates the factorial of a given number.
    It is a singleton to ensure that all parts of the program use the same instance.
    """
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)

if __name__ == "__main__":
    # The client code to test the Singleton implementation.
    calculator1 = FactorialCalculator()
    calculator2 = FactorialCalculator()

    if id(calculator1) == id(calculator2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    # Test factorial functionality
    print("Factorial of 5:", calculator1.factorial(5))
    print("Factorial of 7:", calculator2.factorial(7))
