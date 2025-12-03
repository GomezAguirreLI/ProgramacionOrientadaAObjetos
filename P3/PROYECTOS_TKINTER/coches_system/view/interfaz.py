from tkinter import *
from tkinter import messagebox

class View:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.title("..: Coches System :..")
        ventana.geometry("800x700")
        ventana.resizable(False,False)
        self.menu_principal(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
    @staticmethod
    def menu_principal(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menú Principal ::..",justify="center")
        lbl_titulo.pack(pady=10)
        btn_registro=Button(ventana,text="1.- Autos",justify="center",command=lambda: View.menu_autos(ventana))
        btn_registro.pack(pady=15)
        btn_login=Button(ventana,text="2.- Camionetas",justify="center", command=lambda: View.menu_camionetas(ventana))
        btn_login.pack(pady=15)
        btn_login=Button(ventana,text="3.- Camiones",justify="center", command=lambda: View.menu_camiones(ventana))
        btn_login.pack(pady=15)
        btn_salir=Button(ventana,text="4.- Salir",justify="center",command=ventana.quit)
        btn_salir.pack(pady=15)
    
    @staticmethod
    def menu_autos(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menú Autos ::..",justify="center")
        lbl_titulo.pack(pady=15)
        btn_registro=Button(ventana,text="1.- Insertar",justify="center",command=lambda: View.auto_registro(ventana))
        btn_registro.pack(pady=10)
        btn_login=Button(ventana,text="2.- Consultar",justify="center", command=lambda: ""(ventana))
        btn_login.pack(pady=10)
        btn_salir=Button(ventana,text="3.- Actualizar",justify="center",command=lambda: ""(ventana))
        btn_salir.pack(pady=10)
        btn_salir=Button(ventana,text="4.- Eliminar",justify="center",command=lambda:""(ventana))
        btn_salir.pack(pady=10)
        btn_volver=Button(ventana,text="5.- Regresar",command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=10)
    
    @staticmethod
    def menu_camionetas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menú Camionetas ::..",justify="center")
        lbl_titulo.pack(pady=15)
        btn_registro=Button(ventana,text="1.- Insertar",justify="center",command=lambda: ""(ventana))
        btn_registro.pack(pady=10)
        btn_login=Button(ventana,text="2.- Consultar",justify="center", command=lambda: ""(ventana))
        btn_login.pack(pady=10)
        btn_salir=Button(ventana,text="3.- Actualizar",justify="center",command=lambda: ""(ventana))
        btn_salir.pack(pady=10)
        btn_salir=Button(ventana,text="4.- Eliminar",justify="center",command=lambda:""(ventana))
        btn_salir.pack(pady=10)
        btn_volver=Button(ventana,text="5.- Regresar",command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def menu_camiones(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menú Camiones ::..",justify="center")
        lbl_titulo.pack(pady=15)
        btn_registro=Button(ventana,text="1.- Insertar",justify="center",command=lambda: ""(ventana))
        btn_registro.pack(pady=10)
        btn_login=Button(ventana,text="2.- Consultar",justify="center", command=lambda: ""(ventana))
        btn_login.pack(pady=10)
        btn_salir=Button(ventana,text="3.- Actualizar",justify="center",command=lambda: ""(ventana))
        btn_salir.pack(pady=10)
        btn_salir=Button(ventana,text="4.- Eliminar",justify="center",command=lambda:""(ventana))
        btn_salir.pack(pady=10)
        btn_volver=Button(ventana,text="5.- Regresar",command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def auto_registro(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="...: Registro de Autos :...", justify="center")
        lbl_titulo.pack(pady=15)

        lbl_marca=Label(ventana,text="Marca: ",justify="center")
        lbl_marca.pack(pady=10)
        txt_marca=Entry(ventana)
        txt_marca.pack(pady=10)
        txt_marca.focus()
        
        lbl_color=Label(ventana,text="Color: ",justify="center")
        lbl_color.pack(pady=10)
        txt_color=Entry(ventana)
        txt_color.pack(pady=10)
        
        lbl_modelo=Label(ventana,text="Modelo: ",justify="center")
        lbl_modelo.pack(pady=10)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=10)
        
        lbl_velocidad=Label(ventana,text="Velocidad: ",justify="center")
        lbl_velocidad.pack(pady=10)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=10)

        lbl_potencia=Label(ventana,text="Potencia: ",justify="center")
        lbl_potencia.pack(pady=10)
        txt_potencia=Entry(ventana)
        txt_potencia.pack(pady=10)

        lbl_nro_plazas=Label(ventana,text="Numero de Plazas: ",justify="center")
        lbl_nro_plazas.pack(pady=10)
        txt_nro_plazas=Entry(ventana)
        txt_nro_plazas.pack(pady=10)

        btn_guardar=Button(ventana,text="Guardar", command=lambda: [messagebox.showinfo("Guardar", "Auto registrado correctamente"), View.menu_autos(ventana)])
        btn_guardar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_autos(ventana))
        btn_volver.pack(pady=10)
