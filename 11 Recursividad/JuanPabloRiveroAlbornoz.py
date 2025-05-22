# Ejercicio 1: Factorial de un número recursivamente
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Mostrar factorial desde 1 hasta n
n = int(input("Ingresá un número: "))
for i in range(1, n + 1):
    print(f"{i}! = {factorial(i)}")



#Ejercicio 2: Fibonacci recursivamente
def fibonacci(pos):
    if pos == 0:
        return 0
    if pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)

# Mostrar serie hasta una posición 
n = int(input("Ingresá la posición hasta la que querés ver la serie de Fibonacci: "))
for i in range(n):
    print(f"F({i}) = {fibonacci(i)}")



#Ejercicio 3 : Potencia número recursivamente
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("Base: "))
exp = int(input("Exponente: "))
print(f"{base}^{exp} = {potencia(base, exp)}")


#Ejercicio 4: Conversion a Binario recursivamente
def a_binario(n):
    if n == 0:
        return ""
    return a_binario(n // 2) + str(n % 2)

numero = int(input("Ingresá un número en base decimal: "))
binario = a_binario(numero)
print(f"{numero} en binario es: {binario if binario else '0'}")


#Ejercicio 5: es palíndromo recursivamente
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingresá una palabra: ").lower()
print("Es palíndromo" if es_palindromo(texto) else "No es palíndromo")


#Ejercicio 6: Suma de los dígitos recursivamente
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

numero = int(input("Número entero positivo: "))
print(f"Suma de los dígitos: {suma_digitos(numero)}")


#Ejercicio 7: Contar bloques de una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

nivel_base = int(input("Bloques en el nivel inferior: "))
print(f"Total de bloques necesarios: {contar_bloques(nivel_base)}")

#Ejercicio 8: Contar dígitos 
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

num = int(input("Número: "))
dig = int(input("Dígito a contar: "))
print(f"Apariciones de {dig}: {contar_digito(num, dig)}")