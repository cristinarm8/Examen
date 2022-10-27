# Creación clase Alumno:
class Alumno():

    # Método constructor:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno se ha creado con éxito")

    def calificacion(self):

        if self.nota >= 5:
            print("{} ha aprobado el examen con un {} de nota".format(self.nombre, self.nota))
        else:
            print("{} ha suspendido el examen con un {} de nota".format(self.nombre, self.nota))
    
    # Creación objetos:
alumno1 = Alumno("Laura", 9)
