class EspacioPublico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

    def mostrar_info(self):
        print(f"Espacio Público: {self.nombre}, Ubicación: {self.ubicacion}")

class ZonaUrbana(EspacioPublico):
    def __init__(self, nombre, ubicacion, jardin):
        super().__init__(nombre, ubicacion)
        self.jardin = jardin  

    def mostrar_detalles(self):
        self.mostrar_info()
        print("Incluye el siguiente jardín:")
        self.jardin.mostrar_jardin()

class Jardin:
    def __init__(self, nombre, tamano, personas, minibuses):
        self.nombre = nombre
        self.tamano = tamano
        self.personas = personas     
        self.minibuses = minibuses   

    def mostrar_jardin(self):
        print(f"Jardín: {self.nombre}, Tamaño: {self.tamano}")
        print("Personas en el jardín:")
        for p in self.personas:
            print(f"- {p.nombre}, {p.actividad_actual}")
        print("Minibuses que pasan por el jardín:")
        for m in self.minibuses:
            print(f"- Línea {m.numero} (Ruta: {m.ruta})")

class Persona:
    def __init__(self, nombre, edad, actividad_actual):
        self.nombre = nombre
        self.edad = edad
        self.actividad_actual = actividad_actual

class Minibus:
    def __init__(self, numero, ruta, capacidad):
        self.numero = numero
        self.ruta = ruta
        self.capacidad = capacidad

def Main():
    
    p1 = Persona("Lucía", 25, "Leyendo")
    p2 = Persona("Marco", 40, "Caminando")

    m1 = Minibus(11, "Villa Fátima - Centro", 18)
    m2 = Minibus(7, "Obrajes - Cementerio", 16)
    
    jardin_prado = Jardin("Jardín Central", "500 m²", [p1, p2], [m1, m2])
    prado = ZonaUrbana("El Prado", "Av. 16 de Julio", jardin_prado)
    prado.mostrar_detalles()

if __name__ == "__main__":
    Main()
