# Author: Efrain Noa
# Programacion Orientada a objetos
# Creacion de classes, constructor, metodos, objetos (instancias)

# Code developed based on video 26 "curso python" from https://www.youtube.com/watch?v=Y_SiIgxc-xI&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=26
# and video 27 from https://www.youtube.com/watch?v=x5CY8fVyYLo&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=27
# and video 28

class coche:
    def __init__(self): #CONSTRUCTOR
        
        self.largo = 200
        self.ancho = 500
        self.__ruedas = 4 #Encapsular (accesible desde la misma clase, no desde afuera)
        self.__enmarcha = False

    def arranca(self, arrancamos): #METODO
        self.__enmarcha = arrancamos

        if (self.__enmarcha):
            chequeo = self.__chequeo_interno()
            
        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en chequeo, no podemos arrancar"
        else:
            return "El coche esta parado"

    def estado(self): #METODO
        print ("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.ancho,
               " y un largo de ", self.largo)

    def __chequeo_interno(self):
        print ("realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "mal"
        self.puertas = "cerradas"

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False

# Objeto 1
mi_coche = coche() #OBJETO o INSTANCIA

print (mi_coche.arranca(True)) #LLAMA UN COMPORTAMIENTO

mi_coche.estado() #LLAMA UN COMPORTAMIENTO

print ("---- A continuacion creamos otro coche -----")

# Objeto 2
mi_coche_2 = coche() #OBJETO O INSTANCIA

print (mi_coche_2.arranca(False))

mi_coche_2.estado() #LLAMA UN COMPORTAMIENTO
