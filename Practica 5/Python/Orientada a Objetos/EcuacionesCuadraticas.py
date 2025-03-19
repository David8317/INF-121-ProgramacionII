import math
#Programacion Orientada a Objetos.
class Ecuacion:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_discriminante(self):
        return (self.b ** 2) - (4 * self.a * self.c)

    def get_raiz1(self):
        return (-self.b + math.sqrt(self.get_discriminante())) / (2 * self.a)

    def get_raiz2(self):
        return (-self.b - math.sqrt(self.get_discriminante())) / (2 * self.a)

    def resolver(self):
        discriminante = self.get_discriminante()
        if discriminante > 0:
            print(f"La ecuación tiene dos raíces: {self.get_raiz1():.5f} y {self.get_raiz2():.5f}")
        elif discriminante == 0:
            print(f"La ecuación tiene una raíz: {self.get_raiz1():.5f}")
        else:
            print("La ecuación no tiene raíces reales")

def main():
    a, b, c = map(float, input("Ingrese a, b, c: ").split())
    ecuacion = Ecuacion(a, b, c)
    ecuacion.resolver()

main()
