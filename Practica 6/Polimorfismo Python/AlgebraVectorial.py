import math

class Lineal:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Lineal(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Lineal(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Lineal(self.x * scalar, self.y * scalar, self.z * scalar)
        raise ValueError("Multiplicación solo soportada con escalares.")
    
    def __truediv__(self, scalar):
        if scalar != 0:
            return Lineal(self.x / scalar, self.y / scalar, self.z / scalar)
        raise ValueError("División por cero no permitida.")
    
    def producto_escalar(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    
    def producto_vectorial(self, otro):
        return Lineal(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )
    
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalizar(self):
        mag = self.magnitud()
        if mag == 0:
            raise ValueError("No se puede normalizar un vector nulo.")
        return self / mag
    
    def es_perpendicular(self, otro):
        return math.isclose(self.producto_escalar(otro), 0, abs_tol=1e-9)
    
    def es_paralelo(self, otro):
        return self.producto_vectorial(otro).magnitud() == 0
    
    def proyeccion_sobre(self, otro):
        return otro * (self.producto_escalar(otro) / otro.magnitud()**2)
    
    def componente_en_direccion(self, otro):
        return self.producto_escalar(otro) / otro.magnitud()
    
    def __repr__(self):
        return f"Lineal({self.x}, {self.y}, {self.z})"
    
# Ejemplo de uso
a = Lineal(1, 2, 3)
b = Lineal(4, 5, 6)

print("a) Perpendicular: |a + b| = |a - b|", abs((a + b).magnitud() - (a - b).magnitud()) < 1e-9)
print("b) Perpendicular: |a - b| = |b - a|", abs((a - b).magnitud() - (b - a).magnitud()) < 1e-9)
print("c) Perpendicular: a · b = 0", a.producto_escalar(b) == 0)
print("d) Perpendicular: |a + b|² = |a|² + |b|²", math.isclose((a + b).magnitud()**2, a.magnitud()**2 + b.magnitud()**2, abs_tol=1e-9))
print("e) Paralelo: a = r * b", a.es_paralelo(b))
print("f) Paralelo: a × b = 0", a.producto_vectorial(b).magnitud() == 0)
print("g) Proyección de a sobre b:", a.proyeccion_sobre(b))
print("h) Componente de a en la dirección de b:", a.componente_en_direccion(b))
