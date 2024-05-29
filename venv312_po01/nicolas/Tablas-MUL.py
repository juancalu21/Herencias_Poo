'''
SENA CBA 
FICHA: 2877795
APRENDIZ: Nicolas Andres Acosta Higuera 
VERSION: 1.0
FECHA: 25/04/2024
'''
def titulo():
        print()
        print('*'*30)
        print('TABLAS DE MULTIPLICAR')
        print( )
        print('*'*30)
        print()


def ciclo_multi():
    #Se genera un numero aleatorio entre 1 y 20
    aleatorio=randint(1,20)
    numero=1
    print ('NUMERO DE TABLAS ALEATORIAS: ',aleatorio)

    f2=1
    f1=1
    
    #Se genera un ciclo para generar las tablas de multiplicar aleatorias
    while numero> 0 and numero <= aleatorio:
        
        #Se genera un ciclo para generar las tablas de multiplicar
        while f1 <= aleatorio:
            print()
            #Se imprime el titulo de la tabla de multiplicar
            print ('*'*30)
            print()
            #Se imprime el numero de la tabla de multiplicar
            print ('TABLA DE MULTIPLICAR DEL NUMERO: ',numero)
            print ()
            #Se imprimen las tablas de multiplicar
            
            for f2 in range (1,11):
                producto= f1*f2
                print (numero,'x',f2,'=',producto)
            os.system('pause')
            f1+=1                                  #se aumenta el valor de f1 para que se genere la siguiente tabla de multiplicar
            numero+=1                              #se aumenta el valor de numero para que se genere la siguiente tabla de multiplicar

#Se importa libreria random para generar numeros aleatorios
from random import randint
import os
from colorama import Fore, Back
print((Fore.YELLOW),(Back.RED))
import titulo
#Se crea una lista con las |
opciones='si' 
def ciclo_multi():
    #Se genera un numero aleatorio entre 1 y 20
    aleatorio=randint(1,20)
    numero=1
    print ('NUMERO DE TABLAS ALEATORIAS: ',aleatorio)

    f2=1
    f1=1
    
    #Se genera un ciclo para generar las tablas de multiplicar aleatorias
    while numero> 0 and numero <= aleatorio:
        
        #Se genera un ciclo para generar las tablas de multiplicar
        while f1 <= aleatorio:
            print()
            #Se imprime el titulo de la tabla de multiplicar
            print ('*'*30)
            print()
            #Se imprime el numero de la tabla de multiplicar
            print ('TABLA DE MULTIPLICAR DEL NUMERO: ',numero)
            print ()
            #Se imprimen las tablas de multiplicar
            
            for f2 in range (1,11):
                producto= f1*f2
                print (numero,'x',f2,'=',producto)
            os.system('pause')
            f1+=1                                  #se aumenta el valor de f1 para que se genere la siguiente tabla de multiplicar
            numero+=1                              #se aumenta el valor de numero para que se genere la siguiente tabla de multiplicar
#Pregunta al usuario si quiere generar tablas de multiplicar aleatorias

while True:

    
    '''
    #Pregunta al usuario si quiere generar tablas de multiplicar aleatorias
    print('¿Quiere generar tablas de multiplicar aleatorias?') 
    print('                Escribe Si o No                  ')
    print()
    user =input ().strip().lower() #se usa .lower() para que la respuesta siempre la tome en minusculas
    
    #Condicional para validar la respuesta del usuario
    if user=='no':
        print('GRACIAS POR USAR EL PROGRAMA')
        break #se rompe el ciclo para terminar el programa
    
    elif not user in opciones:
        print('Opcion invalida')
        continue #vuelve a preguntar al usuario si quiere generar tablas de multiplicar aleatorias y se salta el ciclo para reiniciarse en este punto
   '''     

    ciclo_multi()
    #Pregunta al usuario si quiere generar tablas de multiplicar aleatorias
    
    #Pregunta al usuario si quiere generar tablas de multiplicar aleatorias
    print('¿Quiere generar tablas de multiplicar aleatorias?') 
    print('                Escribe Si o No                  ')
    print()
    user =input ().strip().lower() #se usa .lower() para que la respuesta siempre la tome en minusculas
    
    #Condicional para validar la respuesta del usuario
    if user=='no':
        print('GRACIAS POR USAR EL PROGRAMA')
        break #se rompe el ciclo para terminar el programa
    
    elif not user in opciones:
        print('Opcion invalida')
        continue #vuelve a preguntar al usuario si quiere generar tablas de multiplicar aleatorias y se salta el ciclo para reiniciarse en este punto

    #Se almacena la respuesta del usuario en la variable user
    ''''''
    user =input ().lower() #se usa .lower() para que la respuesta siempre la tome en minusculas
    
    #Condicional para validar la respuesta del usuario
    if user=='no':
        print('GRACIAS POR USAR EL PROGRAMA')
        break #se rompe el ciclo para terminar el programa
    
    elif not user in opciones:
        print('Opcion invalida')
        continue

       #vuelve a preguntar al usuario si quiere generar tablas de multiplicar aleatorias y se salta el ciclo para reiniciarse en este punto
    
        

            