import math
#Modular-Estructura
def promedio(numeros):
    return sum(numeros) / len(numeros)

def desviacion(numeros, promedio):
    return math.sqrt(sum((x - promedio) ** 2 for x in numeros) / (len(numeros) - 1))

def main():
    numeros = list(map(float, input("Ingrese 10 números: ").split()))
    prom = promedio(numeros)
    print(f"El promedio es {prom:.2f}")
    print(f"La desviación estándar es {desviacion(numeros, prom):.5f}")

main()
