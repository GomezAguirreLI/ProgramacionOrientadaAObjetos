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

import os

os.system("cls")
#coche1.marca="VW"
#coche1.color="Blanco"
#coche1.modelo="2022"
#coche1.velocidad=220
#coche1.caballaje=150
#coche1.plazas=5




def autos():
    
    print(f"..:::Datos del Vehiculo :::..")

    marca=input("Ingresar la marca del auto: ").upper()
    color=input("Ingresa el color del auto:   ").upper()
    modelo=input("Ingresa el modelo: ").upper()
    velocidad=int(input("Ingresa la velocidad: "))
    potencia=int(input("Cual es la potencia: "))
    plazas=int(input("Ingresa el # de plazas"))

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)



    print(f"\n\t Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlaza()} ")



def camionetas():
    
    print(f"..:::Datos del Vehiculo :::..")

    marca=input("Ingresar la marca del auto: ").upper()
    color=input("Ingresa el color del auto:   ").upper()
    modelo=input("Ingresa el modelo: ").upper()
    velocidad=int(input("Ingresa la velocidad: "))
    potencia=int(input("Cual es la potencia: "))
    plazas=int(input("Ingresa el # de plazas"))

    traccion=input("Ingrese el tipo de traccion").upper()
    cerrada=input("Ingresar SI/NO si es cerrada o no").upper().strip()

    if cerrada=="SI":
        cerrada=True

    else:
        cerrada=False   

    coche1=Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)



    print(f"\n\t Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlaza()}\n\t  {coche1.traccion}\n\t {coche1.cerrada}  ")

    #print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlaza()} ")

def camiones():
    
    print(f"..:::Datos del Vehiculo :::..")

    marca=input("Ingresar la marca del auto: ").upper()
    color=input("Ingresa el color del auto:   ").upper()
    modelo=input("Ingresa el modelo: ").upper()
    velocidad=int(input("Ingresa la velocidad: "))
    potencia=int(input("Cual es la potencia: "))
    plazas=int(input("Ingresa el # de plazas"))

    eje=int(input("Ingrese el valor del eje").upper())
    capacidadCarga=int(input("Ingresar la capacidad de carga"))

    

    coche1=Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)



    print(f"\n\t Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlaza()}\n\t  {coche1.eje}\n\t{coche1.capacidadCarga}")

    #print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlaza()} ")




opcion=1
while opcion!=4:
    os.system("cls")
    opcion=input("\n\t..::Menu principal::.\n\t1.-Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\Elige una opcion").lower().strip()
    match opcion:
        case "1":
            autos()

        case "2":
            print("Camionetas")
            input("Oprima tecla para continuar")
        case "3":
            print("camiones")
            input("Oprima tecla para continuar")

        case "4":
            print("Salir del sistema")
            input("Oprima cualquier tecla para continuar")    

        case _:
            input("Opcion invalida...vuelva a interntarlo")



