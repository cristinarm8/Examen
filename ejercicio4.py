# Creación clase Alumno:
class Alumno():

    # Método constructor:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("\nEl alumno se ha creado con éxito\n")
    
    def __str__(self):
        return "Nombre: {}\nNota: {}".format(self.nombre, self.nota)

    def calificacion(self):

        if self.nota >= 5:
            print("{} ha aprobado el examen con un {} de nota\n".format(self.nombre, self.nota))
        else:
            print("{} ha suspendido el examen con un {} de nota\n".format(self.nombre, self.nota))

# Creación objeto:
alumno1 = Alumno("Laura", 9)
print(alumno1)

# Método calificación
alumno1.calificacion()

# Creación objeto:
alumno2 = Alumno("Álvaro", 4)
print(alumno2)
alumno2.calificacion()
