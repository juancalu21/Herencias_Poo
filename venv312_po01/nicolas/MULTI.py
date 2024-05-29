'''
SENA CBA 
FICHA: 2877795
APRENDIZ: Nicolas Andres Acosta Higuera 
VERSION: 1.0
FECHA: 25/04/2024
'''
from random import randint
import msvcrt
import time
import os

#Se importa libreria random para generar numeros aleatorios
from random import randint
import msvcrt
import time
import os

opciones='si'
#Pregunta al usuario si quiere generar tablas de multiplicar aleatorias

while True:
    print()
    print('*'*30)
    print('TABLAS DE MULTIPLICAR')
    print( )
    print('*'*30)
    print()
    os.system('Pause')


    '''
    #Pregunta al usuario si quiere generar tabla
    s de multiplicar aleatorias
    print('¿Quiere generar tablas de multiplicar aleatorias?') 
    print('                    Escriba Si o NO              ')
    user =input ().lower() #se usa .lower() para que la respuesta siempre la tome en minusculas


    User='no'

    #Condicional para validar la respuesta del usuario
    if user=='no':
        print('GRACIAS POR USAR EL PROGRAMA')
        break #se rompe el ciclo para terminar el programa

    elif not user in opciones:
        print('Opcion invalida')
        continue #vuelve a preguntar al usuario si quiere generar tablas de multiplicar aleatorias y se salta el ciclo para reiniciarse en este punto
    '''

    #Se genera un numero aleatorio entre 1 y 20
    aleatorio=randint(1,20)
    print ('NUMERO DE TABLAS ALEATORIAS: ',aleatorio)
    numero=1


    #Se genera un ciclo para generar las tablas de multiplicar aleatorias


    while numero> 0 and numero <= aleatorio:
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
                f2=1
                f1=1
                producto= f1*f2
                
                print (numero,'x',f2,'=',producto)
                
            print ('*** Precione una tecla para continuar ***')
            os.system('Pause')
            f1+=1#se aumenta el valor de f1 para que se genere la siguiente tabla de multiplicar
            numero+=1 #se aumenta el valor de numero para que se genere la siguiente tabla de multiplicar
                #Pregunta al usuario si quiere generar tablas de multiplicar aleatorias



#Pregunta al usuario si quiere generar tablas de multiplicar aleatorias
print('¿Quiere generar tablas de multiplicar aleatorias?') 
print('                    Escriba Si o NO              ')
user =input ().lower() #se usa .lower() para que la respuesta siempre la tome en minusculas



#Condicional para validar la respuesta del usuario
if user=='no':
    print('GRACIAS POR USAR EL PROGRAMA')
    
elif not user in opciones:
    print('Opcion invalida')
 #vuelve a preguntar al usuario si quiere generar tablas de multiplicar aleatorias y se salta el ciclo para reiniciarse en este punto


