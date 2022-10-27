lista = [18, 50, 210, 80,145,33,70,30]

numeros = [x for x in lista if x%10 == 0 and x < 200]
print(numeros)

def parar(lista):
    for i in lista:
        if i > 300:
            break
        else:
            print("Es un número menor de 300")
            break
parar(lista)

def ordenar_lista(lista):
    return lista.sort()
ordenar_lista(lista)
