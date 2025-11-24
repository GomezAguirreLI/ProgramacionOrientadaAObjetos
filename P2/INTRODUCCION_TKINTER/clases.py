import math

class Figuras:
    def __init__(self,x,y,visible):
        self.x=x
        self.y=y
        self.visible=visible

    def get_x(self):
        return self.x
    
    def set_x(self,x):
        self.x=x

    
    def get_y(self):
        return self.y
    
    def set_y(self,y):
        self.y=y

    def estaVisible(self):
        return self.estaVisible
    
    def mostrar(self):
        return f"Mostrando figura"
    
    def ocultar(self):
        return f"Ocultando figura"
    
    def mover(self,x,y):
        return f"Moviendo figura a {x} y a {y}"
    
    def calcularArea(self):
        return f"{self.get_x*self.get_y}"
    

class circulos(Figuras):
    def __init__(self,x,y,visible,radio):
        super().__init__(x,y,visible)
        self.__radio=radio

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self,radio):
        self.__radio=radio

    def calcularArea(self,radio):
        return f" El area del cirulo es {math.pi*(radio*radio)}"        
    

class Rectangulos(Figuras):
    def __init__(self,x,y,visible,alto,ancho):
        super().__init__(x,y,visible)
        self.__alto=alto
        self.__ancho=ancho

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self,alto):
        self.__alto=alto

    
    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self,ancho):
        self.__ancho=ancho


    def calcularArea(self,alto,ancho):
         return f"el area es {alto*ancho}"       




      
