from tkinter import *
ventana=Tk()

def mostrarEstado():
    if opcion.get()==1:
        resultado.config(text=f"Notificaciones Activadas")
    else:
        resultado.config(text=f"Notificaciones Desactivadas")

ventana.title("CheckButton")
ventana.geometry("500x600")
ventana.resizable(True,True) #metodo para redimensionar el tamaño de la ventana 

#Es como si fuera un click listener
opcion=IntVar()

Checkbton=Checkbutton(
    ventana,
    text="¿Deseas recibir notificaciones?",
    variable=opcion,
    onvalue=1,
    offvalue=0
)
#Dibujarlo en el la ventana
Checkbton.pack()

boton=Button(
    ventana,
    text="Confirmar",
    command=mostrarEstado,
    
)
boton.pack()


resultado=Label(
    ventana,
    text=""
)




resultado.pack()


ventana.mainloop() # metodo que permite tenerla ventana abierta e interactuar con ella pero va al final
