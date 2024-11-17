import json
from modelos.entidadVineria import EntidadVineria
 
 #hereda de entidadVineria
class Bodega(EntidadVineria):

    def __init__(self, id, nombre): 
        super().__init__(id, nombre)

    #consultas#          
    def obtenerVinos(self):
        from vinoteca import Vinoteca

        vinosBodega = []
        vinos = Vinoteca.obtenerVinos()
        for vino in vinos:
            if vino.obtenerBodega().obtenerId() == self.obtenerId():#preguntar
                vinosBodega.append(vino)
        return vinosBodega

            
    def obtenerCepas(self):
        vinosBodega = self.obtenerVinos()
        cepas = []
        
        for vino in vinosBodega:
            for cepa in vino.obtenerCepas():
                if cepa not in cepas:  
                    cepas.append(cepa)
        return cepas


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
    