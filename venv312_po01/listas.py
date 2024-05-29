from random import randint
from modules import funciones
       
list = []
x=randint(0,20)
while x != 0:
    x=randint(0,20)
    if x != 0:
        list +=[x]
print(list)  

 

print("\nLa suma de los valires dentro de la lista es: ",funciones.sumaLista(list))
print("\nLa longitud de la lista es de: ",funciones.contadorLista(list), "numeros\n")

funciones.promedio(list)