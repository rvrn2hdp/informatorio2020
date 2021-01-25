""" ejercicio 5
 Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser
 instanciada indicando: los tres atributos, sólo la hora y minuto,o sólo la hora.
 Crear además los métodos necesarios para modificar la hora en cualquier
 momento de forma manual. Mantenga la integridad de los datos en todo momento
 definiendo de tipo “private”. Crear  una  clase prueba_tiempo que
 prueba  una  hora  concreta  y  la  modifique  a  su  gusto  mostrándola  por pantalla.
"""

class Tiempo(object):
    def __init__(self, hora=00, minuto=00, segundo=00):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def __str__(self):
        return f"{self.__hora}:{self.__minuto}:{self.__segundo}"

    