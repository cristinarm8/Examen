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






    