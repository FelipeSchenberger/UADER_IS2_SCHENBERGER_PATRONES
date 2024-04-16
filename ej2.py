#!/usr/python
#*--------------------------------------------------
#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class TaxCalculator(metaclass=SingletonMeta):
    def calculate_taxes(self, base_amount):
        """
        Calcula y retorna el total incluyendo impuestos sobre la base imponible.
        """
        iva = base_amount * 0.21
        iibb = base_amount * 0.05
        municipal_tax = base_amount * 0.012
        total_tax = iva + iibb + municipal_tax
        return base_amount + total_tax


if __name__ == "__main__":
    # The client code.

    tax_calculator1 = TaxCalculator()
    tax_calculator2 = TaxCalculator()

    if id(tax_calculator1) == id(tax_calculator2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    # Calculating taxes
    base_amount = 1000
    total_with_taxes = tax_calculator1.calculate_taxes(base_amount)
    print(f"Total amount including taxes for {base_amount} is {total_with_taxes:.2f}")
