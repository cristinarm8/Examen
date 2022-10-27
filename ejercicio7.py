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

    





    