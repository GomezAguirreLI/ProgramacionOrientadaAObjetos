from tkinter import *


def mostrarValor():
    resultado.config(text=f"Valor seleccionado por el usuario: {valor.get()}")



ventana=Tk()



ventana.title("Scale")
ventana.geometry("500x500")

valor=IntVar()
escala=Scale(
    ventana,
    from_=0,
    to=100,
    orient=HORIZONTAL,
    variable=valor
)
escala.pack()


boton=Button(
    ventana,
    text="Mostrar valor",
    command=mostrarValor
)
boton.pack()

resultado=Label(
    ventana,
    text=""
)
resultado.pack()

ventana.resizable(True,True) #metodo para redimensionar el tamaño de la ventana 
ventana.mainloop() # metodo que permite tenerla ventana abierta e interactuar con ella