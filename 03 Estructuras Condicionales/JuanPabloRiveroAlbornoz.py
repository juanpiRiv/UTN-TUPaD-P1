
import random
from statistics import mode, median, mean, StatisticsError
# 1)  Verificar si es mayor de edad 
edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


# 2)  Verificar si es aprobado o desaprobado
nota = float(input("Por favor, ingresa tu nota: "))

# Evaluar la nota e imprimir el resultado
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# 3)  Verificar si el número es par
while True:
    # Solicitar al usuario que ingrese un número
    numero = int(input("Por favor, ingrese un número: "))

    # Verificar si el número es par
    if numero % 2 == 0:
        print("Ha ingresado un número par")
        break
    else:
        print("Por favor, ingrese un número par")


# 4)  Determinar la categoría según la edad
edad = int(input("Por favor, ingresa tu edad: "))

# Determinar la categoría según la edad
if edad < 12:
    print("Niño/a: menor de 12 años.")
elif 12 <= edad < 18:
    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif 18 <= edad < 30:
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
else:
    print("Adulto/a: mayor o igual que 30 años.")

# 5)  Verificar la longitud de la contraseña
contraseña = input("Por favor, ingrese su contraseña: ")

# Evaluar la longitud de la contraseña
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6)  Calcular los parámetros estadísticos
# Generar una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular los parámetros estadísticos
try:
    moda = mode(numeros_aleatorios)  # Calcula la moda
except StatisticsError:  # Usar el nombre específico de la excepción
    moda = None  # Manejo de error en caso de que no haya una única moda
mediana = median(numeros_aleatorios)  # Calcula la mediana
media = mean(numeros_aleatorios)  # Calcula la media

# Comparar los valores para determinar el tipo de sesgo
if moda is not None:
    if media > mediana > moda:
        sesgo = "Sesgo positivo (a la derecha)"
    elif media < mediana < moda:
        sesgo = "Sesgo negativo (a la izquierda)"
    elif media == mediana == moda:
        sesgo = "Sin sesgo"
    else:
        sesgo = "No se puede determinar el sesgo claramente"
else:
    sesgo = "No se puede calcular la moda"

# Imprimir resultados
print("Lista de números aleatorios:", numeros_aleatorios)
print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)
print("Tipo de sesgo:", sesgo)


# 7)  Añadir signo de exclamación al final de la frase
texto = input("Por favor, ingrese una frase o palabra: ")

# Verificar si el último carácter es una vocal
if texto[-1].lower() in "aeiou":
    texto += "!"  # Añadir signo de exclamación al final

# Imprimir el resultado
print(texto)


# 8)  Transformar el nombre según la opción elegida
nombre = input("Por favor, ingresa tu nombre: ")

# Solicitar la opción al usuario
print("Selecciona una opción:")
print("1. Mostrar el nombre en mayúsculas.")
print("2. Mostrar el nombre en minúsculas.")
print("3. Mostrar el nombre con la primera letra en mayúscula.")
opcion = int(input("Ingresa el número de la opción deseada (1, 2 o 3): "))

# Realizar la transformación según la opción elegida
if opcion == 1:
    print(nombre.upper())  # Convierte el nombre a mayúsculas
elif opcion == 2:
    print(nombre.lower())  # Convierte el nombre a minúsculas
elif opcion == 3:
    print(nombre.title())  # primera letra de cada palabra a mayúscula
else:
    print("Opción no válida. Por favor, selecciona 1, 2 o 3.")


# 9)  Clasificar la magnitud según la escala de Richter
magnitud = float(input("Por favor, ingrese la magnitud del terremoto: "))

# Clasificar la magnitud según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")


# 10)  Determinar la estación según el hemisferio y la fecha
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("Por favor, ingresa el mes (como número del 1 al 12): "))
dia = int(input("Por favor, ingresa el día del mes: "))

# Determinar la estación según el hemisferio y la fecha
# Solicitar información al usuario
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("Por favor, ingresa el mes (como número del 1 al 12): "))
dia = int(input("Por favor, ingresa el día del mes: "))

# Determinar la estación según el hemisferio y la fecha
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or \
       (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or \
         (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or \
         (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or \
       (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or \
         (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or \
         (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

# Imprimir la estación del año
print(f"La estación en la que te encuentras es: {estacion}")