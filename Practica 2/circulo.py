import matplotlib.pyplot as plt
import numpy as np

class Circulo:
    def __init__(self, cx, cy, radio):
        self.cx = cx
        self.cy = cy
        self.radio = radio

    def __str__(self):
        return f"Círculo con centro en ({self.cx}, {self.cy}) y radio {self.radio}"

    def dibuja_circulo(self):
        theta = np.linspace(0, 2 * np.pi, 100)
        x = self.cx + self.radio * np.cos(theta)
        y = self.cy + self.radio * np.sin(theta)

        # Dibujar el círculo
        plt.plot(x, y, label=f'Círculo: Centro ({self.cx}, {self.cy}), Radio {self.radio}')
        plt.gca().set_aspect('equal', adjustable='box')  # Para que el círculo no se deforme
        plt.title("Dibujo de Círculo")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.legend()
        plt.show()

circulo = Circulo(3.0, 4.0, 5.0)
print(circulo)
circulo.dibuja_circulo()
