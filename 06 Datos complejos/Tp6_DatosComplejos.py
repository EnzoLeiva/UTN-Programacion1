#1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agregar nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#3
solo_frutas = list(precios_frutas.keys())
print("Lista de frutas:", solo_frutas)

#4
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

# Prueba clase Persona
persona1 = Persona("Rocío", "Argentina", 25)
persona1.saludar()

#5)
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Prueba clase Circulo
c = Circulo(5)
print("Área:", c.calcular_area())
print("Perímetro:", c.calcular_perimetro())

#6)
def esta_balanceado(cadena):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for caracter in cadena:
        if caracter in '({[':
            pila.append(caracter)
        elif caracter in ')}]':
            if not pila or pila.pop() != pares[caracter]:
                return False
    return len(pila) == 0

# Prueba balanceo
print("([]{}) está balanceado:", esta_balanceado("([]{})"))  # True
print("([)] está balanceado:", esta_balanceado("([)]"))      # False

#7
from collections import deque

cola = deque()

def encolar(cliente):
    cola.append(cliente)

def desencolar():
    if cola:
        return cola.popleft()
    else:
        return "No hay clientes"

def siguiente_cliente():
    return cola[0] if cola else "No hay clientes"

# Prueba sistema de turnos
encolar("Cliente 1")
encolar("Cliente 2")
print("Siguiente cliente:", siguiente_cliente())
print("Atendiendo:", desencolar())
print("Siguiente cliente:", siguiente_cliente())

#8
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Prueba lista enlazada
lista = ListaEnlazada()
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(2)
lista.insertar_al_inicio(1)
print("Lista original:")
lista.recorrer()

#9
def invertir_lista(lista):
    anterior = None
    actual = lista.cabeza
    while actual:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente
    lista.cabeza = anterior

# Prueba inversión
invertir_lista(lista)
print("Lista invertida:")
lista.recorrer()
