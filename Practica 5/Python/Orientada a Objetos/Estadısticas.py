import math
#Programacion Orientada a Objetos.
class Estadisticas:
    def __init__(self, numeros):
        self.numeros = numeros

    def get_promedio(self):
        return sum(self.numeros) / len(self.numeros)

    def get_desviacion(self):
        promedio = self.get_promedio()
        return math.sqrt(sum((x - promedio) ** 2 for x in self.numeros) / (len(self.numeros) - 1))

    def mostrar_resultados(self):
        print(f"El promedio es {self.get_promedio():.2f}")
        print(f"La desviación estándar es {self.get_desviacion():.5f}")

def main():
    numeros = list(map(float, input("Ingrese 10 números: ").split()))
    estadisticas = Estadisticas(numeros)
    estadisticas.mostrar_resultados()

main()
