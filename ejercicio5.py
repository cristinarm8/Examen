# Encriptar y desencriptar:

clave = 10

# Bucle que recorre del 32 al (126-1) y tranforma cada nº en un caracter con chr()
caracteres = [chr(i) for i in range(32,126)]

# Funcion encriptar:
def encriptar(caracteres, clave):
    mensaje_encriptado = ""
    for x in caracteres:
        

