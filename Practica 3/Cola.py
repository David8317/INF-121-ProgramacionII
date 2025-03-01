class Cola:
    def __init__(self, n):
        self.n = n
        self.arreglo = [0] * n
        self.inicio = 0
        self.fin = -1
        self.elementos = 0

    def insert(self, e):
        if not self.isFull():
            self.fin = (self.fin + 1) % self.n
            self.arreglo[self.fin] = e
            self.elementos += 1
        else:
            print("Cola llena")

    def remove(self):
        if not self.isEmpty():
            valor = self.arreglo[self.inicio]
            self.inicio = (self.inicio + 1) % self.n
            self.elementos -= 1
            return valor
        print("Cola vacía")
        return -1

    def peek(self):
        if not self.isEmpty():
            return self.arreglo[self.inicio]
        print("Cola vacía")
        return -1

    def isEmpty(self):
        return self.elementos == 0

    def isFull(self):
        return self.elementos == self.n

    def size(self):
        return self.elementos


# Prueba de la clase con 3 elementos
if __name__ == "__main__":
    cola = Cola(5)
    cola.insert(10)
    cola.insert(20)
    cola.insert(30)
    #Agrega un elemento al final de la cola.
    
    print(cola.remove())  # 10 Elimina y devuelve el primer elemento.
    print(cola.remove())  # 20
    print(cola.peek())    # 30 Muestra el primer elemento sin eliminarlo.
