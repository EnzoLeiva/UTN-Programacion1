#1
def factorial(x):
    return 1 if x == 0 else x * factorial(x-1)

valor = int(input("Ingrese un número: "))
for i in range(1, valor + 1):
    print(f"{i}! = {factorial(i)}")

#2
def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion-1) + fibonacci_recursivo(posicion-2)
    
pos = int(input("Ingrese la posición de la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(pos + 1):
    print(fibonacci_recursivo(i), end=" ")

#3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

#4
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(numero)
print(f"Binario: {binario if binario != '' else '0'}")

#5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower()
print("Es palíndromo." if es_palindromo(texto) else "No es palíndromo.")

#6
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número: "))
print(f"Suma de sus dígitos: {suma_digitos(numero)}")

#7
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

bloques_base = int(input("Bloques en el nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(bloques_base)}")

#8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número: "))
digito = int(input("Ingrese el dígito a contar (0-9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")
