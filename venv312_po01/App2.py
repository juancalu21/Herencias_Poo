#Problema:Tablas de multiplicar con numero aleatorio
#Nombre: Juan Pablo Calu Romero
#Version: 0.2


#Importamos la funcion randint de la libreria random para generar los numeros aleatorios
from random import randint
import os
from modules import funciones
from pynput import keyboard

if __name__=="__main__":

   
#Leemos un string que determinara si el programa se ejecutara o no
    print("Bienvenido, a continuacion mostraremos tablas de multiplicar hasta un numero aleatorio entre 1 y 20...")
    os.system("pause")
    p = "SI"
    print()


    while p =="SI" or "NO":
        if p == "SI": #Este ciclo While funciona con el valor de la variable 'p'
            
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
                
                
            p=input("¿Desea generar nuevas tablas?, Escriba:'SI' o 'NO' =  ")#Lee un string y determina si el ciclo se repite o se cierra
            p= p.upper()
            os.system("cls")
        
            
        elif p=="NO":
            print("_"*50)
            print()

            print("Gracias, vuelva pronto")
            print()
            print("_"*50)
            break

        else:
            print("_"*50)
            print()
            p=input("Digite una opcion valida,  Escriba:'Si' o 'No' =   ")#Lee un string y determina si el ciclo se repite o se cierra
            print("_"*50)
            p= p.upper()
            os.system("cls")
        continue


