# Encriptar y desencriptar:

clave = 10

# Bucle que recorre del 32 al (126-1) y tranforma cada nº en un caracter con chr()
caracteres = [chr(i) for i in range(32,126)]

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
    for x in caracteres:
        mensaje_encriptado += chr(ord(x)-clave)
    return mensaje_encriptado
w = desencriptar(x, clave)

