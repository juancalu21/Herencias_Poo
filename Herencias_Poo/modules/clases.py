
class Persona:
    
    def __init__(self,documento,nombreCompleto) :
        
        self.__documento = documento
        self.__nombreCompleto = nombreCompleto
        
        
    def get_documento(self):
        return self.__documento
    
    def set_documento(self, value):
        self.__documento = value    
    
    def get_nombreCompleto(self):
        return self.__nombreCompleto
    
    def set_nombreCompleto(self, value):
        self.__nombreCompleto = value 
        
    def informacion():
        persona1 = Persona("","")
        documento = int(input("Ingrese el documento"))
        persona1.set_documento(documento)
        
        nombre = int(input("Ingrese el Nombre completo"))
        persona1.set_nombreCompleto(nombre)
        

class Aprendiz(Persona):
    
    def __init__(self, documento, nombreCompleto, ficha, programa):
        super().__init__(documento, nombreCompleto)
    
    def get_ficha(self):
        return self.__ficha
    
    def set_ficha(self, value):
        self.__ficha = value        
    
    def get_programa(self):
        return self.__programa
    
    def set_programa(self, value):
        self.__programa = value    
    
    
class EtapaLectiva(Aprendiz):
    
    def __init__(self, documento, nombreCompleto, ficha, programa):
        super().__init__(documento, nombreCompleto, ficha, programa)