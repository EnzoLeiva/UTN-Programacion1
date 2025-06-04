
import random
import time

# Arrays para almacenar los resultados de las conversiones
resultados_for = []
resultados_recursivo = []

# Esta función genera una lista de cadenas binarias aleatorias de longitud fija
# param cantidad: Cantidad de números binarios a generar
# return: Lista de cadenas binarias de 32 bits
def generar_binarios(cantidad):
    binarios = []
    for i in range(cantidad):
        # Con la librería random genero un número entero aleatorio entre 0 y 2^32 - 1
        numero = random.randint(0, 2**32 - 1)
        # Guardo el numero en formato binario de 32 bits
        # f'032b' asegura que el número se represente con 32 bits, rellenando con ceros a la izquierda si es necesario
        binarios.append(format(numero, f'032b'))
    return binarios

# Función para convertir binario a decimal usando un ciclo for
# param binario: Lista de cadenas binarias a convertir
# return: Tiempo que tarda en convertir todos los binarios a decimal
def binario_a_decimal_for(binarios):
    # Inicio tiempo para medir la conversión
    inicio = time.time()
    # Recorro lista de binarios y convierto cada uno a decimal
    for b in binarios:
        # Inicializo el decimal en 0
        decimal = 0
        # Recorro cada bit del binario y    
        for i in range(len(b)):
            # Obtengo el bit en la posición i
            bit = int(b[i])
            # Calculo la potencia de 2 correspondiente
            potencia = len(b) - 1 - i
            # Acumulo el valor en decimal
            decimal += bit * (2 ** potencia)
        # Almaceno el resultado en la lista de resultados
        resultados_for.append(decimal)
    # Fin tiempo de conversión
    fin = time.time()

    return fin - inicio

# Función para convertir binario a decimal de forma recursiva
# param binario: binario como cadena de caracteres
def binario_a_decimal_recursivo(binario):
    #caso base: si la cadena está vacía, retorno 0
    if binario == "":
        return 0
    # Tomo el bit mas significativo [0] y lo multiplico por 2 elevado a la potencia de su posición
    # y sumo el resultado de la llamada recursiva a lo que queda de la cadena
    # al invocar con binario[1:] no envio la primer posicion que es la que estoy procesando
    # y así voy reduciendo la cadena hasta que quede vacía
    return int(binario[0]) * (2 ** (len(binario) - 1)) + binario_a_decimal_recursivo(binario[1:])

# Función para medir el tiempo de conversión recursiva
# param binarios: Lista de cadenas binarias a convertir
# return: Tiempo que tarda en convertir todos los binarios a decimal
def convertir_recursivo(binarios):
    inicio = time.time()
    for b in binarios:
        # Llamo a la función recursiva para convertir cada binario y almaceno el resultado en la lista de resultados
        resultados_recursivo.append(binario_a_decimal_recursivo(b))
    fin = time.time()
    return fin - inicio

def main():
    # Definimos las cantidades de binarios a generar
    cantidades = [10000, 30000, 50000, 100000, 250000]
    #cantidades = [1000000,2000000,3000000,4000000,5000000]
    
    print("Iniciando comparación. Esto puede tardar unos minutos...")

    # Iteramos sobre las cantidades de binarios
    for cantidad in cantidades:
        print(f"Procesando {cantidad} binarios...")

        # Generar binarios
        binarios = generar_binarios(cantidad)

        # Transformar y medir tiempo con ciclo for
        tiempo_for = binario_a_decimal_for(binarios)
        
        # Tiempo con recursividad
        tiempo_rec = convertir_recursivo(binarios)
        
        # Imprimir resultados por cada cantidad
        print(f"{cantidad} elementos - Iterativo: {tiempo_for:.8f}s - Recursivo: {f'{tiempo_rec:.8f}s'}")
        
        # Ahora comparamos los resultados
        errores = []
        for i in range(len(binarios)):
            if resultados_for[i] != resultados_recursivo[i]:
                errores.append((binarios[i], resultados_for[i], resultados_recursivo[i]))

        # Mostrar resultados incorrectos
        if errores:
            print("Diferencias encontradas entre métodos:")
            for b, f, r in errores:
                print(f"Binario: {b} → for: {f} | recursivo: {r}")
        else:
            print("Todos los resultados coinciden entre los dos algoritmos.")

main()
