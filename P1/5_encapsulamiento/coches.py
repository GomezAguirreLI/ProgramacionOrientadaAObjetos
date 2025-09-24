import os
os.system("cls")

class Coches:


   #Metodo constructor
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
      self.marca=marca
      self.color=color
      self.modelo=modelo
      self.velocidad=velocidad
      self.caballaje=caballaje
      self.plazas=plazas

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
       return self.marca
    
    def setModelo(self,modelo):
       self.marca=modelo

    def getVelocidad(self):
       return self.marca
    
    def setVelocidad(self,velocidad):
       self.marca=velocidad

    def getCaballaje(self):
       return self.marca
    
    def setCaballaje(self,caballaje):
       self.marca=caballaje
    
    
    def getPlaza(self):
       return self.marca
    
    def setPlaza(self,plaza):
       self.marca=plaza








    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase



coche1=Coches("BMW","Blanco","2024","250","300","4")
coche2=Coches("Susuki","Red","2020","200","200","2")
coche3=Coches("Honda","",0,0,0,0)
coche4=Coches("","",0,0,0,0,)
coche4.marca2="VOLVO"
print(coche4.marca2)
print(coche4.marca2)


#coche1.marca="VW"
#coche1.color="Blanco"
#coche1.modelo="2022"
#coche1.velocidad=220
#coche1.caballaje=150
#coche1.plazas=5


print(coche3.marca2)


print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlaza()}\n Numero de serie {coche1.num_serie} ")



print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlaza()} ")



