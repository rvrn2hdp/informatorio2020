'''Ejercicio 12: Próximo Siguiente
 En este ejercicio creará una función llamada proximo_primo que encuentra
 y devuelve el primer número primo mayor que algún número entero, n.
 El valor de n se pasará a la función como su único parámetro.
 Incluya un programa principal que lea un número entero del usuario
 y muestre el primer número primo mayor que el valor ingresado.
'''

def proximo_primo(n):
    while True:
        n += 1
        cont = 0
        acu = 1
        
        while acu <= n:
            if n % acu == 0:
                cont += 1
            acu += 1
        
        if cont == 2:
            return n
        
def principal():
    print("Inicio")
    valor = int(input("Ingrese un número entero: "))
    print(f"El próximo número primo de {valor} es {proximo_primo(valor)}.")

principal()