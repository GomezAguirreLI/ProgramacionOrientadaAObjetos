class Fabrica:
    def __init__(self,color,precio):
        self._color=color
        self._precio=precio



class Moto(Fabrica):
    def __init__(self, color, precio,cant_llantas,precio_trans):
        self._cant=cant_llantas
        self._precio_trans=precio_trans

    def getAtributos(self):
            print(f"cantidad de llantas {self._cant} color{self._precio_trans} y precio {self._precio_trans} ")




class Carro(Fabrica):
    def __init__(self, color, precio,cant_llantas,precio_trans):
        self._cant=cant_llantas
        self._precio_trans=precio_trans

    def getAtributos(self):
            print(f"cantidad de llantas {self._cant} color{self._precio_trans} y precio {self._precio_trans} ")



c=Fabrica("negro","2")


mustang=Carro(4,60)


carcaaza=Fabrica("blanca",1000)

yasaki=Moto(2,400)


mustang.getAtributos()
yasaki.getAtributos()