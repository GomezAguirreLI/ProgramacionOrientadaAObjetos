from coches import *

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

