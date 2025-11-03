class Vehiculos:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo


    def info(self):
        return f"{self.marca} {self.modelo}" 


class Coche(Vehiculos):
    def __init__(self, marca, modelo,num_puertas):
        #de la clase vehiculos 
        super().__init__(marca, modelo)
        self.num_puertas=num_puertas


    def info(self):
        base=super().info()
        return f"{base} - {self.num_puertas}" 



c=Coche("Ford","Mustang shelby",2)
print(f" El coche es un {c.info()}")


class Moto(Vehiculos):
    def __init__(self, marca, modelo,tipo):
        super().__init__(marca, modelo)
        self.tipo=tipo

    def info(self):
        return f"{self.marca} {self.modelo}-{self.tipo}"    
    

moto=Moto("Yahama","NINJA","Deportiva")    

print(moto.info())


class Electricos:
    def __init__(self,bateria_km):
        self.bateria_km=bateria_km


    def info_bateria(self):
        return f"Bateria de una autonomia de {self.bateria_km} kilometros"    
    

class Autonomos:
    def __init__(self,crucero):
        self.crucero=crucero

    def info_autonomo(self):
        return f"El modo de crucero del carro autonomo es {self.crucero} "


class CocheElecrtico(Electricos,Coche):
    def __init__(self,marca,modelo,num_puertas,bateria_km):
        Coche.__init__(self,marca,modelo,num_puertas)
        Electricos.__init__(self,bateria_km)

    def info(self):
        return f"Esta es la info del carro {Coche.info(self)} y esta es la de la bateria {self.info_bateria()}"



print(CocheElecrtico.mro())      