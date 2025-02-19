import matplotlib.pyplot as plt

class Linea:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f"Línea de ({self.x1}, {self.y1}) a ({self.x2}, {self.y2})"

    def dibuja_linea(self):
        plt.plot([self.x1, self.x2], [self.y1, self.y2], marker='o', color='b')
        plt.title("Dibujo de Línea")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()

linea = Linea(1.0, 2.0, 4.0, 6.0)
print(linea)
linea.dibuja_linea()
