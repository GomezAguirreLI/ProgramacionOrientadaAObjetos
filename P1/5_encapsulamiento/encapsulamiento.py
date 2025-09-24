class Clase:
    atributo_publico="Soy un atributo publico"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"


    def __init__(self,color,tamanio):
        self.__color=color
        self.__tamanio=tamanio

    def __getAtributoPrivado(self):
        return self.__atributo_privado
    
    def getAtibutoPrivado2(self):
        self.__getAtibutoPrivado()
    
    def setAtributoPrivado(self,atributo_privado):
        self.__atributo_privado=atributo_privado
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color=color

    @property
    def tamano(self):
        return self.__tamanio
    
    @tamano.setter
    def tamano(self,tamano):
        self.__tamano=tamano
#Usar los atributos y Metodos de acuerdo a encaspulamiento

objeto=Clase("Rojo","Grande") 

print(f"Mi objeto tiene los siguientes atributos {objeto.color} y {objeto.tamano}")

print(f"Soy el contenido del atributo publico: {objeto.atributo_publico}")
print(f"Soy el contenido del atributo protegido : {objeto._atributo_protegido}")
print(f"Soy el contenido del atributo privado : {objeto.getAtributoPrivado()}")

objeto.setAtributoPrivado("Cambie el contenido del atributo privado")
print(f"Soy el contenido del atributo privado : {objeto.getAtributoPrivado()}")

