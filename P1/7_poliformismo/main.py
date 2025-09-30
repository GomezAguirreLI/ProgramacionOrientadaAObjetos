from coches import *


'''

coche1=Coches("BMW","Blanco","2024","250","300","4")
coche2=Coches("Susuki","Red","2020","200","200","2")
coche3=Coches("Honda","",0,0,0,0)
coche4=Coches("","",0,0,0,0,)
coche4.marca2="VOLVO"
print(coche4.marca2)
print(coche4.marca2)

'''


#coche1.marca="VW"
#coche1.color="Blanco"
#coche1.modelo="2022"
#coche1.velocidad=220
#coche1.caballaje=150
#coche1.plazas=5


num_coches=int(input("¿Cuantos vehicuos va a comprar? "))

for i in range(0,num_coches):

    print(f"..:::Datos del Vehiculo #{i+1}:::..")

    marca=input("Ingresar la marca del auto: ").upper()
    color=input("Ingresa el color del auto:   ").upper()
    modelo=input("Ingresa el modelo: ").upper()
    velocidad=int(input("Ingresa la velocidad: "))
    potencia=int(input("Cual es la potencia: "))
    plazas=int(input("Ingresa el # de plazas"))

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)



    print(f"\n\t Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlaza()} ")

    #print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlaza()} ")
