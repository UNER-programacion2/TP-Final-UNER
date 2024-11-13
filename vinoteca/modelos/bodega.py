import json
from modelos.entidadVineria import EntidadVineria

class Bodega(EntidadVineria):

    #hereda de entidadVineria
    def __init__( id, nombre): 
        super().__init__( id, nombre)

    #<<Consultas>>           Plantear el uso de GET Y SET
    def obternerVinos(self):
        from vinoteca import Vinoteca 
        
        vinosDeLaBodega = []
        vinos = Vinoteca.obtenerVinos()
        for vino in vinos:
            if vino.bodega._id == self._id:
                vinosDeLaBodega.append(vino)
        return vinosDeLaBodega
    
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