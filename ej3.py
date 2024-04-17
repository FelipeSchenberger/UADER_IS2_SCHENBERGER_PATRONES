#!/usr/bin/python3.7
#*--------------------------------------------------
#* factory.py
#* adapted for a specific scenario with hamburgers and their delivery methods
#*--------------------------------------------------
from abc import ABC, abstractmethod

class HamburguesaCreator(ABC):
    """
    The HamburguesaCreator class declares the factory method that is supposed
    to return an object of a Hamburguesa class. The HamburguesaCreator's subclasses
    usually provide the implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        The factory method that creates a Hamburguesa.
        """
        pass

    def some_operation(self) -> str:
        """
        Calls the factory method to create a Hamburguesa object and then uses it.
        """
        product = self.factory_method()
        result = f"Orden de Hamburguesa: La hamburguesa será {product.delivery_method()}\n"
        return result

class MostradorCreator(HamburguesaCreator):
    def factory_method(self):
        return MostradorHamburguesa()

class RetiroClienteCreator(HamburguesaCreator):
    def factory_method(self):
        return RetiroClienteHamburguesa()

class DeliveryCreator(HamburguesaCreator):
    def factory_method(self):
        return DeliveryHamburguesa()

class Hamburguesa(ABC):
    """
    The Hamburguesa interface declares the operations that all concrete hamburguesas
    must implement.
    """
    @abstractmethod
    def delivery_method(self) -> str:
        pass

class MostradorHamburguesa(Hamburguesa):
    def delivery_method(self) -> str:
        return "entregada en mostrador."

class RetiroClienteHamburguesa(Hamburguesa):
    def delivery_method(self) -> str:
        return "retirada por el cliente."

class DeliveryHamburguesa(Hamburguesa):
    def delivery_method(self) -> str:
        return "enviada por delivery."

def client_code(creator: HamburguesaCreator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface.
    """
    print(creator.some_operation(), end="")

if __name__ == "__main__":
    print("App: Hamburguesa para entrega en mostrador")
    client_code(MostradorCreator())
    print("\nApp: Hamburguesa para retiro por el cliente")
    client_code(RetiroClienteCreator())
    print("\nApp: Hamburguesa para delivery")
    client_code(DeliveryCreator())
