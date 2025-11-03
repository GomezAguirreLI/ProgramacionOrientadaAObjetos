"""
Tkinter trabaja a traves de interfaces , es una biblioteca de pyhton que permite crear aplicaciones en python para escritorio

"""

#from tkinter import *

import tkinter as tk

ventana=tk.Tk()

ventana.title("Mi primer App grafica con Tkinter con Pyhton")
ventana.geometry("800x600")
ventana.resizable(False,False) #metodo para redimencionar el tamaño de la ventana

ventana.mainloop()#Metodo que permite tener la ventana abierta e interacturar con ela