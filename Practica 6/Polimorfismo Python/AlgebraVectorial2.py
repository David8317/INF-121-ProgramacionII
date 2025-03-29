import math

class Lineal2:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sumar(self, otro):
        return Lineal2(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def multiplicar(self, escalar):
        return Lineal2(self.x * escalar, self.y * escalar, self.z * escalar)

    def magnitud(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalizar(self):
        magnitud = self.magnitud()
        return Lineal2(self.x / magnitud, self.y / magnitud, self.z / magnitud)

    def producto_escalar(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z

    def producto_vectorial(self, otro):
        return Lineal2(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

if __name__ == "__main__":
    a = Lineal2(1, 2, 3)
    b = Lineal2(4, 5, 6)

    print("a) Suma de vectores:", a.sumar(b))
    print("b) Multiplicación por escalar (2):", a.multiplicar(2))
    print("c) Magnitud de a:", a.magnitud())
    print("d) Vector normalizado de a:", a.normalizar())
    print("e) Producto escalar:", a.producto_escalar(b))
    print("f) Producto vectorial:", a.producto_vectorial(b))
