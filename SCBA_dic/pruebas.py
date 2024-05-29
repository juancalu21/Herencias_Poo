def buscarLista(general):
    os.system("cls")
    print("\nDocumento__||_Nombre_________________||_Ficha___||Eva||\n")
    for i in general:
        for clave, valor in i.items():
            Value =(f"{valor<20}").format(DOCUMENTO = DOCUMENTO, NOMBRE = NOMBRE, FICHA = FIHCA, EVALUACION = EVALUACION)
            print(Value) 
        print(" ")
      #input("Presiona Enter para continuar...")


buscarLista()