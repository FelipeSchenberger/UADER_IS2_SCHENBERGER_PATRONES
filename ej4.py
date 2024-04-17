from abc import ABC, abstractmethod

# Product Interface
class Factura(ABC):
    @abstractmethod
    def detalles(self) -> str:
        pass

# Concrete Products
class FacturaIVAResponsable(Factura):
    def __init__(self, importe_base):
        self.importe_base = importe_base
        self.iva = self.importe_base * 0.21  # Asumimos un IVA del 21%

    def detalles(self) -> str:
        importe_total = self.importe_base + self.iva
        return f"Factura IVA Responsable: Importe base ${self.importe_base}, IVA ${self.iva}, Total ${importe_total}."

class FacturaIVANoInscripto(Factura):
    def __init__(self, importe_base):
        self.importe_base = importe_base
        self.iva = 0  # No se agrega IVA

    def detalles(self) -> str:
        return f"Factura IVA No Inscripto: Importe total ${self.importe_base} (IVA no aplicado)."

class FacturaIVAExento(Factura):
    def __init__(self, importe_base):
        self.importe_base = importe_base
        self.iva = 0  # Exento de IVA

    def detalles(self) -> str:
        return f"Factura IVA Exento: Importe total ${self.importe_base} (exento de IVA)."

# Creator
class CreatorFactura(ABC):
    @abstractmethod
    def factory_method(self, tipo: str, importe_base: float) -> Factura:
        pass

# Concrete Creator
class ConcreteCreatorFactura(CreatorFactura):
    def factory_method(self, tipo: str, importe_base: float) -> Factura:
        if tipo == 'responsable':
            return FacturaIVAResponsable(importe_base)
        elif tipo == 'no_inscripto':
            return FacturaIVANoInscripto(importe_base)
        elif tipo == 'exento':
            return FacturaIVAExento(importe_base)
        else:
            raise ValueError("Tipo de factura no soportado")

def client_code(creator: CreatorFactura, tipo: str, importe_base: float) -> None:
    factura = creator.factory_method(tipo, importe_base)
    print(factura.detalles())

if __name__ == "__main__":
    creator = ConcreteCreatorFactura()
    client_code(creator, 'responsable', 1000)
    client_code(creator, 'no_inscripto', 1000)
    client_code(creator, 'exento', 1000)
