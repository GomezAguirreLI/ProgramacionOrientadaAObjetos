from tkinter import *

ventana=Tk()

def mostrarSeleccion():
     resultado.config(text=f"Opción seleccioanda {opcion.get()}")






ventana.title("RadioButton")
ventana.geometry("800x600")


opcion=StringVar()


opcion1=Radiobutton(
    ventana,
    text="Opcion 1",
    variable="opcion",
    value="opcion1"
)
opcion1.pack()

opcion2=Radiobutton(
    ventana,
    text="Opcion 2",
    variable="opcion",
    value="opcion2"
)

opcion2.pack()

opcion3=Radiobutton(
    ventana,
    text="Opcion 3",
    variable="opcion",
    value="opcion3"
)
opcion3.pack()


boton=Button(
    text="Mostrar Seleccion",
    command=mostrarSeleccion
)
boton.pack()


resultado=Label(
    ventana,
    text=""
)
resultado.pack()





ventana.resizable(True,True) #metodo para redimensionar el tamaño de la ventana 
ventana.mainloop() # metodo que permite tenerla ventana abierta e interactuar con ella