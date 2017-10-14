# Author: Efrain Noa
# email: enoay7@yahoo.com; noayarae@oregonstate.edu
# Programacion Orientada a objetos
# Creacion de Herencias - superclases

# Code developed based on video 31 "curso python" from https://www.youtube.com/watch?v=oe04X1B14YY&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=31

class persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
       print("nombre: ", self.nombre, "cEdad: ", self.edad,
             " Residencia: ", self.residencia)

class empleado(persona):
    def __init__(self, salario, antiguedad):
        self.salario = salario
        self.antiguedad = antiguedad

antonio = persona("Antonio", 55, "Espana")
antonio.descripcion()

antonio = empleado(1500, 5)
