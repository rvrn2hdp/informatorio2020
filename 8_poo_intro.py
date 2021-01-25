# Orientación a objetos (POO)

# Cuando hablamos de POO estamos hablando de un paradigma de programación donde debemos
# resolver la problemática a partir de clases y objetos. 
# Si recordamos las primeras clases cuando hablamos de tipos de datos dijimos que
# todos los datos en Python eran tratados como objetos.
# En Python cada objeto tiene una identidad, un tipo y un valor. 

# La identidad de objeto nunca cambia una vez es creada es por esto que al devolver
# un objeto independientemente del tipo veíamos la dirección del objeto en memoria. 

# El tipo de un objeto es inmutable. La función “type()” nos mostraba el tipo de 
# un objeto (que es un objeto en sí mismo). 
# El tipo de un objeto determina las operaciones o acciones que admite el objeto
# (por ejemplo, agregar o remover elementos de una lista) 
# Y también define los valores posibles para los objetos de ese tipo 
# (si trabajamos con un input entonces trabajaremos con strings como dato por defecto). 

# El valor de algunos objetos puede cambiar. 
# Se dice que los objetos cuyo valor puede cambiar son mutables; los objetos cuyo valor
# no se puede cambiar una vez que se crean se llaman immutable. 
# La mutabilidad de un objeto está determinada por su tipo; por ejemplo, los números,
# las cadenas y las tuplas son inmutables, 
# mientras que los diccionarios y las listas son mutables.

# Ejemplos de objetos en Python:

lenguaje = "Python"
print(type(lenguaje))           # class str=""

def mitad(x):
    return x/2

print(type(mitad))              # class function=""

valor = mitad(25)
print(type(valor))              # class float=""

import os
print(type(os))                 # class module=""

lista = [1, 2, 3, 4, 5]
print(type(lista))              # class list=""


# ¿Que es un objeto y que es un clase?
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Objeto --------------------------------------------------------------------------------------------------------------------------------------------------------------

# Si observamos a nuestro alrededor veremos muchos ejemplos de objetos,
# ya que se corresponden con los objetos reales del mundo que nos rodea, o con objetos internos dentro de un programa.

# Ejemplos de objetos: Persona, Computadora, Lapiz, Libro, Numero, Lista

# Un objeto posee:

# Tiempo de vida: La duración de un objeto en un programa siempre está limitada en el tiempo.
# La mayoría de los objetos sólo existen durante una parte de la ejecución del programa.
# Los objetos son creados mediante un mecanismo denominado instanciación, y cuando dejan de existir se dice que son destruidos.

# Estado: Todo objeto posee un estado, definido por sus atributos.
# Con él se definen las propiedades del objeto, y el estado en que se encuentra en un momento determinado de su existencia.
# Los atributos describen el estado de un objeto. Pueden ser de cualquier tipo de dato.

# Comportamiento: Todo objeto ha de presentar una interfaz, definida por sus métodos,
# para que el resto de objetos que componen los programas puedan interactuar con él.

# Identidad: Propiedad del objeto que lo distingue de los demás.

# El equivalente de un objeto en el paradigma estructurado sería una variable. 
# Así mismo la instanciación de objetos equivaldría a la declaración de variables,
# y el tiempo de vida de un objeto al ámbito de una variable.


# Los objetos también son conocidos como entidades, cada uno de estos
# tienen rasgos que los hacen diferentes unos de otros.
# A grandes rasgos podemos definir a un objeto como una entidad que posee
# características que lo hacen diferente a otros y que reaccionan a eventos. 

# En POO las características son variables, las cuales llamaremos atributos 
# y a las acciones las llamaremos métodos. 


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Clase --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Es un modelo, una especie de plantilla o prototipo que se utiliza para
# crear instancias individuales del mismo tipo de objeto.
# Define las propiedades y comportamiento de un tipo de objeto concreto.
# Una clase es una instancia de un objeto.

# Una clase se compone de dos partes:

# Atributos: Los atributos o propiedades de los objetos son las características que puede tener un objeto.
# Son datos asociados a las clases y a los objetos creados a partir de ellas.
# De ello, se deducen los dos tipos de atributos o de variables existentes:
# variables de clase y variables de instancia (objetos).

# Métodos: Son bloques de código (o funciones) de una clase que se utilizan
# para definir el comportamiento de los objetos.
# Estos representan las operaciones que se pueden realizar con los objetos de la clase.
# La ejecución de un método puede conducir a cambiar el estado del objeto.

# Ejemplos de Clases:

# Lápiz:
# Atributos pueden ser: color = amarillo, material = madera, tamaño = 15cm
# Métodos: Escribir, Dibujar

# Persona:
# Atributos pueden ser: nombre= Juan, apellido= Perez, color_ojos = azul, altura = 170cm, peso = 60Kg
# Métodos: Caminar, Correr, Hablar, Dormir

# Ahora que ya tenemos los conceptos teóricos veamos como definimos una clase en Python:
class Persona:
    'Esta clase define el estado y comportamiento de una persona'

    # Esto es lo que se conoce como el constructor de una clase
    # Define las características de la clase y las inicializa
    def __init__(self, nombre, edad, genero, estatura, peso):       
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.estatura = estatura
        self.peso = peso

    def hablar(self):
        print("Hola soy {}".format(self.nombre))
    def correr(self):
        print("{} está corriendo".format(self.nombre))
    def caminar(self):
        print("{} está caminando".format(self.nombre))

persona1 = Persona("Juan", 23, "Masculino", 170, 90)
persona2 = Persona("Maria", 25, "Femenino", 160, 70)

# Desde cualquier lugar de un programa se puede acceder a la cadena de documentación
# de una clase accediendo al atributo especial: NombreClase.__doc__
# El método __init__ sirve para realizar cualquier proceso de inicialización 
# que sea necesario como puede ser la asignación de valores a atributos, cálculos,
# llamadas a otras funciones o procedimientos.
# El método __init__, se ejecuta justo después de crear un nuevo objeto
# a partir de la clase proceso que se conoce con el nombre de instanciación.
# El método __init__, no retorna ningún valor y es opcional, ya que podemos
# utilizar otro nombre de método para la inicialización de la clase.
# Este método permitirá asignar atributos cada vez que creemos un objeto
# a partir de esa clase haciéndolo obligatorio. 
# Además nos permitirá llamar métodos de la clase sin instanciar; entre otras cosas.
# Cuando se crea una variable de tipo Persona, realmente se está instanciando un objeto de dicha clase.
# En este caso persona1 y persona2 son objetos cuya clase es Persona. Ambos objetos pueden hablar,
# correr y caminar porque su clase define estas operaciones
# Además poseen un nombre y edad en ambos casos, pero difieren de acuerdo a cada objeto.

# Si vemos los métodos son similares a las funciones, la única diferencia sintáctica entre
# la definición de un método y la definición de una función es
# que el primer parámetro del método por convención debe ser el nombre self.


# Tanto para acceder a los atributos como para llamar a los métodos se
# utiliza el método denominado de notación de punto
# que se basa en escribir el nombre del objeto o de la clase 
# seguido de un punto y el nombre del atributo o del método con
# los argumentos que procedan: clase.atributo, objeto.atributo, objeto.método([argumentos]).

# Es posible consultar la clase de un objeto con la función type(),
# pero también se puede consultar a través de su atributo especial class:

# print(Coche)
# print(type(Coche))
# print(coche_uno.__class__)

# A su vez las clases tienen un atributo especial "name"
# que nos devuelve su nombre en forma de cadena sin adornos:

# print(Coche.__name__)
# print(type(coche_uno).__name__)
# print(coche_uno.__class__.__name__)

# Para modelar soluciones usando Paradigma Orientado a Objetos, comúnmente se utilizan los Diagramas de Clases
# En los Diagramas de Clases modelamos las Clases como conceptos dentro de un contexto específico definido, 
#

# Veamos otro ejemplo de como definir una clase:

class Coche:
    ''' Esta clase define el estado y comportamiento de un coche '''

    ruedas = 4                                                              

    def __init__(self, color, aceleracion): # Constructor
        self.color = color                                                  
        self.aceleracion = aceleracion                                      
        self.velocidad = 0                                                  

    def acelerar(self):                                                     
        self.velocidad = self.velocidad + self.aceleracion

    def frenar(self):                                                       
        v = self.velocidad - self.aceleracion

        if v < 0:
            v = 0

        self.velocidad = v

# Creamos instancias de clase (coche_uno y coche_dos)
coche_uno = Coche('rojo', 20)
# La siguiente línea se hace referencia al atributo color del objeto coche_uno
print(coche_uno.color) 
# La siguiente línea se hace referencia al atributo ruedas del objeto coche_uno
print(coche_uno.ruedas) 

coche_dos = Coche('azul', 30)
print(coche_dos.color)
print(coche_dos.ruedas)

# coche_uno y coche_dos son objetos de la clase Coche. 
# Ambos objetos pueden acelerar y frenar, porque su clase define estas operaciones
# y tienen un color, porque la clase Coche también define ese atributo. 
# La diferencia es que coche_uno es de color rojo, mientras que coche_dos es de color azul.

# Atributos de Datos ------------------------------------------------------------------------------------------------------------------------------------
# En una clase podemos tener "Atributos de datos", éstos no necesitan ser declarados previamente. 
# Un objeto los crea del mismo modo en que se crean las variables en Python,
# es decir, cuando les asigna un valor por primera vez.
# Si retomamos el ejemplo anterior podemos agregar el número de velocidades
# de la caja del coche agregando las siguientes líneas a la definición de la clase Coche:

coche_uno.caja_velocidades = 6
print(coche_uno.caja_velocidades)

# Si tratamos de aplicar ese atributo al objeto coche_dos obtendremos un error:
# AttributeError: 'Coche' object has no attribute 'caja_velocidades'
# print(coche_dos.caja_velocidades)

# El objeto coche_dos intenta referenciar al mismo atributo,
# pero como no está definido en la clase y tampoco lo ha inicializado, el intérprete lanza un error.

# Atributos de Clase y Atributos de instancia ------------------------------------------------------------------------------------------------------------------------------------
# Una clase puede definir dos tipos diferentes de atributos de datos:
# atributos de clase y atributos de instancia.
# Los atributos de clase son atributos compartidos por todas las instancias de esa clase.
# Los atributos de instancia, por el contrario, son únicos para cada uno de los objetos
# pertenecientes a dicha clase.

# En el siguiente ejemplo, el atributo ruedas es un atributo de clase
# ya que se comparte entre todas las instancias de la clase
# Los atributos color, aceleracion y velocidad en cambio son atributos
# de instancia ya que su valor es único para cada objeto.

class Coche:
    ''' Esta clase define el estado y comportamiento de un coche '''

    ruedas = 4                                                              # Atributo de clase

    def __init__(self, color, aceleracion):                                 # Constructor
        self.color = color                                                  # Atributo de instancia
        self.aceleracion = aceleracion                                      # Atributo de instancia
        self.velocidad = 0                                                  # Atributo de instancia

    def acelerar(self):                                                     # Metodo Acelerar
        self.velocidad = self.velocidad + self.aceleracion

    def frenar(self):                                                       # Metodo Frenar
        v = self.velocidad - self.aceleracion

        if v < 0:
            v = 0

        self.velocidad = v

# Creamos instancias de clase (coche_uno y coche_dos)
coche_uno = Coche('rojo', 20)
print("Color del coche uno es: ", coche_uno.color) 
print("Cantidad de ruedas del coche uno es: ", coche_uno.ruedas) 

coche_dos = Coche('azul', 30)
print("Color del coche dos es: ",coche_dos.color)
print("Cantidad de ruedas del coche dos es: ", coche_dos.ruedas)

# Para referenciar a un atributo de clase se utiliza, generalmente, el nombre de la clase. 
# Al modificar un atributo de este tipo, los cambios se verán reflejados en todas y cada una las instancias.

Coche.ruedas = 6  # Atributo de clase
print("El número de ruedas del coche uno es: ", coche_uno.ruedas)  # Atributo de clase
print("El número de ruedas del coche dos es: ", coche_dos.ruedas)  # Atributo de clase

# Si un objeto modifica un atributo de clase, lo que realmente hace es crear un atributo de instancia con el mismo nombre que el atributo de clase.

coche_uno.ruedas = 8  # Crea el atributo de instancia ruedas dandole valor solo a este objeto
print("El número de ruedas del coche uno es: ", coche_uno.ruedas)           # Atributo de instancia
print("El número de ruedas del coche dos es: ", coche_dos.ruedas)           # Atributo de clase

print("Número de ruedas del atributo de la clase Coche: ", Coche.ruedas)            

# Herencia ---------------------------------------------------------------------------------------------------------------------------------------------------
# La Herencia muestra como puede crearse un objeto a partir de otro objeto ya existente. 
# El nuevo objeto hereda todas las cualidades del objeto del que deriva y
# además puede añadir nuevas funcionalidades o modificar las ya existentes.
# Es la capacidad de reutilizar una clase extendiendo su funcionalidad. 
# Una clase que hereda de otra puede añadir nuevos atributos, ocultarlos, añadir nuevos métodos o redefinirlos.

# Herencia simple ---------------------------------------------------------------------------------------------------------------------------------------------
# Como ejemplo vamos a implementar las clases del siguiente diagrama: https://bit.ly/30Zuo31
# Tomaremos la clase "Persona" como clase base, las clases "Supervisor" y "Obrero" como clases derivadas. 
# Definimos primero entonces la clase Persona:

class Persona():
    '''Clase que representa una Persona'''

    def __init__(self, dni, nombre, apellido, telefono):
        '''Constructor de clase Persona'''
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def __str__(self):
        '''Devuelve una cadena representativa de Persona'''
        return "%s: %s, %s %s, %s." % (
            self.__doc__[25:34], str(self.dni), self.nombre, 
            self.apellido, self.telefono)

    def hablar(self):
        '''Mostrar mensaje de saludo de Persona'''
        print("Hola soy {}".format(self.nombre))

    def correr(self):
        '''Mostrar mensaje de que Persona esta corriendo'''
        print("{} está corriendo".format(self.nombre))

    def caminar(self):
        '''Mostrar mensaje de que Persona esta caminando'''
        print("{} está caminando".format(self.nombre))

# La clase base comparte sus atributos y métodos con las clases derivadas.
# Ahora definimos entonces las clases derivadas Supervisor y Obrero:

class Supervisor(Persona):
    '''Clase que representa a un Supervisor'''

    def __init__(self, dni, nombre, apellido, telefono, rol):
        '''Constructor de clase Supervisor'''
        # Invocamos al constructor de la clase base
        Persona.__init__(self, dni, nombre, apellido, telefono)

        # Agregamos los atributos propios de esta clase
        self.rol = rol
        self.tareas = ['10','11','12','13']

    def __str__(self):
        '''Devuelve una cadena representativa al Supervisor'''
        return "%s: %s %s, rol: '%s', sus tareas: %s." % (
            self.__doc__[26:37], self.nombre, self.apellido, 
            self.rol, self.consulta_tareas())

    def consulta_tareas(self):
        '''Mostrar las tareas del Supervisor'''
        return ', '.join(self.tareas)

class Obrero(Persona):
    '''Clase que representa a un Obrero'''

    def __init__(self, dni, nombre, apellido, telefono, tareas):
        '''Constructor de clase Obrero'''
        # Invocamos al constructor de la clase base
        Persona.__init__(self, dni, nombre, apellido, telefono)

        # Agregamos los atributos propios de esta clase
        self.tareas = tareas

    def __str__(self):
        '''Devuelve una cadena representativa al Obrero'''
        return "%s: %s %s, sus tareas: %s." % (
            self.__doc__[26:37], self.nombre, self.apellido, self.consulta_tareas())

    def consulta_tareas(self):
        '''Mostrar las tareas del Obrero'''
        return ''.join(self.tareas)

# Creemos instancias de la clase derivada Supervisor:
supervisor_one = Supervisor("12345678", "Juan", "Perez", "3624123456", "Jefe de Calidad")
obrero_one = Obrero("51234567", "Pedro", "Picapiedras", "3624123456", '2,4,6,8,10')

# Imprimimos los detalles de la instancia creada:
print ("\n" + str(supervisor_one) + "\n")
print ("\n" + str(obrero_one) + "\n")

#-------------------------------------------------------------------------------------------------------
# Funcion issubclass()
# Es una función integrada de Python la cual le permite corroborar si un objeto es subclase de una clase.
# Sintaxis: issubclass(subclase, clase)
# Esta función devuelve True si la clase especificada es una subclase de la clase base, de lo contrario False.
# Usemos el ejemplo de las instancias definidas arriba:

print(issubclass(Supervisor, Persona))

#-------------------------------------------------------------------------------------------------------
# Funcion isinstance()
# Es una función integrada de Python la cual le permite corroborar si un objeto es instancia de una clase.
# Sintaxis: isinstance(subclase, clase)
# Esta función devuelve True si la clase especificada es una instancia de la clase indicada como argumento, de lo contrario False.
# Usemos el ejemplo de las instancias definidas arriba:

print(isinstance(supervisor_one, Persona))


#-------------------------------------------------------------------------------------------------------
# Funcion setattr()
# Permite establecer un atributo con nombre en un objeto; setattr(name, 'attributename', valor) es equivalente a name.attribute = valor

setattr(supervisor_one, 'email', 'jperez@mail.com')

#-------------------------------------------------------------------------------------------------------
# Funcion getattr()
# Permite consultar valor de un atributo usando el nombre de objeto; getattr(name, valor) es equivalente a name.valor
getattr(supervisor_one,'email')
print(getattr(supervisor_one,'email'))

# Herencia Múltiple ---------------------------------------------------------------------------------------------------------------------------------------------
# A diferencia de lenguajes como Java y C#, el lenguaje Python permite la herencia múltiple, es decir, se puede heredar de múltiples clases.
# La herencia múltiple es la capacidad de una subclase de heredar de múltiples súper clases.
# Como ejemplo vamos a implementar las clases del siguiente diagrama: https://bit.ly/30Zuo31
# Tomaremos la clase "Animal" como clase base, las clases "Terrestre","Acuatico" y "Cocodrilo" como clases derivadas. 
# Definimos primero entonces la clase Animal:

class Animal:
    '''Clase que representa un Animal'''
    def __init__(self, nombre):
        print("Se ejecuta el constructor de la clase Animal")
        self.nombre = nombre
        pass

    def mostrarNombre(self):
        print(f"El nombre del animal es: {self.nombre}")

# Definimos las clases derivadas del primer nivel "Terrestre" y "Acuatico":

class Terrestre:
    '''Clase que representa un Animal Terrestre'''
    def __init__(self):
        print("Se ejecuta el constructor de la clase Terrestre")
        pass

    def desplazar(self):
        print("El animal terrestre se desplaza")

class Acuatico:
    '''Clase que representa un Animal Acuatico'''
    def __init__(self):
        print("Se ejecuta el constructor de la clase Acuatico")
        pass

    def desplazar(self):
        print("El animal nada")


class Cocodrilo(Terrestre, Acuatico):
    def __init__(self):
        print("Se ejecuta el constructor de la clase Cocodrilo")
        pass


# Tomando en cuenta lo que indica el Diagrama de clases, la clase "Cocodrilo" deriva de dos clases base,
# la clase "Terrestre" y la clase "Acuatico"
# En el caso que tengamos que implementar Herencia Múltiple en Python debemos
# indicar en la definición cuales son las clases de las que deriva, 
# y es por eso que entre los paréntesis colocamos las clases "Terrestre" y "Acuatico". 
# Así como en el caso anterior de Herencia simple,
# la clase Cocodrilo hereda todos los atributos y métodos de las clases  "Terrestre" y "Acuatico".
# Creo una instancia de la clase Cocodrilo

un_cocodrilo = Cocodrilo()

# Llamo al método desplazar

un_cocodrilo.desplazar()

# En el caso en el que tengamos dos métodos con el mismo nombre incluidos en las clases base,
# como es el caso del método desplazar()
# incluido en la clase Acuatico y Terrestre al instanciarlo como en este caso Cocodrilo hereda ambos métodos 
# Para ejecutar el método desplazar(), Python se guía por el orden de ejecución. 
# Primero se busca si el método esta definido dentro de la clase. 
# Si no se encuentra, la búsqueda continúa en clases primarias en profundidad,
# de izquierda a derecha, sin buscar la misma clase dos veces. 
# Es por esto que al ejecutar el método desplazar() en este caso nos muestra el siguiente resultado: 
# Se ejecuta el constructor de la clase Cocodrilo. El animal terrestre se desplaza
# Comprobamos que se ejecuta el método desplazar() de la clase "Terrestre"
# porque en la definición de la clase Cocodrilo esta definida más a la izquierda.
# El orden de búsqueda es [Cocodrilo, Terrestre, Acuatico, Animal, Object]

# Podemos consultar el método de resolución de Python utilizando el atributo __mro__ o el método mro():
print(Cocodrilo.__mro__)
print(Cocodrilo.mro())



# Herencia Multininvel ---------------------------------------------------------------------------------------------------------------------------------------------
# La herencia multinivel es la capacidad de una subclase de heredar de una clase derivada.
# Como ejemplo vamos a implementar las clases del siguiente diagrama: https://bit.ly/30Zuo31
# Tomaremos la clase "Figura" como clase base, la clase "Poligono"
# como clase derivada de primer nivel y la clase "Cuadrilatero" como clase derivada de segundo nivel. 

# Definimos primero entonces la clase Figura:
class Figura:
    '''Clase que representa una Figura geométrica'''

    def __init__(self, area):
        print("Se ejecuta el constructor de la clase Figura")
        self.area = area

    def retornar_area(self):
        print("El área de la figura es:", self.area)


# Definimos la clase Poligono:
class Poligono(Figura):
    '''Clase que representa un Poligono'''

    def __init__(self, lados, area):
        Figura.__init__(self, area)
        self.lados = lados

    def retornar_lados(self):
        print("Los lados del poligono son:", self.lados)

# Definimos la clase Cuadrilatero:
class Cuadrilatero(Poligono):
    '''Clase que representa un Cuadrilatero'''

    def __init__(self, area):
        Poligono.__init__(self, 4, area)

# Poligono se deriva de Figura , y Cuadrilatero se deriva de Poligono por lo que
# Cuadrilatero tendra los métodos y atributos tanto de las clase Poligono como de la clase Figura. 
# Si en la clase Poligono alguno de las métodos de Figura es redefinido 
# Cuadrilatero heredara el método redefinido.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Polimorfismo 
# Es la capacidad que tienen los objetos de una clase de responder
# al mismo mensaje o evento en función de los parámetros utilizados durante su invocación.

# En una clase podemos aplicar polimorfismo al implementar dos métodos distintos
# en implementación pero con el mismo nombre. 
# Python al ser de tipado dinámico, no impone restricciones a los tipos 
# que se le pueden pasar a una función, por ejemplo, más allá de que el objeto se comporte como se espera. 
# Es por ello que encontramos funciones que aplican este concepto 
# y si bien usan un mismo nombre los resultados se adaptan a los datos que reciben como parámetros.

# Funciones por defecto que implementan polimorfismo en Python: 
# len()

# len() usada con una cadena como argumento
print(len("Data Science"))

# len() usada con una lista como argumento
print(len([1, 2, 3, 4]))


# Polimorfismo con métodos de clase y herencia: 
# Un objeto de una clase derivada es al mismo tiempo un objeto de la clase padre,
# de forma que allí donde se requiere un objeto de la clase padre también se puede
# utilizar uno de la clase hija.

class Animal:
    '''Clase que representa un Animal'''
    def __init__(self, nombre):
        print("Se ejecuta el constructor de la clase Animal")
        self.nombre = nombre
        pass

    def mostrarNombre(self):
        print(f"El nombre del animal es: {self.nombre}")

# Definimos las clases derivadas del primer nivel "Terrestre" y "Acuatico":

class Terrestre:
    '''Clase que representa un Animal Terrestre'''
    def __init__(self):
        print("Se ejecuta el constructor de la clase Terrestre")
        pass

    def desplazar(self):
        print("El animal terrestre se desplaza")

class Acuatico:
    '''Clase que representa un Animal Acuatico'''
    def __init__(self):
        print("Se ejecuta el constructor de la clase Acuatico")
        pass

    def desplazar(self):
        print("El animal nada")


class Cocodrilo(Terrestre, Acuatico):
    def __init__(self):
        print("Se ejecuta el constructor de la clase Cocodrilo")
        pass

# Sobrecarga de métodos: 
# Overriding Methods, le permite sustituir un método proveniente de la Clase Base,
# en la Clase Derivada debe definir un método con la misma forma 
# (es decir, mismo nombre de método y mismo número de parámetros que como está definido en la Clase Base).
# En Python no existe sobrecarga de métodos (el último método sobreescribiría
# la implementación de los anteriores), aunque se puede conseguir un comportamiento similar recurriendo 
# a funciones con valores por defecto para los parámetros o a la sintaxis *params o **params,
# o bien usando decoradores.

class Persona():
    '''Clase que representa una Persona'''
    def __init__ (self, dni):
        self.dni = dni

    def mensaje(self):
        print( "Mensaje desde la clase Persona" )

class Obrero(Persona):
    '''Clase que representa una Obrero'''

    def __init__ (self, dni):
        Persona.__init__(self, dni)
        self.__especialista = 1

    def mensaje(self):
        print ( "Mensaje desde la clase Obrero" )

# Creo una instancia
obrero_planta = Obrero ( 12345 )
obrero_planta.mensaje()

# Lo que se logra definiendo el método mensaje() en la Clase Derivada ( Obrero ) se conoce como 
# Método Overriding haciendo que cuando se cree el objeto (en este caso obrero_planta ) y se 
# llame al método mensaje() , este será tomado de la propia clase y no de la Clase Base Persona ). 
# Si comenta o borra el método mensaje() de la clase Obrero (Clase Derivada) y corre nuevamente 
# el código, el método llamado será el mensaje() de la Clase Base Persona .

# Sobrecarga de Operadores: 
# Overloading Operators, trata básicamente de lo mismo que la sobrecarga de métodos pero pertenece en esencia 
# al ámbito de los operadores aritméticos, binarios, de comparación y lógicos.

class Punto:
    def __init__ (self,x = 0 ,y = 0 ):
        self.x = x
        self.y = y

    def __add__ (self,other):
        x = self .x + other.x
        y = self .y + other.y
        return x, y

punto1 = Punto ( 4 , 6 )
punto2 = Punto ( 1 , -2 )
print (punto1 + punto2)