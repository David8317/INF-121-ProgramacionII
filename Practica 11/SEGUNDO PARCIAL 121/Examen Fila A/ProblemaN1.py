class Artista:
    def __init__(self, nombre, ci, años_experiencia):
        self.nombre = nombre
        self.ci = ci
        self.años_experiencia = años_experiencia

    def __str__(self):
        return f"{self.nombre} ({self.años_experiencia} años de experiencia)"

class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

    def __str__(self):
        return f"Anuncio #{self.numero} - Precio: {self.precio}"

class Obra:
    def __init__(self, titulo, material, artista1, artista2, anuncio=None):
        self.titulo = titulo
        self.material = material
        self.artista1 = artista1
        self.artista2 = artista2
        self.anuncio = anuncio

    def artistas(self):
        return [self.artista1, self.artista2]

    def set_anuncio(self, anuncio):
        self.anuncio = anuncio

class Pintura(Obra):
    def __init__(self, titulo, material, artista1, artista2, genero, anuncio=None):
        super().__init__(titulo, material, artista1, artista2, anuncio)
        self.genero = genero

    def __str__(self):
        return f"Pintura: {self.titulo} ({self.genero})"

    @staticmethod
    def artista_mas_experimentado(pinturas):
        mayor = None
        max_experiencia = -1
        for pintura in pinturas:
            for artista in pintura.artistas():
                if artista.años_experiencia > max_experiencia:
                    max_experiencia = artista.años_experiencia
                    mayor = artista
        return mayor

    @staticmethod
    def monto_total(pinturas):
        total = 0
        for pintura in pinturas:
            if pintura.anuncio is not None:
                total += pintura.anuncio.precio
        return total


def Main():
    # a. Crear un objeto pintura con anuncio y otro sin anuncio
    a1 = Artista("Carlos", "12345", 5)
    a2 = Artista("Lucía", "67890", 8)
    a3 = Artista("Marta", "54321", 12)
    a4 = Artista("Luis", "98765", 6)
    print("\n", a1, "\n", a2, "\n", a3, "\n", a4)

    anuncio1 = Anuncio(1, 1500)
    print("\n",anuncio1)
    
    pintura_con_anuncio = Pintura("Atardecer", "Oleo", a1, a2, "Paisaje", anuncio1)
    pintura_sin_anuncio = Pintura("Montañas", "Acrílico", a3, a4, "Naturalismo")
    pinturas = [pintura_con_anuncio, pintura_sin_anuncio]
    print("\n",pintura_con_anuncio,"\n",pintura_sin_anuncio)
    # b Mostrar el nombre del artista con más años de experiencia
    mas_experto = Pintura.artista_mas_experimentado(pinturas)
    print("Artista con mas experiencia:", mas_experto.nombre)
    # c Agregar un anuncio a la pintura sin anuncio y mostrar el monto total de venta
    anuncio2 = Anuncio(2, 2000)
    print("\n",anuncio2)
    pintura_sin_anuncio.set_anuncio(anuncio2)
    total = Pintura.monto_total(pinturas)
    print("Total de venta de ambas pinturas:", total)

if __name__ == "__main__":
    Main()
