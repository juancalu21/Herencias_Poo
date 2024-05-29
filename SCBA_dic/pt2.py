import os
def buscarFicha(general, llave, valor):
    os.system("cls")
    for diccionario in general:
        if llave in diccionario and diccionario[llave] == valor:
            print(diccionario["NOMBRE"],diccionario["FICHA"])
    else:
        print("-no hay-")
        
general = [{
            
            "DOCUMENTO": 1010062647,
            "NOMBRE": "Juan Pablo Calu",
            "FICHA": 2877795,
            "EVALUACION": "A",
        }]
        
llave = "FICHA"
valor = int(input())
buscarFicha(general, llave, valor)