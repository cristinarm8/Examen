# Creación de una matriz
def estructurar_matriz(filas, columnas):
    #Creamos una matriz nueva
    matriz = [None] * filas
    # Bucle for que recorra las filas.
    for i in range(filas):
        # Creación columnas
        matriz[i] = [None] * columnas
    return matriz


def rellenar(fila, columna):
    matriz = estructurar_matriz(5,5)
    for i in range(fila):
        for j in range(columna):
            matriz[i][j] = int(input("Valor Fila {}, Valor Columna {}:".format(i+1, j+1)))
    print("\n".join([str(l) for l in matriz]))

    return matriz

# Calcular determinante:
def calculo_determinante(a):
    determinante = ((a[0][0] * a[1][1]* a[2][2]) + (a[0][1] * a[1][2] * a[2][0])  + (a[0][2] * a[1][0] * a[2][1] )) - ((a[2][0]* a[1][1] * a[0][2]) + (a[2][1] * a[1][2] * a[0][0]) + (a[2][2] * a[1][0] * a[0][1]))
    return determinante

print("\nEstructura de la matriz: \n")
relleno_matriz = rellenar(5,5)

print("Determiante de la matriz de imension 5x5 por el método de Sarrus: \n")
print(f"Valor obtenido: {calculo_determinante(relleno_matriz)}")
'''
def agregar_elementos_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        for j in range(columnas):
            valor = float(input("Valor Fila {}, Valor Columna: {}".format(i+1, j+1)))
            matriz[i].append(valor)
    return matriz
'''
#estructurar_matriz(3,3)
#agregar_elementos_matriz(3,3)
         