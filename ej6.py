#!/usr/python
#*--------------------------------------------------
#* prototype.py
#*--------------------------------------------------
import copy
import time


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    """
    Python proporciona su propia interfaz de Prototype mediante las funciones
    `copy.copy` y `copy.deepcopy`. Cualquier clase que quiera implementar
    implementaciones personalizadas debe sobrescribir las funciones miembro
    `__copy__` y `__deepcopy__`.
    """

    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        # Retraso artificial para simular carga de procesamiento
        time.sleep(0.1)  # Esto es para demostración; ajusta según sea necesario para simular diferentes cargas

        # Primero, vamos a crear copias de los objetos anidados.
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # Luego, vamos a clonar el objeto en sí, utilizando los clones preparados de los
        # objetos anidados.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        # Retraso artificial para simular carga de procesamiento
        time.sleep(0.1)  # Esto es para demostración; ajusta según sea necesario para simular diferentes cargas

        if memo is None:
            memo = {}

        # Primero, vamos a crear copias de los objetos anidados.
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        # Luego, vamos a clonar el objeto en sí, utilizando los clones preparados de los
        # objetos anidados.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    # Simular una copia profunda más
    deep_copied_component = component
    for _ in range(20):  # Esto incrementará el proceso de deepcopy hasta 20 niveles de profundidad
        deep_copied_component = copy.deepcopy(deep_copied_component)
    
    # Finalmente imprimir un mensaje que el proceso ha completado
    print("La copia profunda a 20 niveles de anidamiento se ha completado.")
