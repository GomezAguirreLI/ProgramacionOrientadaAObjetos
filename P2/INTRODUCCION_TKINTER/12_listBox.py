from tkinter import *

def mostrarSeleccion():
    valor=lista.get(lista.curselection())
    resultado.config(text=f"el resultado seleccionado es {valor} ")

ventana=Tk()
ventana.title("ListBox")
ventana.geometry("800x600")

lista=Listbox(
    ventana,
    width=50,
    height=5,
    selectmode='single'
)
lista.pack()

opciones=["Azul","Rojo","Negro","Amarrilo"]

for i in opciones:
    lista.insert(END,i)


boton=Button(
    ventana,
    text="Mostrar seleccion del usuario",
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