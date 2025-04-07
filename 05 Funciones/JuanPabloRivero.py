def imprimir_hola_mundo():
    """Actividad 1: Imprime el mensaje 'Hola Mundo!'"""
    print("Hola Mundo!")


def saludar_usuario(nombre):
    """Actividad 2: Recibe un nombre y devuelve un saludo personalizado."""
    return f"Hola {nombre}!"


def informacion_personal(nombre, apellido, edad, residencia):
    """Actividad 3: Imprime información personal formateada."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


def calcular_area_circulo(radio):
    """Actividad 4: Devuelve el área de un círculo dado su radio."""
    import math
    return math.pi * radio ** 2


def calcular_perimetro_circulo(radio):
    """Actividad 4: Devuelve el perímetro de un círculo dado su radio."""
    import math
    return 2 * math.pi * radio


def segundos_a_horas(segundos):
    """Actividad 5: Convierte segundos a horas."""
    return segundos / 3600


def tabla_multiplicar(numero):
    """Actividad 6: Imprime la tabla de multiplicar del número del 1 al 10."""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def operaciones_basicas(a, b):
    """Actividad 7: Devuelve una tupla con suma, resta, multiplicación y división de a y b."""
    suma = a + b
    resta = a - b
    producto = a * b
    division = None
    if b != 0:
        division = a / b
    return suma, resta, producto, division


def calcular_imc(peso, altura):
    """Actividad 8: Calcula y devuelve el Índice de Masa Corporal (IMC)."""
    return peso / (altura ** 2)


def celsius_a_fahrenheit(celsius):
    """Actividad 9: Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32


def calcular_promedio(a, b, c):
    """Actividad 10: Devuelve el promedio de tres números."""
    return (a + b + c) / 3


def main():
    # Actividad 1
    imprimir_hola_mundo()

    # Actividad 2
    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))

    # Actividad 3
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    # Actividad 4
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")

    # Actividad 5
    segundos = int(input("Ingrese cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"Equivalente en horas: {horas:.2f} h")

    # Actividad 6
    num = int(input("Ingrese un número para su tabla de multiplicar: "))
    tabla_multiplicar(num)

    # Actividad 7
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    suma, resta, producto, division = operaciones_basicas(a, b)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {producto}")
    if division is not None:
        print(f"División: {division}")
    else:
        print("División: No se puede dividir por cero.")

    # Actividad 8
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")

    # Actividad 9
    celsius = float(input("Ingrese temperatura en Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"Equivalente en Fahrenheit: {fahrenheit:.2f}°F")

    # Actividad 10
    x = float(input("Ingrese el primer número para promedio: "))
    y = float(input("Ingrese el segundo número para promedio: "))
    z = float(input("Ingrese el tercer número para promedio: "))
    promedio = calcular_promedio(x, y, z)
    print(f"El promedio es: {promedio:.2f}")

if __name__ == "__main__":
    main()
