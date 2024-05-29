from random import randint

#*******
#Ficha: 2877795
#Versión: 1.0
#Aprendiz: Melanie Lozano - Juan Calú 
#Fecha: 25/04/2024
#*******

#Aqui guardamos numeros aleatorios generados mediante la funcion randint en dos variables
n1 = randint(0,100)
n2 = randint(0,100)

#Estamos definiendo una funcion que muestra un mensaje en pantalla
def saludo():
    print("Hola Ficha 2877795 ")

#Determina si la funcion saludo debe ejecutarse o no
if __name__=="__main__":
    saludo()

#Define una funcion que suma dos valores (num1 y num2)
def suma(num1, num2):
    return num1 + num2

#Define una funcion que resta dos valores (num1 y num2)
def resta(num1, num2):
    return num1 - num2

#Define una funcion que multiplica dos valores (num1 y num2)
def multip(num1, num2):
    return num1 * num2

#Define una funcion que divide dos valores (num1 y num2)
def division(num1, num2):
    return num1 / num2
#Aqui mostramos en pantalla los valores que arrojo la funcion de aleatorio

print("***********")
print("El primer valor es: ", n1)
print("El segundo valor es: ", n2)
print("***********")
print()

#imprime en pantalla los resultados de las funciones anteriores
print("*****Inicio******")
print("La suma es: ", suma (n1,n2))
print("La resta es: ", resta (n1,n2))
print("La multiplicacion es: ", multip (n1,n2))

if n2 == 0:
    print("No se puede dividir ningun valor por 0")
else:
    print("La division es: ", division (n1,n2))
print("*****Fin******")