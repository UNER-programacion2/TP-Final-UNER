import json
from modelos.entidadVineria import EntidadVineria
   
#hereda de Entidad vineria#
class Cepa(EntidadVineria):

    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    #consultas#
    def obtenerVinos(self):  
        from vinoteca import Vinoteca 

        vinosCepa = []
        vinos = Vinoteca.obtenerVinos()
        for vino in vinos:
            if self in vino.obtenerCepas():
                vinosCepa.append(vino)
        return vinosCepa
    
    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)
    
