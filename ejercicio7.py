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





    