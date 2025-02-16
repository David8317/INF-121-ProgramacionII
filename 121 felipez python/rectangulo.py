class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def area(self):
        return self.base * self.altura


# Ejemplo de uso
rectangulo = Rectangulo(5, 3)
print("Base:", rectangulo.base)
print("Altura:", rectangulo.altura)
print("Perímetro:", rectangulo.perimetro())
print("Área:", rectangulo.area())
