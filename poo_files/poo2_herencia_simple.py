# Author: Efrain Noa
# email: enoay7@yahoo.com; noayarae@oregonstate.edu
# Programacion Orientada a objetos
# Creacion de Herencias

# Code developed based on video 29 "curso python" from https://www.youtube.com/watch?v=u_VbLsIyzRk&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=29
# and video 30 "curso python" from: https://www.youtube.com/watch?v=jMQQN9OxwVc&index=30&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS
# and first part of video 31

class vehiculos():
    def __init__(self, marca, modelo): #Constructor
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    #Metodos (Comportamientos)
    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\n En Marcha: ",
               self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)

class furgoneta(vehiculos): #Subclase
    def carga(self, carga):
        self.cargado = carga
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "LA furgoneta no esta cargada"

class moto(vehiculos): #Subclase - recibe herencia de clase vehiculos
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo caballito"

    def estado(self):
        print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\n En Marcha: ",
               self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ",
               self.frena, "\n", self.hcaballito)

class ve_electricos(): #subclase
    def __init__(self): #Constructor
        self.autonomia = 100
    def cargar_energia(self): #Metodo
        self.cargando = True
    

mi_moto = moto("Honda","CR1100") # objeto o instancia
mi_moto.caballito() #assign tex-value to "hcaballito"
mi_moto.estado() # ask for printing
print ()

mi_furgoneta = furgoneta("Renault", "Kangoo") # Objeto o instancia
mi_furgoneta.arrancar()
mi_furgoneta.estado()
print (mi_furgoneta.carga(True))


class bici_electrica(vehiculos, ve_electricos): #subclase heredando de 2 clases
    pass

mi_bici = bici_electrica("orbea", "FD200")

