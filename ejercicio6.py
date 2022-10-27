# Creación de una matriz

def estructurar_matriz(filas, columnas):
    #Creamos una matriz nueva
    matriz = [None] * filas
    # Bucle for que recorra las filas.
    for i in range(filas):
        # Creación columnas
        matriz[i] = [None] * columnas
    return matriz