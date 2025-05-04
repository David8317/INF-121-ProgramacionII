class Indigena:
    def __init__(self, nombre, edad, comunidad):
        self.nombre = nombre
        self.edad = edad
        self.comunidad = comunidad

    def __str__(self):
        return f"Indígena: {self.nombre}, Edad: {self.edad}, Comunidad: {self.comunidad}"


class Gobierno:
    def __init__(self, nombre_presidente, medidas):
        self.nombre_presidente = nombre_presidente
        self.medidas = medidas  

    def mostrar_medidas(self):
        print("Medidas del gobierno:")
        for medida in self.medidas:
            print(f"- {medida}")

    def agregar_medida(self, medida):
        self.medidas.append(medida)


class EmpresaMinera:
    def __init__(self, nombre, ubicacion, lista_indigenas, gobierno):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.lista_indigenas = lista_indigenas 
        self.gobierno = gobierno  

    def contar_indigenas_afectados(self):
        return len(self.lista_indigenas)

    def mostrar_datos_empresa(self):
        print(f"Empresa Minera: {self.nombre}, Ubicación: {self.ubicacion}")
        print(f"Cantidad de indígenas afectados: {self.contar_indigenas_afectados()}")
        print("Datos de indígenas:")
        for indigena in self.lista_indigenas:
            print(indigena)
        print("Gobierno que interviene:")
        print(f"Presidente: {self.gobierno.nombre_presidente}")
        self.gobierno.mostrar_medidas()


def main_parte_a():
    indigena1 = Indigena("Juan", 45, "comunidad Aymara")
    indigena2 = Indigena("Lucia", 30, "comunidad Quechua")
    lista_indigenas = [indigena1, indigena2]

    medidas_gobierno = ["Compensación economica", "Reforestacion", "Reubicacion"]
    gobierno = Gobierno("Luis Arce", medidas_gobierno)

    empresa = EmpresaMinera("MinaAndes", "Potosi", lista_indigenas, gobierno)
    empresa.mostrar_datos_empresa()
if __name__ == "__main__":
    main_parte_a()

