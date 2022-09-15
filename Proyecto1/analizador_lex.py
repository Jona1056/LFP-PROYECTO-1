import tkinter
from numeros import Ope as OPERACION


D = ["0","1","2","3","4","5","6","7","8","9"]

A = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
R= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
global Ope
columna = 1
global Texto
Texto = []
global funcion_escribir
funcion_escribir = []
global variables
global resultado
global lista_operaciones
resultado = 0
Ope = ""
global txt
global wh
lista_operaciones = []
global tamaño
fila = 0 
txt = ""
global contador_oper




errores =[]

variables =[]
global cnt
cnt = 0
S = ["<", ">", "=", "." , "/", "[" , "]"]

class Lexico:
    global Ope
    contador = 0
    vaa = 0
    angular_abierta = 0
    igual = False

    dato1 = ""
    dato2 = ""
    dato3 = ""
    global wh
    global resultado
    wh = 0
  



    def __init__(self):
      
        self.linea = 1
        self.columna = 1
        self.fila = 1 
    
    def Analizar(self, cadena):
        dato1 = ""
        dato2 = ""
        dato3 = ""
        estado = 0
        est = 0
        puntero = 0
        Ope = ""
        contador_oper = 0
        espacio_texto = 0
        TEXTO = ""
        tkn = ""
        tkn2 = ""
        texto_titulo  = ""

    

        while puntero < len(cadena):
        
         char = cadena[puntero]
       
         ## si el primer caracter que viene es un salto de linea
         if ord(char) == 10:
                self.columna = 1
                self.linea += 1 
                puntero += 1 
            ## si viene tabulador
         elif ord(char) == 9:
                self.columna += 1
                puntero += 1 
            ## si viene espacio blanco
         elif ord(char) == 32:
                espacio_texto = 1
                self.columna += 1
                puntero += 1
         else:
            if estado ==0:
            ##si el primer caracter que viene es <
               wh = 0
               
               if char in S:
                
                estado = 1 
                puntero += 1
                self.columna += 1 
      
         
         
               else:  
                listanueva = [char, "Error",self.columna,self.linea]
                errores.append(listanueva)
                puntero += 1
                self.columna += 1
                estado = 0

            elif estado == 1:
              
                if char in A:
                
                    self.columna += 1
                    puntero += 1
                    estado = 2
                    tkn += char
              
                elif char == "/":
                    self.columna+=1
                    puntero+=1
                    estado = 1
                    tkn+=char
                else:
                    listanueva = [char, "Error",self.columna,self.linea]
                    errores.append(listanueva)
                
                    puntero+=1
                    self.columna+=1
                    estado = 1
                    
            elif estado == 2:
                if char in R:
                    self.columna += 1
                    puntero += 1
                    tkn += char
                    estado = 3
                elif char in A:
                    self.columna += 1
                    puntero += 1
                    tkn += char
                    estado = 3
                 
                else: 
                    listanueva = [char, "Error, en Palabra",self.columna,self.linea]
                    errores.append(listanueva)
                    print("error")
                    break
            elif estado == 3:
           
                if (char) in S:
                    self.columna += 1
                    puntero += 1
                    estado = 4
                   
                elif char in R: 
                    estado = 2
                elif char in A:
                    estado = 2
                else: 
                    listanueva = [char,"Error", self.columna,self.linea]
                    errores.append(listanueva)
                    estado = 4
                    puntero +=1
                    self.columna+=1
                  
            elif estado == 4:
          
                if tkn =="Tipo":
        
                    estado = 0
                    
                    tkn = ""
                elif tkn == "Operacion":
                    contador_oper +=1
             
                    tkn = ""
                    estado = 5
                elif tkn == "Numero":
                  
                    tkn = ""
                    estado = 7
                elif tkn == "/Operacion":
                    tkn= ""
                    contador_oper  = contador_oper-1
                    if contador_oper == 0:
                     try:
                    
                      estado = 0
                    
                     except:
                        als ="no hace nada"
                        estado = 14
                    else :
                        estado = 14
                elif tkn == "/Tipo":
                    tkn = ""
                    estado = 0
                elif tkn == "Texto":
                    tkn = ""
                    estado = 15
                elif tkn == "Funcion":
                    tkn = ""
                    estado = 5
                elif tkn == "Titulo":
                    tkn = ""
                    estado = 16
                elif tkn == "Descripcion":
                    tkn = ""
                    estado = 16
                elif tkn == "Contenido":
                    tkn = ""
                    estado = 16
                elif tkn == "/Funcion":
                 
                    tkn = ""
                    estado = 0
                elif tkn == "Estilo":
                  
                    estado = 17
                    tkn = ""
               
          
                   
            
                    
                    
                    
                    
                    
                 
                   
                  
                   

                else:
                    listanueva = [char, "no se Encontro Palabra Reservada",self.columna,self.linea]
                    errores.append(listanueva)
                    break

            elif estado == 5:
              
                if char in A:
                    self.columna +=1
                    puntero +=1
                    tkn += char
                    estado = 5
                elif char in S:
                    self.columna +=1
                    puntero +=1
                    estado = 6
                else: 
                    listanueva = [char,"Error", self.columna,self.linea]
                    errores.append(listanueva)
                    estado = 6
                    puntero+=1
                    self.columna+=1
            elif estado == 6:
               
                if tkn == "SUMA":
                    Ope = tkn
                    tkn = ""
                    
             
                    estado = 0
                elif tkn == "RESTA":
                    Ope = tkn
                    tkn = ""
                    
                    estado = 0
                elif tkn =="MULTIPLICACION":
                    Ope = tkn
                    tkn = ""
                    estado = 0
                elif tkn == "DIVISION":
                    Ope = tkn
                    tkn = ""
                    estado = 0
                elif tkn == "POTENCIA":
                    Ope = tkn
                    tkn = ""
                    estado = 0
                elif tkn == "RAIZ":
                    Ope = tkn
                    tkn = ""
                    estado = 0
                elif tkn == "ESCRIBIR":
                    tkn = 0
                    tkn = ""
                    estado = 0
                else:
                    listanueva = [char, "no se Encontro Palabra Reservada",self.columna,self.linea]
                    errores.append(listanueva)
                    break

            elif estado == 7:
                
                if char in D:
                  
                 
                
                    self.columna +=1
                    puntero +=1
                    estado = 8
                    dato1 += char
            
                
                else:
                     listanueva = [char, "Error",self.columna,self.linea]
                     errores.append(listanueva)
                     estado == 8
                     puntero +=1
                     self.columna+=1
                
            elif estado == 8:
             
                if char in D:
                    self.columna +=1
                    puntero +=1
                    dato1+=char
                    estado = 8
                elif char == ".":
                    self.columna +=1
                    puntero +=1
                    dato1 +=char
                    estado = 8
                elif char == "<":
               
                    estado = 9
                    puntero += 1
                    self.columna+=1
                else:
                     listanueva = [char, "Error",self.columna,self.linea]
                     errores.append(listanueva)
                     puntero+=1
                     self.columna+=1
                     estado = 9
            elif estado == 9:
           
                if char == "/":
                    estado = 10
                    puntero+=1
                    self.columna+=1
                else:
                    listanueva = [char,"Error",self.columna,self.linea]
                    errores.append(listanueva)
                    estado = 10
                    puntero+=1
                    self.columna+=1
            elif estado == 10:
                if char in A:
                    puntero +=1
                    self.columna+=1
                    estado = 11
                    tkn +=char
                else:
                    listanueva = [char,"Error",self.columna,self.linea]
                    errores.append(listanueva)
                    self.columna+=1
                    puntero+=1
                    estado = 11
            elif estado == 11:
                if char in R:
                    self.columna+=1
                    puntero+=1
                    tkn+=char
                    estado = 12
                else:
                    listanueva = [char, "Error, en Palabra",self.columna,self.linea]
                    errores.append(listanueva)
                   
                    break
            elif estado == 12:
              
                if char in S:
                    self.columna+=1
                    puntero+=1
                    estado = 13
                elif char in R:
                    estado = 11
                elif char in A:
                    estado = 11
                else: 
                    listanueva = [char,"Error", self.columna,self.linea]
                    errores.append(listanueva)
                    estado = 13
                    puntero +=1
                    self.columna+=1
            elif estado == 13:
              
                if tkn == "Numero":
                    list = [Ope,dato1]
                    variables.append(list)
                    dato1 = ""
                    estado = 0
                    tkn = ""
                elif tkn == "Tipo":
                    estado = 0
                    tkn = ""
                elif tkn == "Texto":
                    estado = 0
                    tkn = ""
                elif tkn == "Titulo":
                    estado = 0
                    tkn = ""
                elif tkn == "Descripcion":
                    estado = 0
                    tkn = ""
                elif tkn == "Contenido":
                    estado = 0
                    tkn = ""
                  

                    
                else:
                    listanueva =[char,"Error en palabra de cierre",self.columna,self.fila]
                    errores.append(listanueva)
                    break
            elif estado == 14:
                variables.clear()
              
                
                estado = 0
            
            elif estado == 15:
                if char == "<":
                    estado = 9
                    self.columna+1
                    puntero+=1
                    
                else:
                    self.columna+1
                    puntero+=1
                    if espacio_texto == 1:
                     
                        tx = " "
                        TEXTO+=tx
                        TEXTO+=char
                        estado = 15
                        espacio_texto = 0
                    else:
                     TEXTO +=char
                     estado = 15
            elif estado == 16:
                
                if char == "<":
                    estado = 9
                    self.columna+1
                    puntero+=1
                    funcion_escribir.append(texto_titulo)
                    texto_titulo = ""
                else:
                    self.columna+1
                    puntero+=1
                    if espacio_texto == 1:
                        tx = " "
                        texto_titulo  +=tx
                        texto_titulo  +=char
                        estado = 16
                        espacio_texto = 0
                    else: 
                        texto_titulo +=char
                        estado = 16
            elif estado == 17: 
                if char in S:
                
                    estado = 18
                    puntero += 1
                    self.columna += 1 
                else:  
                    listanueva = [char, "Error",self.columna,self.linea]
                    errores.append(listanueva)
                    puntero += 1
                    self.columna += 1
                    estado = 17
            elif estado == 18:
                if char in A:
                    tkn +=char
                    puntero+=1
                    estado = 19
                    self.columna+1
                else:
                    listanueva = [char, "Error",self.columna,self.linea]
                    errores.append(listanueva)
                
                    puntero+=1
                    self.columna+=1
                    estado = 19
            elif estado == 19:
                if char in R:
                    tkn+=char
                    if tkn == "Titulo":
                        estado = 20
                        self.columna+=1
                        puntero+=1
                      
                    else:
                        estado = 19
                        self.columna+=1
                        puntero+=1
                else:
                    listanueva = [char, "Error",self.columna,self.linea]
                    errores.append(listanueva)
                
                    puntero+=1
                    self.columna+=1
                    estado = 19
            elif estado == 20:
                print("Hola")
                break

                 



          


                    
                
      




            else: 
               listanueva = [char,"E.P.R" ,self.columna,self.linea]
               errores.append(listanueva)
               self.columna += 1
               puntero += 1
        print(TEXTO)
        print(funcion_escribir)
        OPERACION()    
        
            



  

 

            





    



        
    

  


              

  


       

  
            


            
           

  

   
    
    
