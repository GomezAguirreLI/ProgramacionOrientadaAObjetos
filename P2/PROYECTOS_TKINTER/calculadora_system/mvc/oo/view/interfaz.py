from tkinter import messagebox
from tkinter import *
from controller import funciones
from model import operaciones
#Interfaz o view

class Vista:
    def __init__(self,ventana):
        ventana=Tk()
        ventana.title("Calculadora")
        ventana.geometry("600x400")
        ventana.resizable(False,False)
        self.interfaz_principal(ventana)
    @staticmethod
    def interfaz_principal(ventana):
        Vista.menuPrincipal(ventana)    
        
        ventana.title("Calculadora")
        ventana.geometry("600x400")
        ventana.resizable(False,False)

        #Variables para los entry
        n1=IntVar()
        n2=IntVar()

        txt_numero1=Entry(ventana,textvariable=n1,width=5,justify="right")
        txt_numero1.focus
        txt_numero1.pack(side="top",anchor="center")

        txt_numero2=Entry(ventana,textvariable=n2,width=5,justify="right")
        txt_numero2.pack(side="top",anchor="center")

        btn_suma=Button(ventana,text="+",command=lambda: funciones.Funciones.operaciones(n1.get(),n2.get(),"+"))
        btn_suma.pack()

        btn_resta=Button(ventana,text="-",command=lambda:funciones.Funciones.operaciones(n1.get(),n2.get(),"-"))
        btn_resta.pack()

        btn_multiplicacion=Button(ventana,text="X",command=lambda:funciones.Funciones.operaciones(n1.get(),n2.get(),"x"))
        btn_multiplicacion.pack()

        btn_division=Button(ventana,text="/",command=lambda:funciones.Funciones.operaciones(n1.get(),n2.get(),"/"))
        btn_division.pack()


        btn_salir=Button(ventana,text="Salir",command=ventana.quit)
        btn_salir.pack()
        ventana.mainloop()
 
   


    @staticmethod
    def menuPrincipal(ventana):
        menuBar=Menu(ventana)
        ventana.config(menu=menuBar)

        operacionesMenu=Menu(menuBar,tearoff=False)
        menuBar.add_cascade(label='Operaciones',menu=operacionesMenu)
        operacionesMenu.add_command(label='Agregar',command=lambda:"")
        operacionesMenu.add_command(label='Consultar',command=lambda:Vista.listado_screen(ventana))
        operacionesMenu.add_command(label='Cambiar',command=lambda:"")
        operacionesMenu.add_command(label='Borrar',command=lambda:Vista.eliminar_screen(ventana))
        operacionesMenu.add_separator()
        operacionesMenu.add_command(label="Salir",command=ventana.quit)

    @staticmethod
    def eliminar_screen(ventana):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)
        lbl_titulo=Label(ventana,text=f".:: Borrar una operacion ::.")
        lbl_titulo.pack(pady=10)
        lbl_id=Label(ventana,text="ID de la Operacion: ")
        lbl_id.pack(pady=5)
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify="right",width=5)
        txt_id.focus()
        txt_id.pack(pady=5)


        btn_eliminar=Button(ventana,text="Eliminar",command=lambda:funciones.Funciones.borrar(id.get()))
        btn_eliminar.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=Vista.interfaz_principal(ventana))
        btn_volver.pack(pady=5)
    @staticmethod
    def listado_screen(ventana):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)
        lbl_titulo=Label(ventana,text=f".:: Listado de las oepraciones ::.")
        lbl_titulo.pack(pady=10)

        filas=""
        registros=operaciones.Operaciones.consultar()
        
        if len(registros)>0:
            num_operacion=1
            for fila in registros:
                fila=filas+(f"\nOperacion:{num_operacion} ID{fila[0]} Fecha de Creación {fila[1]} Operacion {fila[2]}{fila[4]}{fila[3]}{fila[5]}")
        else:
            messagebox.showinfo(message="No existen operaciones disponibles")

        lbl_listado=Label(ventana,text="")
        lbl_listado.pack(pady=10) 

        btn_volver=Button(ventana,text=f"Volver",command=lambda:Vista.interfaz_principal(ventana))
        btn_volver.pack(pady=5) 
    #--------------------
    #Actualizar pantalla |
    #--------------------
    def cambiar(ventana):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)


        lbl_titulo=Label(ventana, text=f".:: Cambiar una operación ::..")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la Operación: ")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify="right",width=5)
        txt_id.pack(pady=5)


        Label(ventana,text="Nuevo Número 1: ").pack(pady=5)
        n1=IntVar()
        numero1=Entry(ventana,textvariable=n1,justify="right",width=5)
        numero1.pack(pady=5)

        Label(ventana,text="Nuevo Número 2: ").pack(pady=5)
        n2=IntVar()
        numero2=Entry(ventana,textvariable=n2,justify="right",width=5)
        numero2.pack(pady=5)
    
        Label(ventana,text="Nuevo SIGNO: ").pack(pady=5)
        sig=StringVar()
        txt_signo=Entry(ventana,textvariable=sig,justify="right",width=5)
        txt_signo.pack(pady=5)


        Label(ventana,text="Nuevo Resultado: ").pack(pady=5)
        result=DoubleVar()
        txt_resultado=Entry(ventana,textvariable=result,justify="right",width=5)
        txt_resultado.pack(5)
        Button(ventana, text="Guardar",command=lambda: funciones.Funciones.actualizar(n1.get(),n2.get(),sig.get(),id.get())).pack(pady=5)
        
            
    #Borrar pantalla
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
    