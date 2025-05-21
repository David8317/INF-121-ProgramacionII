class Artista:
    def __init__(self, nombre, ci, anios_experiencia):
        self.nombre = nombre
        self.ci = ci
        self.anios_experiencia = anios_experiencia

    def __str__(self):
        return f"{self.nombre} ({self.anios_experiencia} años de experiencia)"

class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

    def incrementar_precio(self, cantidad):
        self.precio += cantidad

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

    def contiene_artista(self, nombre_artista):
        return self.artista1.nombre == nombre_artista or self.artista2.nombre == nombre_artista

def main_parte_b():
    # a Crear dos objetos pintura que tengan anuncios de venta
    a1 = Artista("Ana", "111", 7)
    a2 = Artista("Mario", "222", 10)
    a3 = Artista("Pedro", "333", 5)
    a4 = Artista("Luisa", "444", 8)
    print("\n", a1, "\n", a2, "\n", a3, "\n", a4)

    anuncio1 = Anuncio(1, 1800)
    anuncio2 = Anuncio(2, 2200)

    pintura1 = Pintura("Sol Andino", "Oleo", a1, a2, "Costumbrista", anuncio1)
    pintura2 = Pintura("Luz de Luna", "Acrílico", a3, a4, "Romanticismo", anuncio2)
    print("\n",pintura1,"\n",pintura2)
    pinturas = [pintura1, pintura2]
    print("\n",anuncio1,"\n",anuncio2)
    # b Calcular el promedio de años de experiencia de los artistas de ambas pinturas
    suma = 0
    cantidad = 0
    for pintura in pinturas:
        for artista in pintura.artistas():
            suma += artista.anios_experiencia
            cantidad += 1

    if cantidad > 0:
        promedio = suma / cantidad
        print("\n","Promedio de años de experiencia:", promedio)
    else:
        print("No hay artistas para calcular el promedio")
    # c Incrementar el precio en X a la pintura del artista con nombre X
    nombre_objetivo = "Mario"
    incremento = 500
    for pintura in pinturas:
        if pintura.contiene_artista(nombre_objetivo):
            pintura.anuncio.incrementar_precio(incremento)
    print("Precios actualizados:")
    for pintura in pinturas:
        print(pintura.anuncio)
        
if __name__ == "__main__":
    main_parte_b()
