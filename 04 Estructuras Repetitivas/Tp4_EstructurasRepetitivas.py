#1
for i in range(101):
    print(i)

#2
numero = int(input("Ingrese un número entero: "))
numero_abs = abs(numero)

if numero_abs == 0:
    print("El número ingresado tiene 1 dígito")
else:
    contador = 0
    while numero_abs > 0:
        numero_abs //= 10
        contador += 1
    print(f"El número ingresado tiene {contador} dígito(s)")

#3
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

if inicio > fin:
    inicio, fin = fin, inicio

suma = 0
for i in range(inicio + 1, fin):
    suma += i

print("La suma de los números entre los valores es:", suma)

#4
suma = 0
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print("La suma total es:", suma)

#5
import random

numeroAleatorio = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numeroAleatorio:
        print(f"¡Correcto! Lo lograste en {intentos} intento(s).")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")

#6
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

#7
numero = int(input("Ingrese un número entero positivo: "))

while numero < 0:
    print("Error: el número debe ser positivo.")
    numero = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(1, numero):
    suma += i

print(f"La suma de los números de 0 a {numero} es: {suma}")

#8
pares = impares = positivos = negativos = 0
cantidad = 100

for _ in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#9
suma = 0
cantidad = 2

for _ in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / cantidad
print("La media de los números ingresados es:", media)

#10
numero = int(input("Ingrese un número entero: "))
invertido = 0
numero_abs = abs(numero)

while numero_abs > 0:
    digito = numero_abs % 10
    invertido = invertido * 10 + digito
    numero_abs //= 10

if numero < 0:
    invertido *= -1

print("Número invertido:", invertido)
