import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

class Boleto(ABC):
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0

    @abstractmethod
    def obtener_precio(self):
        pass

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.precio}"

class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0

    def obtener_precio(self):
        return self.precio

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        if dias_anticipacion >= 10:
            self.precio = 50.0
        else:
            self.precio = 60.0

    def obtener_precio(self):
        return self.precio

class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        if dias_anticipacion >= 10:
            self.precio = 25.0
        else:
            self.precio = 30.0

    def obtener_precio(self):
        return self.precio

# Funciones
def vender_boleto():
    tipo = tipo_boleto.get()
    try:
        numero = int(caja_numero.get())
        dias = int(caja_dias.get()) if tipo in ("Platea", "Galeria") else 0
    except ValueError:
        messagebox.showerror("Ingrese valores numericos validos.")
        return

    if tipo == "Palco":
        boleto = Palco(numero)
    elif tipo == "Platea":
        boleto = Platea(numero, dias)
    elif tipo == "Galeria":
        boleto = Galeria(numero, dias)
    else:
        messagebox.showerror("Seleccione un tipo de boleto.")
        return

    etiqueta_informacion.config(text=str(boleto))

def salir():
    ventana_principal.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Teatro Municipal")
ventana_principal.geometry("450x400")
ventana_principal.configure(bg="white")

etiqueta_titulo = tk.Label(ventana_principal, text="Teatro Municipal", font=("Arial", 20, "bold"), bg="white")
etiqueta_titulo.pack(pady=10)

marco_datos = tk.LabelFrame(ventana_principal, text="Datos del Boleto", padx=10, pady=10, bg="white")
marco_datos.pack(pady=10)

tipo_boleto = tk.StringVar()
tipo_boleto.set("Palco")

radio_palco = tk.Radiobutton(marco_datos, text="Palco", variable=tipo_boleto, value="Palco", bg="white")
radio_platea = tk.Radiobutton(marco_datos, text="Platea", variable=tipo_boleto, value="Platea", bg="white")
radio_galeria = tk.Radiobutton(marco_datos, text="Galeria", variable=tipo_boleto, value="Galeria", bg="white")

radio_palco.grid(row=0, column=0, padx=5, pady=5)
radio_platea.grid(row=0, column=1, padx=5, pady=5)
radio_galeria.grid(row=0, column=2, padx=5, pady=5)

tk.Label(marco_datos, text="Número:", bg="white").grid(row=1, column=0, sticky="e")
caja_numero = tk.Entry(marco_datos)
caja_numero.grid(row=1, column=1, pady=5)

tk.Label(marco_datos, text="Cant. Días para el Evento:", bg="white").grid(row=2, column=0, sticky="e")
caja_dias = tk.Entry(marco_datos)
caja_dias.grid(row=2, column=1, pady=5)

boton_vender = tk.Button(marco_datos, text="Vender", width=10, command=vender_boleto)
boton_salir = tk.Button(marco_datos, text="Salir", width=10, command=salir)
boton_vender.grid(row=3, column=0, pady=10)
boton_salir.grid(row=3, column=1, pady=10)

marco_informacion = tk.LabelFrame(ventana_principal, text="Información", padx=10, pady=10, bg="white")
marco_informacion.pack(pady=10)

etiqueta_informacion = tk.Label(marco_informacion, text="Número: , Precio: ", font=("Arial", 12, "bold"), bg="white", fg="blue")
etiqueta_informacion.pack()

ventana_principal.mainloop()
