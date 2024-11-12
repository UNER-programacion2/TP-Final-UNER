from abc import ABC, abstractmethod

# b. Se debe sobreescribir la consulta __eq__ para que compare dos objetos 
# de la clase por el atributo de instancia id. 
# c. EntidadVineria  debe  ser  una  clase  abstracta,  es  decir,  no  debe  poder 
# instanciarse objetos de dicha clase directamente. 
# 
#  
# Estas son las Bodegas, las Cepas y los Vinos. Todas estas entidades 
# poseen  dos  atributos  de  instancia  comunes  a  todas  ellas,  por  lo  que  esta  estructura 
# estará comprendida en la clase abstracta EntidadVineria. 

class EntidadVineria(ABC):
    
    @abstractmethod
    def __init__(self, id: str, nombre:str):
        self._id = id
        self._nombre = nombre

# <<Comandos>>
    def establecerNombre(self, nombre: str):
        self._nombre = nombre

# <<Consultas>> 
    def obtenerId(self):
        return self._id

    def obtenerNombre(self):
        return self._nombre
    
    #@abstractmethod ##consultar si va aca o no
    def __eq__(self, other):
        if not isinstance(other, EntidadVineria):
            return False
        return self.id == other.id



