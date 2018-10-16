#Autor: Arturo Márquez Olivar. A01376086.
#Realiza varias funciones especificadas en la misión 07.


#Realiza una división restando y determina el cociente y el residuo.
def dividir(divisor, dividendo):
    cociente = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente += 1
    print(cociente, ", sobra", dividendo)


#Recibe dígitos ingresados por el usuario y los compara para ver cual es el mayor.
def encontrarMayor():
    datos = []
    print("Teclea una serie de números para encontrar al mayor.")
    numero = int(input("Teclea un número [-1 para salir]: "))

    while numero != -1:
        datos.append(numero)
        numero = int(input("Teclea un número [-1 para salir]:"))
    if len(datos) > 0:
        print("El mayor es:", max(datos))
    else:
        print("No hay valor mayor.")


#Función principal. Contiene el menú en el cual el usuario decide qué hacer, recibe datos y los imprime.
def main():

    opcion = 0

    while opcion != 3:
        print("""Misión 07. Ciclos while
Autor: Arturo Márquez Olivar
Matrícula: A01376086
1. Calcular divisiones
2. Encontrar mayor
3. Salir""")
        opcion = int(input("Teclea tu opción:"))
        print("")

        if opcion == 1:
            print("Calculando divisiones")
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))

            print("%d / %d = "% (dividendo, divisor), end =""), dividir(divisor, dividendo)
            print("")

        elif opcion == 2:
            encontrarMayor()
            print("")

        elif opcion == 3:
            print("Gracias por usar este programa, regresa pronto.")

        else:
            print("""ERROR, teclea 1, 2 o 3
            """)
    exit()


#Llamada a la función main.
main()