import math  
# 1) Imprimir "saludo" en la consola

print("Hola Mundo!")

# 2) Pedir el nombre del usuario e imprimir un saludo
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")    

# 3) Pedir nombre, apellido, edad y lugar de residencia e imprimirlos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

# 4) Calcular el área y perímetro de un círculo
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El área es {area:.2f} y el perímetro es {perimetro:.2f}")

# 5)  Conversión de segundos a horas

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# 6)  Tabla de multiplicación
numero = int(input("Ingrese un número: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# 7)  Operaciones con dos números
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))

if num1 == 0 or num2 == 0:
    print("Los números deben ser distintos de 0.")
else:
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    print(f"División: {num1 / num2:.2f}")
    print(f"Modulo: {num1 % num2}")
    print(f"Potencia: {num1 ** num2}")

# 8)  Índice de Masa Corporal (IMC)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")


# 9)  Conversión de Celsius a Fahrenheit
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# 10) Promedio de 3 números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio:.2f}")