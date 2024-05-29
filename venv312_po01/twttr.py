

def main():
    palabra = input("Ingrese una palabra: ")
    resultado = twt(palabra)
    print("La palabra abreviada es: " + ''.join(resultado))

def twt(pal):
    pal= pal.lower()
    sal=[]
    for z in range (len(pal)):
        if pal[z] not in ["a","e","i","o","u"," "]:
            sal.append(pal[z])
    return sal
    
if __name__=="__main__":
    main()