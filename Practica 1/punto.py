import math

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return self.x, self.y

    def coord_polares(self):
        r = math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y, self.x)
        return r, math.degrees(theta)

    def __str__(self):
        return f"Punto({self.x}, {self.y})"

p = Punto(3, 4)
print("Coordenadas cartesianas:", p.coord_cartesianas())
print("Coordenadas polares:", p.coord_polares())
print("Representación:", p)
