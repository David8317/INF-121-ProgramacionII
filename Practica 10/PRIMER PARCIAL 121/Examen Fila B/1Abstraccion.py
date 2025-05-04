class Planta:
    def __init__(self, nombre, tipo, altura):
        self.nombre = nombre
        self.tipo = tipo
        self.altura = altura  

    def __str__(self):
        return f"Planta: {self.nombre}, Tipo: {self.tipo}, Altura: {self.altura} cm"


class BarreraGeografica:
    def __init__(self, tipo_barrera, ubicacion):
        self.tipo_barrera = tipo_barrera
        self.ubicacion = ubicacion

    def __str__(self):
        return f"Barrera: {self.tipo_barrera} en {self.ubicacion}"


class Ambiente:
    def __init__(self, clima, region, plantas, barrera):
        self.clima = clima
        self.region = region
        self.plantas = plantas  
        self.barrera = barrera  

    def cantidad_plantas(self):
        return len(self.plantas)

    def mostrar_datos_ambiente(self):
        print(f"Ambiente en region: {self.region}, Clima: {self.clima}")
        print(f"Barrera geografica presente: {self.barrera}")
        print(f"Cantidad de plantas: {self.cantidad_plantas()}")
        for planta in self.plantas:
            print(planta)


def main_parte_b():
    planta1 = Planta("Totora", "Acuatica", 150)
    planta2 = Planta("Queñua", "Arbol", 300)
    plantas = [planta1, planta2]

    barrera = BarreraGeografica("Montaña", "Cordillera Real")

    ambiente = Ambiente("Frio", "Altiplano", plantas, barrera)
    ambiente.mostrar_datos_ambiente()
if __name__ == "__main__":
    main_parte_b()
