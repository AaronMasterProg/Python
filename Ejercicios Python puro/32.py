def ingresar_matriz(filas, columnas):
    print(f"Ingresa los elementos de una matriz de {filas}x{columnas}:")
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    elemento = float(input(f"Elemento [{i+1},{j+1}]: "))
                    fila.append(elemento)
                    break
                except ValueError:
                    print("Por favor, ingresa un número válido.")
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{elemento:.2f}" for elemento in fila))

def sumar_matrices(matriz1, matriz2):
    return [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]

def restar_matrices(matriz1, matriz2):
    return [[matriz1[i][j] - matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]

def multiplicar_matrices(matriz1, matriz2):
    filas_m1 = len(matriz1)
    columnas_m1 = len(matriz1[0])
    columnas_m2 = len(matriz2[0])
    resultado = [[0] * columnas_m2 for _ in range(filas_m1)]
    for i in range(filas_m1):
        for j in range(columnas_m2):
            for k in range(columnas_m1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado

def transponer_matriz(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def main():
    print("📊 Calculadora de Matrices 📊")
    while True:
        print("\nOperaciones disponibles:")
        print("1. Sumar matrices")
        print("2. Restar matrices")
        print("3. Multiplicar matrices")
        print("4. Transponer matriz")
        print("5. Salir")
        
        try:
            opcion = int(input("Elige una opción (1-5): "))
            if opcion == 1 or opcion == 2:
                filas = int(input("Número de filas: "))
                columnas = int(input("Número de columnas: "))
                print("Matriz 1:")
                matriz1 = ingresar_matriz(filas, columnas)
                print("Matriz 2:")
                matriz2 = ingresar_matriz(filas, columnas)
                if opcion == 1:
                    resultado = sumar_matrices(matriz1, matriz2)
                    print("Resultado de la suma:")
                else:
                    resultado = restar_matrices(matriz1, matriz2)
                    print("Resultado de la resta:")
                imprimir_matriz(resultado)
            elif opcion == 3:
                filas1 = int(input("Número de filas de la primera matriz: "))
                columnas1 = int(input("Número de columnas de la primera matriz: "))
                matriz1 = ingresar_matriz(filas1, columnas1)
                filas2 = columnas1
                columnas2 = int(input("Número de columnas de la segunda matriz: "))
                matriz2 = ingresar_matriz(filas2, columnas2)
                resultado = multiplicar_matrices(matriz1, matriz2)
                print("Resultado de la multiplicación:")
                imprimir_matriz(resultado)
            elif opcion == 4:
                filas = int(input("Número de filas: "))
                columnas = int(input("Número de columnas: "))
                matriz = ingresar_matriz(filas, columnas)
                resultado = transponer_matriz(matriz)
                print("Resultado de la transposición:")
                imprimir_matriz(resultado)
            elif opcion == 5:
                print("¡Gracias por usar la calculadora de matrices!")
                break
            else:
                print("Por favor, elige una opción válida.")
        except ValueError:
            print("Entrada inválida. Por favor, intenta nuevamente.")

if __name__ == "__main__":
    main()
