class Nodo:
    info, sig = None, None

class datoPolinomio(object):
    """Clase dato Polinomio"""

    # Atributos valor y término del polinomio.
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class Polinomio(object):
    """Clase polinomio"""

    # Método constructor
    def __init__(self):
        # Crea un polinomio del grado cero
        # Puntero que apunta al término amyor del polinomio.
        self.termino_mayor = None
        # Grado del polinomio.
        self.grado = -1
    
    def __str__(self):
        resultado = "Polinomio"
        next = self.termino_mayor
        while(next.sig is not None):
            resultado += (str(next.info.valor) + "x^" + str(next.info.termino) + " + ")
            next = next.sig 
        resultado += (str(next.info.valor) + "x^" + str(next.info.termino))
        return resultado 

def agregar_termino(polinomio, termino, valor):
    """ Agrega un término y su valor al polinomio"""
    # Variable que va a almacenar la clase Nodo
    aux = Nodo()
    # Variable que almacena clase datoPolinomio
    dato = datoPolinomio(valor, termino)
    # Variable que va a almacenar el dato(aux.info): campo de información del Nodo.
    aux.info = dato

    # si el término es mayor que el grado del polinomio:
    if (termino > polinomio.grado):
        # Variable aux.sig (campo de enlace) almacenará el puntero que apunta al término mayor del polinomip.
        aux.sig = polinomio.termino_mayor
        # Ese puntero almacena variable aux que contiene al Nodo.
        polinomio.termino_mayor = aux
        # Atributo gradoo de la clase polinomio almacenas el termino que le has pasado como parámetro a la función:
        polinomio.grado = termino

    # Si el término es menor que el grado del polinomio.
    else:
        actual = polinomio.termino_mayor
        # Mientras que el puntero que apunta al nodo siguiente no sea None y el término sea menor al término del nodo siguiente.
        while(actual.sig is not None and termino  < actual.sig.info.termino):

            actual = actual.sig

        if actual.info.termino == termino:
            actual.info.avlor = valor
            return

        # Salimos del bucle
        aux.sig = actual.sig
        actual.sig = aux

def eliminar_termino1(polinomio, termino):

    aux = polinomio.termino_mayor
    next = aux.sig
    
    if aux.info.termino == termino:
        polinomio.termino_mayor = aux.sig
        return
    while(next is not None and next.info.termino != termino):
        # Variable aux va a almacenar puntero que apunta hacia el siguiente nodo.
        net = next.sig
        aux = aux.sig

    # Si aux que almacena puntero del siguiente nodo no es None y el término de ese nodo es igual al término.
    if (next is not None and next.info.termino != termino):
        aux.sig = next.sig
    else:
        print("Término no encontrado")

    
def restar(polinomio1, polinomio2):

    polinomio_resultado = Polinomio()

    next1 = polinomio1.termino_mayor
    next2 = polinomio2.termino_mayor

    while(next1 is not None):

        while(next2 is not None and next2.info.termino > next1.info.termino):
            agregar_termino(polinomio_resultado, next2.info.termino, next2.info.valor)
            print("Agregado término next2", next2.info.termino, next2.info.valor)
            next2 = next2.sig

        if next2 is not None and next2.info.termino == next1.info.termino:
            agregar_termino(polinomio_resultado,next2.info.termino, next1.info.valor - next2.info.valor)
            print("Resultado términos")
            next2 = next2.sig
        else:
            agregar_termino(polinomio_resultado, next1.info.termino, next1.info.valor)
            print("Agregado término next1", next1.info.termino, next1.info.valor)
        next1 = next1.sig
    return polinomio_resultado

polinomio1 = Polinomio()
polinomio2 = Polinomio()

agregar_termino(polinomio1, 10,3)
agregar_termino(polinomio1, 7,7)
agregar_termino(polinomio1, 9,5)
agregar_termino(polinomio1, 4, 5)

agregar_termino(polinomio2, 7,6)
agregar_termino(polinomio2, 8,5)
agregar_termino(polinomio2, 8,8)
agregar_termino(polinomio2, 4, 9)

print(polinomio1)
print(polinomio2)
'''
print("Eliminamos término")
eliminar_termino1(polinomio1, 10)
print(f"Eliminar: ", polinomio1)
'''
print("Restar:")
resta = restar(polinomio1, polinomio2)
print(resta)