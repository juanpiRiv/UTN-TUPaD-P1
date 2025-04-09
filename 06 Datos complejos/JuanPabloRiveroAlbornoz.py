import math
from collections import deque

# ----------------------------------------------
# Actividad 1: Agregar frutas al diccionario
# ----------------------------------------------

precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Agrego las frutas nuevas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Frutas actualizadas:", precios_frutas)

# ----------------------------------------------
# Actividad 2: Actualizar precios
# ----------------------------------------------

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Precios actualizados:", precios_frutas)

# ----------------------------------------------
# Actividad 3: Lista solo con las frutas
# ----------------------------------------------

frutas = list(precios_frutas.keys())
print("Lista de frutas:", frutas)

# ----------------------------------------------
# Actividad 4: Clase Persona con saludo
# ----------------------------------------------

class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

# Ejemplo
p1 = Persona("Lucía", "Argentina", 25)
p1.saludar()

# ----------------------------------------------
# Actividad 5: Clase Círculo con área y perímetro
# ----------------------------------------------



class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Ejemplo
c1 = Circulo(4)
print("Área:", c1.calcular_area())
print("Perímetro:", c1.calcular_perimetro())

# ----------------------------------------------
# Actividad 6: Verificar paréntesis balanceados
# ----------------------------------------------

def estan_balanceados(expresion):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}
    for char in expresion:
        if char in pares.values():
            pila.append(char)
        elif char in pares:
            if not pila or pila.pop() != pares[char]:
                return False
    return not pila

# Ejemplos de prueba
print("({[]}) balanceado?", estan_balanceados("({[]})"))  # True
print("([)] balanceado?", estan_balanceados("([)]"))      # False

# ----------------------------------------------
# Actividad 7: Cola para turnos en el banco
# ----------------------------------------------


class Banco:
    def __init__(self):
        self.cola = deque()

    def agregar_cliente(self, cliente):
        self.cola.append(cliente)
        print(f"Cliente {cliente} agregado.")

    def atender_cliente(self):
        if self.cola:
            cliente = self.cola.popleft()
            print(f"Atendiendo a {cliente}")
        else:
            print("No hay clientes en la cola.")

    def siguiente_cliente(self):
        if self.cola:
            print(f"Siguiente en la fila: {self.cola[0]}")
        else:
            print("La fila está vacía.")

# Ejemplo
banco = Banco()
banco.agregar_cliente("Ana")
banco.agregar_cliente("Carlos")
banco.siguiente_cliente()
banco.atender_cliente()
banco.siguiente_cliente()

# ----------------------------------------------
# Actividad 8: Lista enlazada - insertar y recorrer
# ----------------------------------------------

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo
lista = ListaEnlazada()
lista.insertar_inicio(10)
lista.insertar_inicio(20)
lista.insertar_inicio(30)
print("Lista enlazada:")
lista.mostrar()

# ----------------------------------------------
# Actividad 9: Invertir lista enlazada
# ----------------------------------------------

class ListaInvertible(ListaEnlazada):
    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            sig = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = sig
        self.cabeza = anterior

# Ejemplo
lista2 = ListaInvertible()
lista2.insertar_inicio(1)
lista2.insertar_inicio(2)
lista2.insertar_inicio(3)
print("Original:")
lista2.mostrar()
lista2.invertir()
print("Invertida:")
lista2.mostrar()
