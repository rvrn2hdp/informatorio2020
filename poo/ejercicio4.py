""" ejercicio 4
 Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre,
 el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:
    Añadir contacto
    Lista de contactos
    Buscar contacto
    Editar contacto
    Cerrar agenda
"""

class Agenda():
    def __init__(self):
        # constructor
        self.contactos = []
    
    def añadir(self, contacto):
        # metodo para añadir contactos
        self.contactos.append(contacto)
    
    def mostrarLista(self):
        # metodo para mostrar la lista de contactos
        print("\nLista de Contactos:")
        for contacto in self.contactos:
            print(contacto)

    def buscar(self):
        # metodo para buscar un contacto en la agenda
        dni = int(input("\nIngrese el ID del contacto: "))
        for contacto in self.contactos:
            if dni == contacto.dni:
                return contacto
        else:
            return "Contacto no encontrado.\n"

    def editar(self, contacto):
        # metodo para modificar un contacto
        print("\nDato a editar:")
        print("1 - Nombre")
        print("2 - Teléfono")
        print("3 - Email")
        dato = int(input("Ingrese una opción: "))
        contacto.editar(dato)
        print(contacto)

    def realizarAccion(self, opc):
        # metodo que realiza una accion
        if opc == 1:
            self.mostrarLista()
        if opc == 2:
            print(self.buscar())
        if opc == 3:
            self.editar(self.buscar())
        if opc == 4:
            print("Cerrando agenda...")

    def mostrarMenu(self):
        # metodo que muestra el menu de la agenda en bucle
        while True:
            print("\nMenú de Agenda: ")
            print("1 - Mostrar Contactos")
            print("2 - Buscar Contacto")
            print("3 - Editar Contacto")
            print("4 - Cerrar Agenda")
            opc = int(input("Ingrese una opción: "))
            self.realizarAccion(opc)
            if opc == 4:
                break

class Contacto():
    def __init__(self, dni, nombre, telefono, email):
        # constructor
        self.dni = dni
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def __str__(self):
        # este metodo retornará una cadena de texto con los datos del contacto
        return f"Nombre: {self.nombre}\nTeléfono: {self.telefono}\nEmail: {self.email}\n"

    def editar(self, dato):
        # metodo que modifica un dato del contacto
        if dato == 1:
            self.nombre = input("Ingrese el nuevo nombre: ")
        elif dato == 2:
            self.telefono = int(input("Ingrese el nuevo teléfono: "))
        elif dato == 3:
            self.email = input("Ingrese el nuevo email: ")
        else:
            print("Opción ingresada incorrecta.")

# creacion de la agenda
miAgenda = Agenda()
# se crean los contactos
contacto1 = Contacto(1, "Alex Rider", 43242, "alexrider@gmail.com")
contacto2 = Contacto(2, "Felix El Gato", 32453, "felixelgato@gmail.com")
contacto3 = Contacto(3, "juan ortiz", 23245, "juanortiz@gmail.com")
# se añaden los contactos creados
miAgenda.añadir(contacto1)
miAgenda.añadir(contacto2)
miAgenda.añadir(contacto3)
# inicializamos el menu de nuestra agenda
miAgenda.mostrarMenu()

"""
print("Creando Agenda...")
print("Ingresando Contactos...\nIngrese 0 si desea terminar:")


while True:
    si = int(input("1 - añadir contacto\n0 - Salir\n"))
    if si == 1:
        dni = int(input("Ingrese el DNI: "))
        nombre = input("Ingrese el nombre: ")
        telefono = int(input("Ingrese el teléfono: "))
        email = input("Ingrese el email:")
        miAgenda.añadir(contacto = Contacto(dni, nombre, telefono, email))
    elif si == 0:
        break
    else:
        print("Opción incorrecta.\n")
"""
