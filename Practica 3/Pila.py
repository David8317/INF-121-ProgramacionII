class Pila:
    def __init__(self, n):
        self.n = n
        self.arreglo = [0] * n
        self.top = -1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.arreglo[self.top] = e
        else:
            print("Pila llena")

    def pop(self):
        if not self.isEmpty():
            valor = self.arreglo[self.top]
            self.top -= 1
            return valor
        print("Pila vacía")
        return -1

    def peek(self):
        if not self.isEmpty():
            return self.arreglo[self.top]
        print("Pila vacía")
        return -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.n - 1

if __name__ == "__main__":
    pila = Pila(5)
    pila.push(10)
    pila.push(20)
    pila.push(30)       
    print(pila.pop())   # 30  Saca y devuelve el último elemento de la pila
    print(pila.pop())   # 20  
    print(pila.peek())  # 10 el último elemento sin sacarlo
