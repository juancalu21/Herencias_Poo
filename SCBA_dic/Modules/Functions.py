import os
general = []
#Definimos la funcion que recibira los datos del diccionario y los agragara a la lista
def crear (general):
    os.system("cls")
    
    #Variable que permite iniciar el ciclo la primera vez
    x = "SI"
    #Ciclo que valida los datos
    while x == "SI":
        #Bloque de ciclos que verifica que los datos ingresados por el usuario sea correctos
        while True:
            print("==="*40)
            docIni = input("Diligencie su documento de identidad: ")
            print("==="*40)
            if docIni.isdigit():
                doc=int(docIni)
                os.system("cls")
                break
            else:                
                os.system("cls")
                print("==="*40)
                print("El valor debe ser numerico")
                print("==="*40)
                continue

        while True:
            print("==="*40)
            nomIni = input("Diligencie su nombre completo: ")
            if nomIni.istitle():
                nom=str(nomIni)
                os.system("cls")
                break
            else:                
                os.system("cls")
                print("==="*40)
                print("El valor debe ser alfabetico y la primera letra de cada nombre debe ser mayuscula.")
                print("==="*40)
                continue

        while True:
            print("==="*40)
            ficIni = input("Numero de su ficha: ")
            if ficIni.isdigit():
                fic=int(ficIni)
                os.system("cls")
                break
            else:                
                os.system("cls")
                print("==="*40)
                print("El valor debe ser numerico")
                print("==="*40)
                continue

        while True:            
            print("==="*40)
            evaIni = input("Evaluacion: ").upper()
            if evaIni.isalpha():
                eva=str(evaIni)
                os.system("cls")
                break
            else:                
                os.system("cls")
                print("==="*40)
                print("El valor debe ser A o D")
                print("==="*40)
                continue

        while True:
            if eva == "A" :
                break
            elif eva == "D" :
                break
            else:
                os.system("cls")
                print("==="*40)
                print("Dato incorrecto el valor debe ser A o D")
                eva = input("Evaluacion: ").upper()
                os.system("cls")
                continue

               
        #fic = int(input("Ficha: "))
        #eva = str(input("Evaluacion: "))
        creador = {
            
            "DOCUMENTO": doc,
            "NOMBRE": nom,
            "FICHA": fic,
            "EVALUACION": eva,
        }

        general += [creador]
        print("==="*40)
        x = input("Desea agregar otro aprendiz? Si / No: ").upper()
        while True:    
                
            if x == "SI":

                break
            elif x == "NO":

                break
            else:
                print("==="*40)
                print("valor incorrecto")
                print("==="*40)
                x = input("Desea agregar otro aprendiz?  Si / No: ").upper()
                continue




    

    print("Gracias")        


def buscarLista(general):
    os.system("cls")
    print("\nDocumento__||_Nombre_________________||_Ficha___||Eva||\n")
    for i in general:
        for clave, valor in i.items():
            print(f"{valor}", end="    ")
        print(" ")
      #input("Presiona Enter para continuar...")
        


def buscarFicha(general, llave, valor):
    os.system("cls")
    for diccionario in general:
        if llave in diccionario and diccionario[llave] == valor:
            print(diccionario["NOMBRE"],diccionario["FICHA"])
    else:
        print("==="*40)
    
def buscarEvaluacion(general, llave, valor):
    os.system("cls")
    for diccionario in general:
        if llave in diccionario and diccionario[llave] == valor:
            print("Aprendiz: ",diccionario["NOMBRE"],"--Nota: ",diccionario["EVALUACION"])
    else:
        print("--"*20)
    

def eliminarAlumno(general, llave, valor):
    #os.system("cls")    
    for diccionario in general:
        if llave in diccionario and diccionario[llave] == valor:
            #.system("cls")
            print(diccionario)
            borrar = input("Desea eliminar al aprendiz? Si / No: ").upper()
            while True:    
                
                if borrar == "SI":
                    if diccionario.get("DOCUMENTO")== valor :
                        general.remove(diccionario)
                        break
                elif borrar == "NO":

                    break
                else:
                    print("valor incorrecto")
                    borrar = input("Desea eliminar al aprendiz? Si / No: ").upper()
                    continue
    else:
        print("--"*20)
        
def actualizarDatos(general, llave, valor):
    os.system("cls")    
    for diccionario in general:
        if llave in diccionario and diccionario[llave] == valor:
            #.system("cls")
            print(diccionario)
            actualizar = input("Desea actualizar Nombre, ficha o evaluacion?: ").upper()
            while True:    
                
                if actualizar == "NOMBRE":
                    diccionario["NOMBRE"] = input("Escriba el nuevo nombre: ")
                    if diccionario["NOMBRE"].istitle():
                        nomn=str(diccionario)
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        print("El valor debe ser alfabetico y la primera letra de cada nombre debe ser mayuscula.")
                        continue
                elif actualizar == "FICHA":
                    ficn = input("Escriba la nueva ficha: ")
                                         
                    if ficn.isdigit():
                        ficn=int(ficn)
                        diccionario["FICHA"] = ficn   
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        print("El valor debe ser numerico")
                        continue
                elif actualizar =="EVALUACION":
                    diccionario["EVALUACION"] = input("Escriba el nuevo EVALUACION: ").upper()
                    if diccionario["EVALUACION"].isalpha():
                        evan=str(diccionario)
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        print("El valor debe ser A o D")
                        continue
                    
                    while True:
                        if evan == "A" :
                            break
                        elif evan == "D" :
                            break
                        else:
                            os.system("cls")
                            print("Dato incorrecto el valor debe ser A o D")
                            evan = input("Evaluacion: ").upper()
                            os.system("cls")
                            continue
                else:
                    os.system("cls")
                    print("==="*40)
                    print("Valor incorrecto")
                    actualizar = input("Desea actualizar Nombre, ficha o evaluacion?: ").upper()
                    print("==="*40)
                    continue


    else:
        print("--"*20)


def gestion():
    while True: 
        
        resp = oper()

        if resp == 1:
            general.clear()
            os.system("cls")
            print("==="*40)
            print("Parametrizado")
            print("==="*40)
            print("Desea realizar otra accion ?")    
            app()
            

        elif resp == 2:
            os.system("cls")

            crear(general)
            os.system("cls")
            print("==="*40)
            print("Desea realizar otra accion ?")    
            app()
            
        elif resp == 3:
            os.system("cls")
            buscarLista(general)
            input("Presione enter para continuar")
            os.system("cls")
            print("==="*40)
            print("Desea realizar otra accion ?")    
            app()
            
        elif resp == 4:
            os.system("cls")  
            while True:
                
                buscarValor =input("Digite la ficha que desea buscar: ")
                if buscarValor.isdigit(): 
                    llave = "FICHA"
                    buscarValor = int(buscarValor)
                    os.system("cls")
                    print("Nombre-----------------Ficha")
                    buscarFicha(general, llave, buscarValor) 
                    input("Presione enter para continuar")
                    os.system("cls")
                    print("==="*40)
                    print("Desea realizar otra accion ?")    
                    app()
                    break
                else: 
                    print("Valor incorrecto")
                    continue
        
        elif resp == 5:
            os.system("cls")
            while True:
                buscarValor =input("Digite la ficha que desea buscar: ")
                if buscarValor.isdigit():
                    llave = "FICHA"
                    buscarValor = int(buscarValor)
                    os.system("cls")
                    print("Nombre-----------------Evaluacion")
                    buscarEvaluacion(general, llave, buscarValor)
                    input("Presione enter para continuar")
                    os.system("cls")
                    print("==="*40)
                    print("Desea realizar otra accion ?")                
                    app()
                    break
                else: 
                    print("Valor incorrecto")
                    continue
        
        elif resp == 6:
            os.system("cls")
            while True:
                buscarLista(general)
                print()
                buscarValor =input("Digite el documento del aprendiz que desea eliminar: ")
                if buscarValor.isdigit():
                    llave = "DOCUMENTO"
                    buscarValor = int(buscarValor)
                    eliminarAlumno(general, llave, buscarValor)
                    input("Presione enter para continuar")
                    os.system("cls")
                    print("==="*40)
                    print("Desea realizar otra accion ?")                
                    app()
                    break
        
        elif resp == 7:
            os.system("cls")
            while True:
                buscarLista(general)
                print()
                buscarValor =input("Digite el documento del aprendiz que desea actualizar: ")
                if buscarValor.isdigit():
                    llave = "DOCUMENTO"
                    buscarValor = int(buscarValor)
                    actualizarDatos(general, llave, buscarValor)
                    input("Presione enter para continuar")
                    os.system("cls")
                    print("==="*40)
                    print("Desea realizar otra accion ?")                
                    app()
                    break
        
        elif resp == 0:
            os.system("cls")
            print("Gracias, vuelva pronto")  
            break 
        
        else:
            os.system("cls")
            print("Valor incorrecto")
            app()
            continue 

def app():
    general = []
     
    print("==="*40)
    print("1. Parametrizar.")
    print("2. Ingresar aprendiz.")
    print("3. Lista aprendices.")
    print("4. Lista por fichas.")
    print("5. resultados por fichas")
    print("6. Borrar aprendiz")
    print("7. Actualizar informacion")
    print("0. salir ")
    print("==="*40)
    
def oper():
    while True:
        oper = input("Digita el numero de la accion que deseas realizar: ")
        if oper.isdigit(): 
            oper =  int(oper)           
            return oper
            break
        else:
            os.system("cls")
            print("Valor incorrecto")
            app()
            continue 