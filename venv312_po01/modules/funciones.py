
from random import randint
import os
from modules import funciones
from pynput import keyboard

def multi(a,b):
    return  a * b

def case_true():
    p="SI"
    if p == "SI": #Este ciclo While funciona con el valor de la variable 
        z = randint(1,20)#En la variable 'z' guardamos el valor aleatorio que genera la funcion randint
        y = 1 #Variable que se usara para el siguiente ciclo While
        print("Se mostraran ", z,"Tablas de multiplicar")#Imprime el valor de 'z' para que el usuario vea cual fue el numero que se genero 
        print()
        i = 1 #Variable que usara el ciclo for

        while y > 0 and y <= z: #Este ciclo while delimitara cuantas veces se generaran tablas segun el valor aleatorio 
            x = 1#Variable que se usara para el siguiente ciclo While
            while x <= z:#Este ciclo while  genera las tablas
                print("Tabla del ", x)#Imprime que tabla se va a mostrar
                print()

                for i in range (1,11):#Este ciclo for itera entre el numero 1 y 10 para realizar las operaciones

                    f=funciones.multi(x,i)#Operacion de multiplicacion 
                            
                    print(x,"*",i,"=",f) #Muestra en pantalla la operacion de la multiplicacion 
                                
                os.system("pause")
                os.system("cls")
                x+=1 #Suma un valor a la variable x
                y +=1#Suma un valor a la variable y
                print()
                print("_"*50)


def case_false():
    print("_"*50)
    print()
    print("Gracias, vuelva pronto")
    print()
    print("_"*50)
    

#def case_invalid(): 

def sumaLista(list):
    suma = 0
    for i in list:
        
        suma += i
        
    return suma

def contadorLista(list):
    contador = 0
    for i in list:
        contador += 1
        
    return contador  

def promedio(list):

    prom = float(sumaLista(list)//contadorLista(list)) 
            
    print(prom) 

    
    



