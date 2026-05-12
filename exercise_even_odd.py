def even_odd():
    """
    Ejercicio 2 - Par o Impar

    Leer un número entero mediante input(). Determinar si el número es par o impar
    e imprimir el resultado correspondiente.

    Ejemplo:
        Para la entrada "8", la salida esperada es:
        El numero 8 es par

        Para la entrada "7", la salida esperada es:
        El numero 7 es impar
    """
    pass
    #PARA SABER UE ES PAR --> NUM %2 == 0      OR      NUM %2 !=0

    numero = int(input("Ingrese el numero: "))
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    elif numero % 2 != 0:
        print(f"El numero {numero} es impar")
even_odd()  