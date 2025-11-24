'''
Crear una calculador:
1.- Dos campos de texto
2.- 4 botones para las operaciones
3.- Mostrar el resultado en una alerta
'''

from tkinter import messagebox
from tkinter import *
#Control app o controler

def mostrar_reusltado(resultado,n1,n2,op):
    operacion=""
    match op:
        case "+":
            operacion="suma"
        case"-":
            operacion="Resta"
        case "*":
            operacion="Multiplicacion"
        case "/":
            operacion="Division"

    messagebox.showinfo(title=operacion,icon="info",message=f"{n1}{op}{n2}={resultado}")


def sumar(numero1,numero2):
    suma=numero1+numero2
    op="+"
    mostrar_reusltado(suma,numero1,numero2,op)

def resta(numero1,numero2):
    resta=numero1-numero2
    op="-"

    mostrar_reusltado(resta,numero1,numero2,"-")

    #messagebox.showinfo(title="Resta",icon="info",message=f"{numero1}-{numero2}={resta}")


def multipliacion(numero1,numero2):
    mult=numero1*numero2
    op="x"
    mostrar_reusltado(mult,numero1,numero2,op)

    #messagebox.showinfo(title="Multiplicacion",icon="info",message=f"{numero1}*{numero2}={mult}")


def division(numero1,numero2):
    div=numero1/numero2
    op="/"

    mostrar_reusltado(div,numero1,numero2,op)

    #messagebox.showinfo(title="Division",icon="info",message=f"{numero1}/{numero2}={div}")


#Interfaz o view
ventana=Tk()
ventana.title("Calculadora")
ventana.geometry("600x400")
ventana.resizable(False,False)

#Variables para los entry
n1=IntVar()
n2=IntVar()

txt_numero1=Entry(ventana,textvariable=n1,width=5,justify="right")
txt_numero1.pack(side="top",anchor="center")


txt_numero2=Entry(ventana,textvariable=n2,width=5,justify="right")
txt_numero2.pack(side="top",anchor="center")


btn_suma=Button(ventana,text="+",command=lambda:sumar(n1.get(),n2.get()))
btn_suma.pack()


btn_resta=Button(ventana,text="-",command=lambda:resta(n1.get(),n2.get()))
btn_resta.pack()

btn_multiplicacion=Button(ventana,text="X",command=lambda:multipliacion(n1.get(),n2.get()))
btn_multiplicacion.pack()

btn_division=Button(ventana,text="/",command=lambda:division(n1.get(),n2.get()))
btn_division.pack()




btn_salir=Button(ventana,text="Salir",command=ventana.quit)
btn_salir.pack()
ventana.mainloop()
