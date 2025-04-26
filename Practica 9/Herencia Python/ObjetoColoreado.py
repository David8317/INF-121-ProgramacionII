import tkinter as tk
from tkinter import messagebox
import random
from abc import ABC, abstractmethod

# Interfaz Coloreado
class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self) -> str:
        pass

# Clase abstracta Figura
class Figura(ABC):
    def __init__(self, color="Sin color"):
        self.color = color

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def __str__(self):
        return f"Color: {self.color}"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# Clase Cuadrado que extiende Figura e implementa Coloreado
class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color="Sin color"):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado

    def comoColorear(self):
        return "Colorear los cuatro lados"

# Clase Circulo que extiende Figura
class Circulo(Figura):
    def __init__(self, radio, color="Sin color"):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio * self.radio

    def perimetro(self):
        return 2 * 3.1416 * self.radio

# --------- Interfaz Gráfica Tkinter ---------

# Funciones
def generar_figuras():
    figuras.clear()
    for _ in range(5):
        tipo = random.randint(1, 2)  # 1: Cuadrado, 2: Circulo
        if tipo == 1:
            lado = random.randint(1, 10)
            figura = Cuadrado(lado, color="Rojo")
        else:
            radio = random.randint(1, 10)
            figura = Circulo(radio, color="Azul")
        figuras.append(figura)
    mostrar_figuras()

def mostrar_figuras():
    texto_resultado.config(state="normal")
    texto_resultado.delete(1.0, "end")
    for figura in figuras:
        texto_resultado.insert("end", f"{figura.__class__.__name__}\n")
        texto_resultado.insert("end", f"{figura}\n")
        texto_resultado.insert("end", f"Área: {figura.area():.2f}\n")
        texto_resultado.insert("end", f"Perímetro: {figura.perimetro():.2f}\n")
        if isinstance(figura, Coloreado):
            texto_resultado.insert("end", f"{figura.comoColorear()}\n")
        texto_resultado.insert("end", "-" * 30 + "\n")
    texto_resultado.config(state="disabled")

def salir():
    ventana_principal.destroy()

# Ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Sistema de Figuras Coloreadas")
ventana_principal.geometry("500x500")
ventana_principal.configure(bg="white")

# Título
etiqueta_titulo = tk.Label(ventana_principal, text="Figuras Aleatorias", font=("Arial", 20, "bold"), bg="white")
etiqueta_titulo.pack(pady=10)

# Botones
marco_botones = tk.Frame(ventana_principal, bg="white")
marco_botones.pack(pady=10)

boton_generar = tk.Button(marco_botones, text="Generar Figuras", width=15, command=generar_figuras)
boton_salir = tk.Button(marco_botones, text="Salir", width=15, command=salir)
boton_generar.grid(row=0, column=0, padx=10)
boton_salir.grid(row=0, column=1, padx=10)

# Área de resultados
marco_resultado = tk.LabelFrame(ventana_principal, text="Resultados", padx=10, pady=10, bg="white")
marco_resultado.pack(pady=10, fill="both", expand=True)

texto_resultado = tk.Text(marco_resultado, state="disabled", wrap="word")
texto_resultado.pack(fill="both", expand=True)

# Lista de figuras
figuras = []

ventana_principal.mainloop()
