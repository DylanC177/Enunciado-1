class Animal:

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido genérico.")


class Perro(Animal):

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau guau!")


class Gato(Animal):

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau miau!")


class Vaca(Animal):

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Muuuu!")

animales = [
    Perro("Rex", 3),
    Gato("Felix", 2),
    Vaca("Lola", 5),
]

for animal in animales:
    animal.hacer_sonido()