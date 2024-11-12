import json
from modelos.entidadVineria import EntidadVineria 
#from vinoteca import Vinoteca


class Bodega(EntidadVineria):
    
    def __init__(self, id, nombre):
        super().__init__(self, id, nombre)

    #<<Consultas>>           Plantear el uso de GET Y SET
    def obternerVinos(self):
        from vinoteca import Vinoteca 
        
        vinosDeLaBodega = []
        vinos = Vinoteca.obtenerVinos()
        for vino in vinos:
            if vino.bodega.id == self._id:
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
       
    # def obtenerCepas(self):
    #   vinosBodega = self.obtenerVinos()
    #   cepasDeLaBodega = set()
    #   for vino in vinosBodega:
    #     cepasDeLaBodega.add(vino.cepa)
    #   return list(cepasDeLaBodega)
    
    
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
