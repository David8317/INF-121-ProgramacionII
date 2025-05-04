class LineaTeleferico:
    def __init__(self, color, tramo, cantidad_cabinas):
        self.color = color
        self.tramo = tramo
        self.cantidad_cabinas = cantidad_cabinas
        self.cantidad_empleados = 0

        self.nombres_empleados = [""] * 100
        self.ape_p_empleados = [""] * 100
        self.ape_m_empleados = [""] * 100
        self.edades_empleados = [0] * 100
        self.sueldos_empleados = [0] * 100

    def agregar_empleado(self, nombre, apellido_paterno, apellido_materno, edad, sueldo):
        i = self.cantidad_empleados
        self.nombres_empleados[i] = nombre
        self.ape_p_empleados[i] = apellido_paterno
        self.ape_m_empleados[i] = apellido_materno
        self.edades_empleados[i] = edad
        self.sueldos_empleados[i] = sueldo
        self.cantidad_empleados =  self.cantidad_empleados + 1

    def mostrar(self):
        print("\nLínea:", self.color)
        print("Tramo:", self.tramo)
        print("Cabinas:", self.cantidad_cabinas)
        print("Empleados:", self.cantidad_empleados)
        for i in range(self.cantidad_empleados):
            print(f"{self.nombres_empleados[i]} {self.ape_p_empleados[i]} {self.ape_m_empleados[i]} - Edad: {self.edades_empleados[i]} - Sueldo: {self.sueldos_empleados[i]} Bs")

    def eliminar_apellido(self, apellido):
        eliminar = 0
        for i in range(self.cantidad_empleados):
            if self.ape_p_empleados[i] != apellido and self.ape_m_empleados[i] != apellido:
                self.nombres_empleados[eliminar] = self.nombres_empleados[i]
                self.ape_p_empleados[eliminar] = self.ape_p_empleados[i]
                self.ape_m_empleados[eliminar] = self.ape_m_empleados[i]
                self.edades_empleados[eliminar] = self.edades_empleados[i]
                self.sueldos_empleados[eliminar] = self.sueldos_empleados[i]
                eliminar= eliminar + 1
        self.cantidad_empleados = eliminar

    def __add__(self, otra_linea):
        num = int(input("Ingrese Numero del empleado a transferir: "))
        if 0 <= num < self.cantidad_empleados:
            otra_linea.agregar_empleado(
                self.nombres_empleados[num],
                self.ape_p_empleados[num],
                self.ape_m_empleados[num],
                self.edades_empleados[num],
                self.sueldos_empleados[num]
            )
            print(f"Empleado {self.nombres_empleados[num]} transferido a la linea {otra_linea.color}")
        else:
            print(" inbalido")
        return otra_linea

    def mostrar_empleado_mayor_edad(self):
        if self.cantidad_empleados == 0:
            print("No hay empleados.")
            return
        mayor = self.edades_empleados[0]
        posicion = 0
        for i in range(1, self.cantidad_empleados):
            if self.edades_empleados[i] > mayor:
                mayor = self.edades_empleados[i]
                posicion = i
        print(f"Mayor edad: {self.nombres_empleados[posicion]} {self.ape_p_empleados[posicion]} {self.ape_m_empleados[posicion]} - Edad: {mayor}")

    def mostrar_empleado_mayor_sueldo(self):
        if self.cantidad_empleados == 0:
            print("No hay empleados")
            return
        mayor = self.sueldos_empleados[0]
        posicion = 0
        for i in range(1, self.cantidad_empleados):
            if self.sueldos_empleados[i] > mayor:
                mayor = self.sueldos_empleados[i]
                posicion = i
        print(f"Mayor sueldo: {self.nombres_empleados[posicion]} {self.ape_p_empleados[posicion]} {self.ape_m_empleados[posicion]} - Sueldo: {mayor} Bs")

def main():
    # a)
    linea_roja = LineaTeleferico("Rojo", "Estacion Central - Cementerio", 20)
    linea_azul = LineaTeleferico("Azul", "Estacion Busch - Prado", 25)

    linea_roja.agregar_empleado("Pedro", "Rojas", "Luna", 35, 2500)
    linea_roja.agregar_empleado("Lucy", "Sosa", "Rios", 43, 3250)
    linea_roja.agregar_empleado("Ana", "Perez", "Rojas", 26, 2700)
    linea_roja.agregar_empleado("Saul", "Arce", "Calle", 29, 2500)
    linea_azul.agregar_empleado("Maria", "Gomez", "Lopez", 30, 2800)

    print("\n--- Línea Roja ---")
    linea_roja.mostrar()
    print("\n--- Línea Azul ---")
    linea_azul.mostrar()

    # b)
    print("\nEliminando empleados con apellido 'Rojas'...")
    linea_roja.eliminar_apellido("Rojas")
    linea_roja.mostrar()

    # c)
    print("\nTransferencia de empleado:")
    linea_azul = linea_roja + linea_azul
    linea_azul.mostrar()

    # d)
    print("\nEmpleado con mayor edad en Línea Roja:")
    linea_roja.mostrar_empleado_mayor_edad()
    print("\nEmpleado con mayor sueldo en Línea Azul:")
    linea_azul.mostrar_empleado_mayor_sueldo()

main()
