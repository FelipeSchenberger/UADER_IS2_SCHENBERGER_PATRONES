from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Avion:
    def __init__(self) -> None:
        self.body = None
        self.turbinas = []
        self.alas = []
        self.tren_aterrizaje = None

    def list_parts(self) -> None:
        print("Partes del avión:")
        print(f"Body: {self.body}")
        print(f"Turbinas: {', '.join(self.turbinas)}")
        print(f"Alas: {', '.join(self.alas)}")
        print(f"Tren de aterrizaje: {self.tren_aterrizaje}")

class Builder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def get_avion(self) -> Avion:
        pass

    @abstractmethod
    def construir_body(self) -> None:
        pass

    @abstractmethod
    def construir_turbinas(self) -> None:
        pass

    @abstractmethod
    def construir_alas(self) -> None:
        pass

    @abstractmethod
    def construir_tren_aterrizaje(self) -> None:
        pass

class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._avion = Avion()

    def get_avion(self) -> Avion:
        avion = self._avion
        self.reset()
        return avion

    def construir_body(self) -> None:
        self._avion.body = "Cuerpo resistente"

    def construir_turbinas(self) -> None:
        self._avion.turbinas.append("Turbinas potentes (x2)")

    def construir_alas(self) -> None:
        self._avion.alas.append("Alas largas (x2)")

    def construir_tren_aterrizaje(self) -> None:
        self._avion.tren_aterrizaje = "Tren de aterrizaje robusto"

class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_avion(self) -> None:
        self.builder.construir_body()
        self.builder.construir_turbinas()
        self.builder.construir_alas()
        self.builder.construir_tren_aterrizaje()

if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    director.build_avion()
    avion = builder.get_avion()
    avion.list_parts()