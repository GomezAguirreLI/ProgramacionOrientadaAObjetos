from tkinter import *

ventana=Tk()
ventana.title("Frame")
ventana.geometry("800x600")


#Marco
marco=Frame(ventana,width=400,height=200,bg="grey",borderwidth=2,border=2,relief=SOLID)
marco.pack_propagate=(False)
marco.pack(pady=100)


marco2=Frame(marco,width=200,height=100,bg="red",relief=GROOVE).pack()

ventana.mainloop()