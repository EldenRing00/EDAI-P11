def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


def fibonacci_inverso(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [1, 0]
    else:
        fibo = fibonacci_inverso(n - 1)
        fibo.append(fibo[-1] + fibo[-2])
        return fibo


def mostrar_menu():
    print("Bienvenido, puede realizar las siguientes operaciones:")
    print("1. Conversión de bases")
    print("2. Serie de Fibonacci")
    print("3. Salir")


def ejecutar_conversion():
    num_decimal = int(input("Ingrese el número decimal a convertir: "))
    num_binario = decimal_a_binario(num_decimal)
    print(f"El número binario equivalente es: {num_binario}")


def ejecutar_fibonacci():
    num_terminos = int(input("Ingrese el número de términos de la serie 
de Fibonacci: "))
    serie_inversa = fibonacci_inverso(num_terminos)
    print("Los términos de la serie de Fibonacci en orden inverso son:")
    for termino in serie_inversa:
        print(termino)


# Programa principal
while True:
    mostrar_menu()
    opcion = input("Ingrese la opción: ")
    
    if opcion == "1":
        ejecutar_conversion()
    elif opcion == "2":
        ejecutar_fibonacci()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")


