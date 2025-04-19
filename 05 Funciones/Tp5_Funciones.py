import math

# 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2
def saludar_usuario(nombre):
    return f"Hola {nombre}"

# 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4
def calcular_area_circulo(radio):
    return math.pi * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5
def segundos_a_horas(segundos):
    return segundos / 3600

# 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Infinito"
    return (suma, resta, multiplicacion, division)

# 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# -------------------------------
# Programa principal
# -------------------------------

# 1
imprimir_hola_mundo()

# 2
nombre = input("Ingresá tu nombre: ")
print(saludar_usuario(nombre))

# 3
nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
residencia = input("¿Dónde vivís? ")
informacion_personal(nombre, apellido, edad, residencia)

# 4
radio = float(input("Ingresá el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

# 5
segundos = int(input("Ingresá una cantidad de segundos: "))
print(f"Equivalen a {segundos_a_horas(segundos):.2f} horas")

# 6
numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# 7
a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
suma, resta, multi, div = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multi}, División: {div}")

# 8
peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

# 9
celsius = float(input("Ingresá la temperatura en °C: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"Equivale a {fahrenheit:.2f} °F")

# 10
a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
c = float(input("Ingresá el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio es: {promedio:.2f}")
