import math


class Figura:

    def area(self):
        return 0


class Rectangulo(Figura):

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Circulo(Figura):

    def __init__(self, radio: float):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio**2)


class Triangulo(Figura):

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


figuras = [
    Rectangulo(base=5, altura=10),
    Circulo(radio=3),
    Triangulo(base=4, altura=8),
]

for figura in figuras:
    nombre_clase = figura.__class__.__name__
    print(f"El área del {nombre_clase} es: {figura.area():.2f}")