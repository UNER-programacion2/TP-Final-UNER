from abc import ABC, abstractmethod
# EntidadVineria 
# <<Atributos de clase>> 
# <<Atributos de instancia>>  
# id: string 
# nombre: string 
# <<Constructores>> 
# EntidadVineria(id, nombre: string) 
# <<Comandos>> 
# establecerNombre(nombre: string) 
# <<Consultas>> 
# obtenerId(): string 
# obtenerNombre(): string 
 
# a. Utilizar el archivo entidadvineria.py 
# b. Se debe sobreescribir la consulta __eq__ para que compare dos objetos 
# de la clase por el atributo de instancia id. 
# c. EntidadVineria  debe  ser  una  clase  abstracta,  es  decir,  no  debe  poder 
# instanciarse objetos de dicha clase directamente.  

class EntidadVineria(ABC):
    
    def __init__(self, id: str, nombre:str):
        self.id = id
        self.nombre = nombre

# <<Comandos>>
    def establecerNombre(self, nombre: str):
        self.nombre = nombre

# <<Consultas>> 
    def obtenerId(self):
        pass

    def obtenerNombre(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, EntidadVineria):
            return False
        return self.id == other.id