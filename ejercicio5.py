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

print("Funcion recursiva:\n")

def encriptar_rec(mensaje_original, clave):
    if mensaje_original == "":
        return ""
    else:
        return chr(ord(mensaje_original[0] + clave)) + encriptar_rec(mensaje_original[1:], clave)

x = encriptar_rec("".join(caracteres, clave))
