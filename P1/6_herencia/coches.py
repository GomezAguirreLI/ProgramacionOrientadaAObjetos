import os
os.system("cls")

class Coches:


   #Metodo constructor
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
      self.__marca=marca
      self.__color=color
      self.__modelo=modelo
      self.__velocidad=velocidad
      self.__caballaje=caballaje
      self.__plazas=plazas

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
   
    #Crear los metodos setters y getters, estos metodos son importantes y necesarios en todas las clases para el que programador interactue con los valores de los atributos a traves de estos metodos digamos que es la manera mas adecuada y recomendada para solicitar un valor get y o para ingresar  o cambiar un valir set a un atributo en particular de la case de un objeto.


    #En teoria  se deberia crear un método Getters y Setters por casa atributo que contenga la clase

    #Los metodos get siempre regresan el valor es decir el valor de la propiedad a traves del return por el otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion



    #Metodos o acciones o funciones que hace el objeto 
    #1 primer forma de hacerlo
    def getMarca(self):
       return self.marca
    
    def setMarca(self,marca):
       self.marca=marca


    #Segunda forma de hacerlo
    @property
    def marca2(self):
       return self.marca

    @marca2.setter

    def marca2(self,marca):
       self.marca=marca
    



    def getColor(self):
       return self.color
    
    def setColor(self,color):
       self.color=color

    def getModelo(self):
       return self.__modelo
    
    def setModelo(self,modelo):
       self.marca=modelo

    def getVelocidad(self):
       return self.__velocidad
    
    def setVelocidad(self,velocidad):
       self.__velocidad=velocidad

    def getCaballaje(self):
       return self.__caballaje
    
    def setCaballaje(self,caballaje):
       self.__caballaje=caballaje
    
    
    def getPlaza(self):
       return self.plazas
    
    def setPlaza(self,plaza):
       self.__plazas=plaza








    def acelerar(self):
      return "Estas acelerando"

    def frenar(self):
      return "Estas frenando"  

#Fin definir clase

#Crear un objetos o instanciar la clase




