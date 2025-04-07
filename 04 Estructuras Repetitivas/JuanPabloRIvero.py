import random  # Lo necesito para el juego de adivinar

# 1) Imprimo todos los enteros de 0 a 100
for i in range(101):      # range(101) va de 0 hasta 100
    print(i)
print()  # separo con línea en blanco

# 2) Cuento cuántos dígitos tiene un entero
n = input("Ingrese un número entero: ")
num = n.lstrip('-')       # quito el '-' si lo ingresó negativo
print(f"Tiene {len(num)} dígitos.")
print()

# 3) Sumo los enteros entre dos valores (sin incluirlos)
a = int(input("Primer valor: "))
b = int(input("Segundo valor: "))
inicio, fin = min(a, b), max(a, b)
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print(f"Suma entre {inicio} y {fin} (sin extremos): {suma}")
print()

# 4) Voy sumando números hasta que ingrese 0
total = 0
while True:
    n = int(input("Número (0 para terminar): "))
    if n == 0:
        break
    total += n
print(f"Total acumulado: {total}")
print()

# 5) Juego: adivinar un número entre 0 y 9
secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina (0-9): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Lo lograste en {intentos} intentos!")
        break
    else:
        print("No es, probá de nuevo.")
print()

# 6) Imprimo los pares de 100 a 0 en orden inverso
for i in range(100, -1, -2):  # empiezo en 100, bajo de 2 en 2
    print(i)
print()

# 7) Sumo todos los números de 0 a N
n = int(input("Ingrese N (positivo): "))
suma = 0
for i in range(n + 1):
    suma += i
print(f"Suma de 0 a {n}: {suma}")
print()

# 8) De 100 números, cuento pares, impares, negativos y positivos
pares = impares = negativos = positivos = 0
cantidad = 100  # lo cambio para probar menos si quiero
for _ in range(cantidad):
    x = int(input("Ingrese un entero: "))
    if x < 0:
        negativos += 1
    elif x > 0:
        positivos += 1
    if x % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Pares: {pares}, Impares: {impares}, Negativos: {negativos}, Positivos: {positivos}")
print()

# 9) Calculo la media de 100 números
total = 0
cantidad = 100
for _ in range(cantidad):
    x = int(input("Ingrese un entero: "))
    total += x
media = total / cantidad
print(f"Media de {cantidad} números: {media:.2f}")
print()

# 10) Invierto los dígitos de un número
n = input("Número a invertir: ")
signo = ''
if n.startswith('-'):
    signo = '-'
    n = n[1:]
invertido = n[::-1]  # doy vuelta la cadena
print("Invertido:", signo + invertido)