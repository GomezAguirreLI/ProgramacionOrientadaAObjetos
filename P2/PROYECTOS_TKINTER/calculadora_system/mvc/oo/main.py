'''
Crear una calculador:
1.- Dos campos de texto
2.- 4 botones para las operaciones
3.- Mostrar el resultado en una alerta
4._Programado de forma oo
5.-Considerar el MVC
'''


from tkinter import *
from view import interfaz
class App:
    def __init__(self,ventana):
        view=interfaz.Vista(ventana)
        

#def main():
    #interfaz.interfaz_principal()


if __name__=="__main__":
    ventana=Tk
    app=App(ventana)
    ventana.mainloop()    

