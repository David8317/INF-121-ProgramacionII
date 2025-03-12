import math
 # sobrecarga

class Figura:
    def area(self):
        pass 
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class TrianguloRect(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

class Trapecio(Figura):
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

class Pentagono(Figura):
    def __init__(self, perimetro, apotema):
        self.perimetro = perimetro
        self.apotema = apotema

    def area(self):
        return (self.perimetro * self.apotema) / 2

if __name__ == "__main__":
    f1 = Circulo(7)
    f2 = Rectangulo(6, 4)
    f3= TrianguloRect(4, 2)
    f4 = Trapecio(3, 8, 3)
    f5= Pentagono(9, 4)

    print("Círculo:", f1.area())
    print("Rectángulo:", f2.area())
    print("Triángulo rectángulo:", f3.area())
    print("Trapecio:", f4.area())
    print("Pentágono:", f5.area())
