#Problema:Tablas de multiplicar con numero aleatorio
#Nombre: Juan Pablo Calu Romero
#Version: 0.3

#Importamos las librerias necesarias para la ejecucion del programa
import os
from modules import funciones
from colorama import Fore, Back, Style, just_fix_windows_console
just_fix_windows_console()

if __name__=="__main__":
   
#Leemos un string que determinara si el programa se ejecutara o no
    os.system("cls")
    print(Fore.LIGHTRED_EX, Back.WHITE+ 'Bienvenido, a continuacion mostraremos tablas de multiplicar hasta un numero aleatorio entre 1 y 20...')
    os.system("pause")
    p = "SI"
    print()   

    while p =="SI" or "NO":
        if p == "SI": #Este ciclo While funciona con el valor de la variable 

            funciones.case_true()

            p=input("¿Desea generar nuevas tablas?, Escriba:'SI' o 'NO' =  ")#Lee un string y determina si el ciclo se repite o se cierra
            p= p.upper()
            os.system("cls")    
            
        elif p=="NO":

            funciones.case_false()
            break

        else:
            print("_"*50)
            print()
            p=input("Digite una opcion valida,  Escriba:'Si' o 'No' =   ")#Lee un string y determina si el ciclo se repite o se cierra
            print("_"*50)
            p= p.upper()
            os.system("cls")
   
        continue

        
