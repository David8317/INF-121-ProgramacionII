import math
#Modular-Estructura
def get_discriminante(a, b, c):
    return (b ** 2) - (4 * a * c)

def get_raiz1(a, b, discriminante):
    return (-b + math.sqrt(discriminante)) / (2 * a)

def get_raiz2(a, b, discriminante):
    return (-b - math.sqrt(discriminante)) / (2 * a)

def main():
    a, b, c = map(float, input("Ingrese a, b, c: ").split())
    discriminante = get_discriminante(a, b, c)

    if discriminante > 0:
        print(f"La ecuación tiene dos raíces: {get_raiz1(a, b, discriminante):.5f} y {get_raiz2(a, b, discriminante):.5f}")
    elif discriminante == 0:
        print(f"La ecuación tiene una raíz: {get_raiz1(a, b, discriminante):.5f}")
    else:
        print("La ecuación no tiene raíces reales")

main()
