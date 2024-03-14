import math


def es_numero(dato):
    try:
        float(dato)
        return True
    except ValueError:
        return False


def resolver_ecuacion_cuadratica(a=None, b=None, c=None):
    # Resolver la ecuación cuadrática
    try:
        if c is None:
            c = math.sqrt(a ** 2 + b ** 2)
            return round(c, 2)
        elif b is None:
            b = math.sqrt(c ** 2 - a ** 2)
            return round(b, 2)
        elif a is None:
            a = math.sqrt(c ** 2 - b ** 2)
            return round(a, 2)
    except ValueError:
        print("Error: No se pudo resolver la ecuación cuadrática.")
        return None


active = True

while active:

    print("Bienvenido al programa de resolución de ecuaciones cuadráticas")
    print("Seleccione una opción:")
    print("1. Resolver ecuación cuadrática")
    print("2. Salir")

    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        print("Resolviendo ecuación cuadrática...")
        # Solicitar las variables al usuario y validar que sean números
        variable_A_input = input("Por favor ingrese el valor de la variable A (deje en blanco si es desconocida): ")
        variable_B_input = input("Por favor ingrese el valor de la variable B (deje en blanco si es desconocida): ")
        variable_C_input = input("Por favor ingrese el valor de la variable C (deje en blanco si es desconocida): ")

        # Verificar que los inputs sean números
        lista_inputs = [variable_A_input, variable_B_input, variable_C_input]

        verificador = True

        for input in lista_inputs:
            if not es_numero(input) and input != "":
                print("Error: Los inputs deben ser números.")
                verificador = False
                break

        if not verificador:
            break

        # Convertir los inputs a float si no están vacíos, o a None si están vacíos
        variable_A = float(variable_A_input) if variable_A_input.strip() != "" else None
        variable_B = float(variable_B_input) if variable_B_input.strip() != "" else None
        variable_C = float(variable_C_input) if variable_C_input.strip() != "" else None

        # Verificar cuántas variables son desconocidas
        desconocidas = sum(1 for v in (variable_A, variable_B, variable_C) if v is None)
        if desconocidas > 1 or desconocidas == 0:
            print("Error: Deje exactamente una variable en blanco para resolver.")
            break

        # Resolver la ecuación cuadrática
        resultado = resolver_ecuacion_cuadratica(a=variable_A, b=variable_B, c=variable_C)

        if resultado is not None:
            print("El valor de la variable desconocida es:", resultado)

        active = False

    elif opcion == "2":
        print("Saliendo del programa...")
        active = False