class Ministerio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_empleados = 0
        self.empleados_nombre = [""] * 100
        self.empleados_apellido_paterno = [""] * 100
        self.empleados_apellido_materno = [""] * 100
        self.edades = [0] * 100
        self.sueldos = [0] * 100

    def agregar_empleado(self, nombre, apellido_paterno, apellido_materno, edad, sueldo):
        posicion = self.numero_empleados
        self.empleados_nombre[posicion] = nombre
        self.empleados_apellido_paterno[posicion] = apellido_paterno
        self.empleados_apellido_materno[posicion] = apellido_materno
        self.edades[posicion] = edad
        self.sueldos[posicion] = sueldo
        self.numero_empleados += 1

    def mostrar(self):
        print("Ministerio:", self.nombre)
        print("Dirección:", self.direccion)
        print("Número de empleados:", self.numero_empleados)
        for i in range(self.numero_empleados):
            print(self.empleados_nombre[i], self.empleados_apellido_paterno[i], self.empleados_apellido_materno[i], 
                  "- Edad:", self.edades[i], "- Sueldo:", self.sueldos[i])

    # b) Eliminar empleados con edad X
    def eliminar_por_edad(self, edad_buscar):
        nuevos_nombres = [""] * 100
        nuevos_apellidos_paterno = [""] * 100
        nuevos_apellidos_materno = [""] * 100
        nuevas_edades = [0] * 100
        nuevos_sueldos = [0] * 100
        nuevo_contador = 0

        for i in range(self.numero_empleados):
            if self.edades[i] != edad_buscar:
                nuevos_nombres[nuevo_contador] = self.empleados_nombre[i]
                nuevos_apellidos_paterno[nuevo_contador] = self.empleados_apellido_paterno[i]
                nuevos_apellidos_materno[nuevo_contador] = self.empleados_apellido_materno[i]
                nuevas_edades[nuevo_contador] = self.edades[i]
                nuevos_sueldos[nuevo_contador] = self.sueldos[i]
                nuevo_contador = nuevo_contador + 1

        self.empleados_nombre = nuevos_nombres
        self.empleados_apellido_paterno = nuevos_apellidos_paterno
        self.empleados_apellido_materno = nuevos_apellidos_materno
        self.edades = nuevas_edades
        self.sueldos = nuevos_sueldos
        self.numero_empleados = nuevo_contador
        
    def __add__(self, otro):
        num = int(input("Ingrese el Numero del empleado a transferir: "))
        if 0 <= num < otro.numero_empleados:
            self.agregar_empleado(
                otro.empleados_nombre[num],
                otro.empleados_apellido_paterno[num],
                otro.empleados_apellido_materno[num],
                otro.edades[num],
                otro.sueldos[num]
            )
            print("Empleado transferido.")
        else:
            print("Índice inválido.")
        return self

    def mostrar_empleado_menor_edad(self):
        if self.numero_empleados == 0:
            print("No hay empleados.")
            return
        menor = self.edades[0]
        num = 0
        for i in range(1, self.numero_empleados):
            if self.edades[i] < menor:
                menor = self.edades[i]
                num = i
        print("Empleado con menor edad:", self.empleados_nombre[num], self.empleados_apellido_paterno[num],
              self.empleados_apellido_materno[num], "- Edad:", menor)

    def mostrar_empleado_menor_sueldo(self):
        if self.numero_empleados == 0:
            print("No hay empleados.")
            return
        menor = self.sueldos[0]
        num = 0
        for i in range(1, self.numero_empleados):
            if self.sueldos[i] < menor:
                menor = self.sueldos[i]
                num = i
        print("Empleado con menor sueldo:", self.empleados_nombre[num], self.empleados_apellido_paterno[num],
              self.empleados_apellido_materno[num], "- Sueldo:", menor)


def main():
    # a)  
    ministerio1 = Ministerio("Salud", "Av. Arce #1000")
    ministerio2 = Ministerio("Educación", "Calle Comercio #200")

    ministerio1.agregar_empleado("Pedro", "Rojas", "Luna", 35, 2500)
    ministerio1.agregar_empleado("Lucy", "Sosa", "Rios", 43, 3250)
    ministerio1.agregar_empleado("Ana", "Perez", "Rojas", 26, 2700)
    ministerio1.agregar_empleado("Saul", "Arce", "Calle", 29, 2400)

    ministerio2.agregar_empleado("Mario", "Lopez", "Soto", 25, 2000)

    ministerio1.mostrar()
    ministerio2.mostrar()
    # b) 
    print("\nEliminando empleados con edad 26 Salud:")
    ministerio1.eliminar_por_edad(26)
    ministerio1.mostrar()
    # c) 
    print("\nTransferencia de empleado de Educacion a Salud:")
    ministerio1 = ministerio1 + ministerio2
    ministerio1.mostrar()
    # d) 
    print("\nEmpleado con menor edad en Salud:")
    ministerio1.mostrar_empleado_menor_edad()
    # d) 
    print("\nEmpleado con menor sueldo en Salud:")
    ministerio1.mostrar_empleado_menor_sueldo()


main()
