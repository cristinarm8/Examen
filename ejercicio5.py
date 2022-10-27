# Encriptar y desencriptar:

clave = 10

# Bucle que recorre del 32 al (126-1) y tranforma cada nº en un caracter con chr()
caracteres = [chr(i) for i in range(32,126)]

print("\nFunción iterativa: \n")
# Funcion encriptar:
def encriptar(caracteres, clave):
    mensaje_encriptado = ""
    for x in caracteres:
        # Transformamos cada valor que recorre el bucle (x) en un ordinal para que pueda sumarse con la clave que es un nº:
        mensaje_encriptado += chr(ord(x) + clave)
        # Después, todo ello lo convertimos en un chr.
    return mensaje_encriptado

x = encriptar(caracteres, clave)
print(f"Encriptar mensaje: {x}")

def desencriptar(x, clave):
    #En este caso la clave será negativa para -> desencriptar el mensaje.
  return encriptar(x, - clave)

w = desencriptar(x, clave)
print(f"Desencriptar mensaje: {w}")

print("\n***************************************************************************************************************\n")
print("Funcion recursiva:\n")

def encriptar_rec(mensaje_original, clave):
    if mensaje_original == "":
        return ""
    else:
        # Transformamos el primer valor del mansaje [0] en un ordinal para que pueda seumarse con la clave y lo transformamos en un chr()
        return chr(ord(mensaje_original[0]) + clave) + encriptar_rec(mensaje_original[1:], clave)

x = encriptar_rec("".join(caracteres), clave)
print(f"Encriptar en forma recursiva: {x}")

def desencriptar_rec(mensaje_encriptado, clave):

    if mensaje_encriptado == "":
        return ""
    else:
        return chr(ord(mensaje_encriptado[0]) - clave) + desencriptar_rec(mensaje_encriptado[1:], clave) 
w = desencriptar_rec(x, clave)
print(f"Desencriptar en forma recursiva: {w}")

