import tkinter
from numeros import Ope as OPERACION
from tkinter import messagebox
from tkinter import *
from tkinter import Tk
import tkinter as tk
import os
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
from analizador_lex import *
from numeros import Operaciones1 as Operaciones1
from numeros import lista_operaciones1 as lista_operaciones1
from analizador_lex import contador_texto as contador_texto
global txa_comentario 

archivo_nuevo = ""



def abrir_archivo():
     global ruta
    #  a = Lexico()
     ruta = filedialog.askopenfilename()
     archivo = open(ruta,"r",encoding="utf-8")
     input = archivo.read()
     archivo_nuevo = input
     txa_comentario.delete("1.0",tk.END)
     txa_comentario.insert("1.0",archivo_nuevo)
   
    #  analizar = a.Analizar(input)
    #  print(errores)

def Guardar():
    global ruta
    archivo = open(ruta,"w",encoding="utf-8")
    dato_nuevo = txa_comentario.get("1.0",tk.END)
    archivo.write(dato_nuevo)
    archivo.close()

    
def leer_archivo():
    global ruta
    ## Inicio()

   
    
    a = Lexico()
    f = open(ruta, 'r',encoding="utf-8")
    input = f.read()
    f.close()
    analizar = a.Analizar(input)
 
    x1 = str(contador_texto[0])
    x1+=".0"
   

    oper = txa_comentario.get("1.0",x1)
    file = open("Operaciones.txt", "w")
    file. write(oper)
    file. close()
    OPERACION()
    print(Operaciones1)
    print(lista_operaciones1)

    
def guardar_como():
    global ruta

    ruta = filedialog.asksaveasfilename(filetypes=[("txt","*.txt")],defaultextension=".txt") 
    archivo = open(ruta,"w",encoding="utf-8")
    dato_nuevo = txa_comentario.get("1.0",tk.END)
    archivo.write(dato_nuevo)
    archivo.close()

def errores1():
    print(errores)
   


    




def Inicio():
 global ventana
 global txa_comentario
 ventana = tkinter.Tk()
 ventana.title("Analizador Lexico")
 ventana.geometry("1000x450")
 ventana.configure(background="black")




 boton1 = tkinter.Button(ventana,text="Abrir",command=abrir_archivo,padx=32,pady=5,bg="gray",fg="black",font=("arial",12))
 boton1.place(x=20,y=20)

 boton2 =  tkinter.Button(ventana,text="Guardar",command= Guardar,padx=20,pady=5,bg="gray",fg="black",font=("arial",12))
 boton2.place(x=20,y=80)

 boton3 = tkinter.Button(ventana,text="Guardar como",command= guardar_como,padx=0,pady=5,bg="gray",fg="black",font=("arial",12))
 boton3.place(x=20, y=140)

 boton4 = tkinter.Button(ventana,text="Salir",command=ventana.destroy, padx=5,pady=5,bg="gray",fg="black",font=("arial",12))
 boton4.place(x=20,y=320)
 
 boton5 = tkinter.Button(ventana,text="Analizar",command = leer_archivo ,padx=20,pady=5,bg="gray",fg="black",font=("arial",12))
 boton5.place(x=20,y=200)

 boton6 = tkinter.Button(ventana,text="Errores",command = errores1, padx=20,pady=5,bg="gray",fg="black",font=("arial",12))
 boton6.place(x=20,y=260)

 txa_comentario = scrolledtext.ScrolledText(ventana,padx=0,pady=0,wrap = tk.WORD)
 txa_comentario.place(x=150,y=10)

 


#  txa_comentario = scrolledtext.ScrolledText(widht=40,height=15,wrap=tk.WORD,font={"Arial",17})
#  txa_comentario.grid(column=0,row=0,padx=)




 ventana.mainloop()




