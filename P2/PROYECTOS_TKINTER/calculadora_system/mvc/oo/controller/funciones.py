from tkinter import messagebox
from model import operaciones
class Funciones:
    @staticmethod
    def operaciones(n1,n2,signo):
        if signo=="+":
            ope=n1+n2
            tipo_ope="Suma"
        elif signo=="-":
            ope=n1-n2
            tipo_ope="Resta"
        elif signo=="x":
            ope=n1*n2
            tipo_ope="Multiplicacion"  
        elif signo=="/":
            ope=n1/n2
            tipo_ope="Divsion"

        resultado=messagebox.askquestion(message=f"{n1}{signo}{n2}={ope} ¿Deseas guardar en la base de datos",icon="question")
        if resultado=="yes":
            exito=operaciones.Operaciones.insertar(n1,n2,signo,ope)
            if exito:
                messagebox.showinfo(title="..::Acción realizada con éxito::..")
    def consultar():
        messagebox.showinfo(text="Funciono")

    @staticmethod
    def borrar(id):
        exito=operaciones.Operaciones.eliminar(id)
        if exito:
            messagebox.showinfo(title="..::Acción realizada con éxito::..")

    @staticmethod
    def actualizar(numero1,numero2,signo,resultado,id):
        
        exito=operaciones.Operaciones.actualizar(numero1,numero2,signo,resultado,id)
        if exito:
            messagebox.showinfo(title="..::Acción realizada con éxito::..")
           