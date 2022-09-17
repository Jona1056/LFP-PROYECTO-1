import tkinter
from numeros import Ope as OPERACION
from tkinter import messagebox
from tkinter import *
from tkinter import Tk
import os
import sys
import webbrowser

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
    errores.clear()

    
def leer_archivo():
 try:
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
    reporte = open("RESULTADOS_202000424.html","w+")
    txt="""
        <html>
            <title>
            RESULTADOS
            </title>
            <head>
            <link rel="icon" href="https://i.ibb.co/xhT1W0r/escudo10.png">
            </head>
            <body style="background-color: #E7FAF8;">

            <font face="nunito,arial,verdana">

            <table style="border: hidden; width: 100%; height: 90px; margin-left: auto; margin-right: auto;">
            <tbody style="border: hidden;">
            <tr style="border: hidden; height: 104px;">
            <td style="height: 90px; width: 92%;">
            </td>
            </tr>
            </tbody>

            <h1  style="text-align: center; color:red">"""+str(Operaciones1)+"""</h1>
            """
    reporte.write(txt)
    reporte.close()
    webbrowser.open("RESULTADOS_202000424.html")
    print(Operaciones1)
    print(lista_operaciones1)
 except:
    messagebox.showinfo(title="ERROR", message="ERROR AL ANALIZAR EL ARCHIVO")

    
def guardar_como():
    global ruta

    ruta = filedialog.asksaveasfilename(filetypes=[("lfp","*.lfp")],defaultextension=".lfp") 
    archivo = open(ruta,"w",encoding="utf-8")
    dato_nuevo = txa_comentario.get("1.0",tk.END)
    archivo.write(dato_nuevo)
    archivo.close()
    errores.clear()



def html_errores1():
    if errores != []:
        reporte = open("ERRORES_202000424.html","w+")
      
        txt="""
        <html>
            <title>
            Reporte de Errores
            </title>
            <head>
            <link rel="icon" href="https://i.ibb.co/xhT1W0r/escudo10.png">
            </head>
            <body style="background-color: #E7FAF8;">

            <font face="nunito,arial,verdana">

            <table style="border: hidden; width: 100%; height: 90px; margin-left: auto; margin-right: auto;">
            <tbody style="border: hidden;">
            <tr style="border: hidden; height: 104px;">
            <td style="height: 90px; width: 92%;">
            </td>
            </tr>
            </tbody>
            </table>
            <h1  style="text-align: center;">REPORTE DE ERRORES</h1>
            <table style="height: 54px; width: 90%; border-collapse: collapse; margin-left: auto; margin-right: auto;" border="3">
            <tbody>
            <tr style="height: 36px;background-color: #F67C62">
            <td style="width: 20%; height: 36px; text-align: center;">No.</td>
            <td style="width: 20%; height: 36px; text-align: center;">Lexema</td>
            <td style="width: 20%; height: 36px; text-align: center;">Tipo</td>
            <td style="width: 20%; height: 36px; text-align: center;">COLUMNA</td>
            <td style="width: 20%; height: 36px; text-align: center;">FILA</td>
            </tr>
            """
        for i in range(len(errores)):
            txt+="""
                <tr style="height: 18px;background-color: #FFFFFF">
                <td style="width: 20%; height: 18px; text-align: center;">"""+str(i+1)+"""</td>
                <td style="width: 20%; height: 18px; text-align: center;">"""+str(errores[i][0])+"""</td>
                <td style="width: 20%; height: 18px; text-align: center;">"""+str(errores[i][1])+"""</td>
                <td style="width: 20%; height: 18px; text-align: center;">"""+str(errores[i][2])+"""</td>
                <td style="width: 20%; height: 18px; text-align: center;">"""+str(errores[i][3])+"""</td>
                </tr>


                """

        txt += """  
            </tbody>
            </table>
            </font>
            </body>
            </html>
         """
        
        
        

        reporte.write(txt)
        reporte.close
        webbrowser.open("ERRORES_202000424.html")
      
    else:
        messagebox.showinfo(title="Atencion", message="Por favor Analize el archivo")

   


    




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

 boton6 = tkinter.Button(ventana,text="Errores",command = html_errores1, padx=20,pady=5,bg="gray",fg="black",font=("arial",12))
 boton6.place(x=20,y=260)

 txa_comentario = scrolledtext.ScrolledText(ventana,padx=0,pady=0,wrap = tk.WORD)
 txa_comentario.place(x=150,y=10)

 


#  txa_comentario = scrolledtext.ScrolledText(widht=40,height=15,wrap=tk.WORD,font={"Arial",17})
#  txa_comentario.grid(column=0,row=0,padx=)




 ventana.mainloop()




