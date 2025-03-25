#1) 
print("Hola Mundo!")

#2) 
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

#3) 
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#4) 
import math
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es {area} y su perímetro es {perimetro}.")

#5) 
segundos = int(input("Ingresa una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

#6) 
numero = int(input("Ingresa un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#7) 
num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

#8) 
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc}")

#9) 
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit}")

#10)
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio}")