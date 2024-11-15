from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    
    @abstractmethod
    def __init__(self, id: str, nombre:str):
        self._id = id
        self._nombre = nombre

###<<COMANDOS>>###
    
    def establecerNombre(self, nombre: str):
        self._nombre = nombre

###<<CONSULTAS>>### 
    
    def obtenerId(self):
        return self._id

    def obtenerNombre(self):
        return self._nombre
    
###c)sobrescribir consulta, comparando dos objetos###
   #consultar si va el @abstractmethod acá
    def __eq__(self, other):
        if not isinstance(other, EntidadVineria):
            return False
        return self._id == other._id



