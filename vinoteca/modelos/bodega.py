import json
from modelos.entidadVineria import EntidadVineria
#from vinoteca import Vinoteca
import vinoteca 

class Bodega(EntidadVineria):

    #hereda de entidadVineria
    def __init__(self, id, nombre): 
        super().__init__(id, nombre)

    #<<Consultas>>          
    def obtenerVinos(self):
        
        vinosDeLaBodega = []
        vinos = vinoteca.Vinoteca.obtenerVinos()
        for vino in vinos:
            if vino._bodega._id == self._id:
                vinosDeLaBodega.append(vino)
        return vinosDeLaBodega
        
    def obtenerIdsVinos(self):
            idsVinosDeLaBodega = []
            vinos = vinoteca.Vinoteca.obtenerVinos()
    
            for vino in vinos:
             print(f"Revisando vino ID: {vino._id}, Bodega ID: {vino._bodega._id}")  # Debugging
            if vino._bodega and vino._bodega._id == self._id:
                idsVinosDeLaBodega.append(vino._id)
    
            print("IDs de vinos de la bodega:", idsVinosDeLaBodega)  # Debugging
            return idsVinosDeLaBodega
            
    def obtenerCepas(self):
        vinosDeLaBodega = self.obtenerVinos()
        cepas = []
        
        for vino in vinosDeLaBodega:
            for cepa in vino.cepas:  
                if cepa not in cepas:  
                    cepas.append(cepa)

        return cepas

######################################################################
######Esto ya estaba en el código original

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
        return list(vinosMapa)