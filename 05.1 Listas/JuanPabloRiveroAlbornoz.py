#1 Creamos la lista de múltiplos de 4 entre 1 y 100
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)


#2 Lista con 5 elementos que me gusten
gustos = ["pizza", "helado", "sushi", "asado", "tarta"]
# Mostramos el penúltimo elemento
print("Penúltimo elemento:", gustos[-2])

#3 Lista vacía
lista_vacia = []
# Agregamos tres palabras con append
lista_vacia.append("python")
lista_vacia.append("listas")
lista_vacia.append("diversión")
# Mostramos la lista resultante
print(lista_vacia)


#4 Lista original
animales = ["perro", "gato", "conejo", "pez"]
# Reemplazamos el segundo y el último valor
animales[1] = "loro"
animales[-1] = "oso"
# Mostramos la lista resultante
print(animales)

#5 analizar lista
# Creamos una lista de números
numeros = [8, 15, 3, 22, 7]
# Eliminamos el número más grande de la lista
# max(numeros) encuentra el mayor (22)
# numeros.remove(...) elimina ese valor de la lista
numeros.remove(max(numeros))
# Mostramos la lista actualizada (sin el 22)
print(numeros)


#6 Creamos la lista del 10 al 30, de 5 en 5
numeros = list(range(10, 31, 5))
# Mostramos los dos primeros elementos
print(numeros[0], numeros[1])
#salida 10 15 


#7 Lista original  Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
autos = ["sedan", "polo", "suran", "gol"]
# Reemplazamos los valores en las posiciones 1 y 2
autos[1] = "camioneta"
autos[2] = "coupe"
# Mostramos la lista resultante
print(autos)

#8 Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)  # Resultado: [10, 20, 30]

#9 Dada la lista “compras”, realizar las operaciones solicitadas
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append
compras[2].append("jugo")
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][compras[1].index("fideos")] = "tallarines"
# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")
# d) Imprimir la lista resultante
print(compras)


#10 Elaborar una lista anidada llamada “lista_anidada” con los elementos solicitados
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
#Resultado: [15, True, [25.5, 57.9, 30.6], False]
