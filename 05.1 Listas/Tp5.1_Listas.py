#1
lista_multiplos_4 = list(range(4, 101, 4))
print("Múltiplos de 4:", lista_multiplos_4)

#2
lista = [1, 2, 3, 4, 5]
print("Penúltimo elemento:", lista[-2])

#3
lista_vacia = []
lista_vacia.append("Programacion")
lista_vacia.append("UTN")
lista_vacia.append("Python")
print("Lista con valores añadidos:", lista_vacia)

#4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("Lista modificada:", animales)

#5
# En la primer línea, crea una lista con 5 elementos, en este caso números. En la segunda obtiene el maximo y lo elimina y en la tercera muestra la lista por pantalla

#6
lista_saltos = list(range(10, 31, 5))
print("Dos primeros números:", lista_saltos[:2])

#7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["volkswagen", "ford"]
print("Lista de autos modificada:", autos)

#8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista de dobles:", dobles)

#9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")                     
compras[1][1] = "tallarines"                 
compras[0].remove("pan")                     
print("Lista de compras modificada:", compras)

#10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("Lista anidada:", lista_anidada)
