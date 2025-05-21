class Lugar:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.medios_transporte = []
        self.eventos = []

    def agregar_medio_transporte(self, medio):
        self.medios_transporte.append(medio)

    def agregar_evento(self, evento):
        self.eventos.append(evento)

    def mostrar_info(self):
        print(f"lugar: {self.nombre}")
        print(f"ubicacion: {self.ubicacion}")
        print("medios de transporte disponibles:")
        for medio in self.medios_transporte:
            medio.mostrar_info()
        print("eventos culturales:")
        for evento in self.eventos:
            evento.mostrar_info()
        print()

class MedioTransporte:
    def __init__(self, tipo, descripcion):
        self.tipo = tipo
        self.descripcion = descripcion

    def mostrar_info(self):
        print(f"- {self.tipo}: {self.descripcion}")

class Evento:
    def __init__(self, tipo, nombre, fecha):
        self.tipo = tipo
        self.nombre = nombre
        self.fecha = fecha

    def mostrar_info(self):
        print(f"- {self.tipo} '{self.nombre}' en fecha: {self.fecha}")

def main():
    copacabana = Lugar("Copacabana", "municipio estrategico con acceso terrestre y lacustre")

    transporte_terrestre = MedioTransporte("terrestre", "buses, taxis y vehiculos particulares")
    transporte_lacustre = MedioTransporte("lacustre", "transporte fluvial predominante en la zona")

    copacabana.agregar_medio_transporte(transporte_terrestre)
    copacabana.agregar_medio_transporte(transporte_lacustre)

    fiesta_patronal = Evento("fiesta tradicional", "fiesta de la virgen de copacabana", "8 de septiembre")
    ritual_religioso = Evento("ritual", "ceremonia ancestral en la isla del sol", "anual")
    celebracion_nacional = Evento("celebracion", "festival cultural de musica y danza", "mes de agosto")

    copacabana.agregar_evento(fiesta_patronal)
    copacabana.agregar_evento(ritual_religioso)
    copacabana.agregar_evento(celebracion_nacional)

    copacabana.mostrar_info()

if __name__ == "__main__":
    main()
