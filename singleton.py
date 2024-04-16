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


class Singleton(metaclass=SingletonMeta):
#    def some_business_logic(self):
#        """
#        Finally, any singleton should define some business logic, which can be
#        executed on its instance.
#        """
#
#
    def getid(self):
        return "Nombre de la empresa --- Tartufo SA"

    def getCUIT(self):
        return "20-13322447-6"

    def getIIBB(self):
        return "111122223333"

    def getCalle(self):
        return "Av. de Mayo 810 - CABA"

class AFIP():
    def getCUIT(self):
        return "20-13322447-6"


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
        print(s1.getid())
        print("\n")
        print("CUIT:"+s1.getCUIT())
        print("IIBB:"+s1.getIIBB())
        print("Calle:"+s1.getCalle())
    else:
        print("Singleton failed, variables contain different instances.")


    print("\nEste es otro programa porque el profe tiene fiaca de tipear\n")
    s3= AFIP()
    s4= AFIP()

    if id(s3) == id(s4):
       print("iguales")
    else:
       print("distintos")
