import random

class Juego:
    def __init__(self, numero_de_vidas):
        self.numero_de_vidas = numero_de_vidas
        self.record = 0

    def reinicia_partida(self):
        self.numero_de_vidas = 3

    def actualiza_record(self):
        if self.numero_de_vidas > self.record:
            self.record = self.numero_de_vidas

    def quita_vida(self):
        self.numero_de_vidas -= 1
        return self.numero_de_vidas > 0

#  (hereda de juego)
class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas):
        super().__init__(numero_de_vidas)

    def valida_numero(self, numero):
        return 0 <= numero <= 10

    def juega(self):
        self.reinicia_partida()
        numero_a_adivinar = random.randint(0, 10)

        print("adivina un numero entre 0 y 10")

        while True:
            intento = int(input())
            if not self.valida_numero(intento):
                print("numero fuera de rango, intenta de nuevo")
                continue
            if intento == numero_a_adivinar:
                print("¡acertaste!")
                self.actualiza_record()
                break
            else:
                if not self.quita_vida():
                    print(f"has perdido, el numero era: {numero_a_adivinar}")
                    break
                print(f"numero incorrecto, {'es mayor' if intento < numero_a_adivinar else 'es menor'}")

#  (hereda de juegoadivinarnumero)
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, numero_de_vidas):
        super().__init__(numero_de_vidas)

    def valida_numero(self, numero):
        if 0 <= numero <= 10 and numero % 2 == 0:
            return True
        print("numero invalido. debe ser un numero par entre 0 y 10")
        return False

#  (hereda de juegoadivinarnumero)
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, numero_de_vidas):
        super().__init__(numero_de_vidas)

    def valida_numero(self, numero):
        if 0 <= numero <= 10 and numero % 2 != 0:
            return True
        print("numero invalido. debe ser un numero impar entre 0 y 10")
        return False

if __name__ == "__main__":
    juego1 = JuegoAdivinaNumero(3)
    juego2 = JuegoAdivinaPar(3)
    juego3 = JuegoAdivinaImpar(3)

    print("juego de adivinanza general")
    juego1.juega()

    print("juego de adivinanza de numeros pares ")
    juego2.juega()

    print(" juego de adivinanza de numeros impares")
    juego3.juega()
