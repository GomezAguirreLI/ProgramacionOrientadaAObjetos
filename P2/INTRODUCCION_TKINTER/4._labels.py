from tkinter import *

ventana=Tk()
ventana.title("Etiquetas")
ventana.geometry("800x600")

#Etiqueta o Label

etiqueta1=Label(ventana, text="Nombre de la Persona").pack()

marco1=Frame(ventana, bg="gold", width=200, height=100).pack()
marco2=Frame(marco1, bg="silver", width=200, height=100).pack()
etiqueta2=Label(marco1, text="Soy una etiqueta dentro de un marco").pack()

ventana.mainloop()