class Empleado:
    def __init__(self, rol, nombre, cedula):
        self.rol = rol
        self.nombre = nombre
        self.cedula = cedula
        self.balance = 0 

    def retirar(self, monto):
        if monto > 0 and monto <= self.balance:
            self.balance -= monto
            return monto
        else:
            return 0

    def pagar(self):
        salarios = {
            "Programador Junior": 500,
            "Programador Senior": 750,
            "Manager": 1000,
        }
        salario = salarios.get(self.rol, 0)
        self.balance += salario

class Nomina:
    def __init__(self):
        self.empleados = [] 
        self.presupuesto = 0 

    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            self.empleados.append(empleado)

    def mostrar_empleados(self):
        for i, empleado in enumerate(self.empleados):
            print(f"{i+1}. Nombre: {empleado.nombre}\nCedula: {empleado.cedula}\nRol: {empleado.rol}\nBalance: ${empleado.balance}\n")

    def pagar_nomina(self):
        total_pagado = 0
        for empleado in self.empleados:
            salarios = {
                "Programador Junior": 500,
                "Programador Senior": 750,
                "Manager": 1000,
            }
            salario = salarios.get(empleado.rol, 0)
            if self.presupuesto >= salario:
                empleado.pagar()
                self.presupuesto -= salario
                total_pagado += salario
            else:
                print(f"No hay suficiente presupuesto para pagar el salario de {empleado.nombre}")
        print(f"Se ha pagado un total de ${total_pagado} a los empleados")
        print(f"El presupuesto restante es de ${self.presupuesto}")

    def agregar_saldo(self, monto):
        if monto > 0:
            self.presupuesto += monto
            print(f"Se ha agregado ${monto} al presupuesto de la nómina")
            print(f"El nuevo presupuesto es de ${self.presupuesto}")
        else:
            print("El monto debe ser positivo")

def menu_interactivo():
    print("Bienvenido al sistema de nómina Saman Inc")
    print("Seleccione una opción:")
    print("1. Registrar un empleado")
    print("2. Mostrar los empleados")
    print("3. Pagar la nómina")
    print("4. Agregar saldo al presupuesto de la Empresa")
    print("5. Retirar dinero")
    print("6. Salir")

def validar_menu(minimo, maximo):
    entrada = None
    while entrada is None:
        try:
            entrada = int(input("> "))
            if entrada < minimo or entrada > maximo:
                print(f"La opción debe estar entre {minimo} y {maximo}")
                entrada = None
        except ValueError:
            print("La opción debe ser un número entero")
    return entrada

#Esta forma de validar el menu que este entre las opciones disponibles, me la enseño un amigo de sistemas de hacerlo de forma distinta y practica :) Quise usarlo en este sistema.

nomina = Nomina()

while True:
    menu_interactivo()
    opcion = validar_menu(1, 6)
    if opcion == 1: 
        rol = input("Ingrese el rol del empleado: ")
        nombre = input("Ingrese el nombre del empleado: ")
        cedula = input("Ingrese la cédula del empleado: ")
        empleado = Empleado(rol, nombre, cedula)
        nomina.agregar_empleado(empleado)
        print(f"Se ha registrado al empleado ({empleado.nombre} - {empleado.cedula}) de rol \"{empleado.rol}\". Balance: ${empleado.balance}\n")
    elif opcion == 2: 
        nomina.mostrar_empleados()
    elif opcion == 3:
        nomina.pagar_nomina()
    elif opcion == 4: 
        monto = float(input("Ingrese el monto a agregar al presupuesto: "))
        nomina.agregar_saldo(monto)
    elif opcion == 5:
        numero = int(input("Ingrese el número del empleado que desea retirar saldo: "))
        if numero > 0 and numero <= len(nomina.empleados):
            empleado = nomina.empleados[numero-1]
            print(f"Empleado seleccionado: {empleado.nombre}\nCedula: {empleado.cedula}\nRol: {empleado.rol}\nBalance: ${empleado.balance}\n")
            monto = float(input("Ingrese el monto que desea retirar: "))
            retirado = empleado.retirar(monto)
            print(f"Se ha retirado ${retirado} del balance del empleado")
            print(f"El nuevo balance del empleado es de ${empleado.balance}")
        else:
            print("El numero del empleado no se ha encontrado")
    elif opcion == 6:
        print("Gracias por usar el sistema de nómina \"Saman Inc\". Hasta pronto.")
        break

